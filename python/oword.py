#!/usr/bin/env python
# -*- coding: utf-8 -*-
import linuxcnc
s = linuxcnc.stat()
c = linuxcnc.command()

# this would be defined in the oword module
def toolread(self, *args):
    s.poll()
    c.load_tool_table()
    # to find the loaded tool information it is in tool table index 0
    if s.tool_table[0].id != 0: # a tool is loaded
        print s.tool_table[0]
    else:
        print "no tool loaded"