################################################################################
# MIT License
#
# Copyright (c) 2018-2020 yeggor
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.
################################################################################

import json
import os

import ida_funcs
import ida_graph
import ida_idp
import ida_kernwin
import ida_ua
import idautils

from .utils import get_dep_json

NAME = 'UEFI_RETool'
DEP_GRAPH = None


class _base_graph_action_handler_t(ida_kernwin.action_handler_t):
    def __init__(self, graph):
        ida_kernwin.action_handler_t.__init__(self)
        self.graph = graph

    def update(self, ctx):
        return ida_kernwin.AST_ENABLE_ALWAYS


class GraphCloser(_base_graph_action_handler_t):
    def activate(self, ctx):
        self.graph.Close()


class ColorChanger(_base_graph_action_handler_t):
    def activate(self, ctx):
        self.graph.color = self.graph.color ^ 0xffffff
        self.graph.Refresh()
        return 1


class SelectionPrinter(_base_graph_action_handler_t):
    def activate(self, ctx):
        try:
            sel = ctx.graph_selection
        except:
            sel = ida_graph.screen_graph_selection_t()
            gv = ida_graph.get_graph_viewer(self.graph.GetWidget())
            ida_graph.viewer_get_selection(gv, sel)
        if sel:
            for s in sel:
                if s.is_node:
                    print(f'[{NAME}] selected node {s.node}')
                else:
                    print(
                        f'[{NAME}] selected edge {str(s.elp.e.src)} -> {str(s.elp.e.dst)}'
                    )
        return 1


class DependencyGraph(ida_graph.GraphViewer):
    def __init__(self, dep_json):
        self.title = f'{NAME} dependency graph'
        ida_graph.GraphViewer.__init__(self, self.title)
        self.dep_json = dep_json
        self.pairs = self._get_all_pairs()
        self.color = 0x555555

        class my_view_hooks_t(ida_kernwin.View_Hooks):
            def __init__(self, v):
                ida_kernwin.View_Hooks.__init__(self)
                self.hook()
                import weakref
                self.v = weakref.ref(v)

            def view_loc_changed(self, w, now, was):
                now_node = now.renderer_info().pos.node
                was_node = was.renderer_info().pos.node
                if now_node != was_node:
                    if self.v().GetWidget() == w:
                        print(
                            f'[{NAME}] current node now: {str(now_node)} (was {str(was_node)})'
                        )

        self.my_view_hooks = my_view_hooks_t(self)

    def OnRefresh(self):
        self.Clear()
        saved_nodes = list()
        for pair in self.pairs:
            output_node = None
            input_node = None
            for saved_node in saved_nodes:
                if pair[0] == saved_node[0]:
                    output_node = saved_node[1]
                if pair[1] == saved_node[0]:
                    input_node = saved_node[1]
            if output_node is None:
                output_node = self.AddNode((pair[0], self.color))
                saved_nodes.append((pair[0], output_node))
            if pair[0] == pair[1]:
                # handle the reflexive case, e.g. (x, x)
                input_node = output_node
            if input_node is None:
                input_node = self.AddNode((pair[1], self.color))
                saved_nodes.append((pair[1], input_node))
            self.AddEdge(output_node, input_node)
        return True

    def OnGetText(self, node_id):
        return self[node_id]

    def OnPopup(self, form, popup_handle):
        # graph closer
        actname = f'graph_closer:{self.title}'
        desc = ida_kernwin.action_desc_t(actname, f'Close: {self.title}',
                                         GraphCloser(self))
        ida_kernwin.attach_dynamic_action_to_popup(form, popup_handle, desc)

        # color changer
        actname = f'color_changer:{self.title}'
        desc = ida_kernwin.action_desc_t(actname,
                                         f'Change colors: {self.title}',
                                         ColorChanger(self))
        ida_kernwin.attach_dynamic_action_to_popup(form, popup_handle, desc)

        # selection printer
        actname = f'selection_printer:{self.title}'
        desc = ida_kernwin.action_desc_t(actname,
                                         f'Print selection: {self.title}',
                                         SelectionPrinter(self))
        ida_kernwin.attach_dynamic_action_to_popup(form, popup_handle, desc)

    def _get_all_pairs(self):
        pairs = list()
        for mod in self.dep_json:
            for ub_mod in mod['used_by']:
                pairs.append((mod['module_name'], ub_mod))
        return pairs


def run(json_file):
    global DEP_GRAPH
    if DEP_GRAPH:
        DEP_GRAPH.Close()
    try:
        with open(json_file, 'r') as f:
            res_json = json.load(f)
        dep_json = get_dep_json(res_json)
        g = DependencyGraph(dep_json)
        DEP_GRAPH = g
        if g.Show():
            return g
    except Exception as e:
        print(f'[{NAME} error] {repr(e)}')
    return False


if __name__ == '__main__':
    pass
