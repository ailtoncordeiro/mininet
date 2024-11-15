from pox.pox.core import core
import pox.pox.openflow.libopenflow_01 as of
from pox.pox.lib.revent import *

log = core.getLogger()

class myfirstapp(EventMixin):
    switches = {}

    def __init__(self):
        super().listenTo(core.openflow)

    def _handle_ConnectionUp (self, event):
        log.debug("Connection UP from %s", event.dpid)
        myfirstapp.switches[event.dpid] = event.connection

    def _handle_PacketIn (self, event):
        pass

def launch():
    core.openflow.miss_send_len = 1024
    core.registerNew(myfirstapp)
