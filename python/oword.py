import os
import re
import sys
import linuxcnc
import emccanon
import atc_remap

from linuxcnc import ini

s = linuxcnc.stat()
c = linuxcnc.command()
# this would be defined in the oword module
def load_tool_changer_ui(self, *args):
    table = atc_remap._atc_list_model(True)

    for pnum, tnum in enumerate(table, start=0):
        if(pnum > 0 and tnum != None):
            self.execute('(DEBUG, EVAL[vcp.getWidget{"dynatc"}.store_tool{'+ str(pnum) +', '+ str(tnum) +'}])')