# Importar as bibliotecas
from pox.core import core
import pox.openflow.libopenflow_01 as of
from pox.lib.revent import *
from pox.lib.addresses import EthAddr, IPAddr
from pox.lib.util import dpidToStr

log = core.getLogger()  # logging

class aula2ex1 (EventMixin):
    def __init__(self):
        self.listenTo(core.openflow)

    def _handle_ConnectionUp(self, event):
        log.debug("Connection UP from %s", event.dpid)

    def _handle_PacketIn(self, event):
        packet = event.parsed
        # Encaminhamento dos pacotes
        msg = of.ofp_flow_mod()
        msg.match.in_port = event.port
        msg.match.dl_src = packet.src
        msg.match.dl_dst = packet.dst

        out_port = 1 if event.port != 1 else 2  # Alternar portas para exemplo
        msg.actions.append(of.ofp_action_output(port=out_port))

        event.connection.send(msg)
        log.debug("Forward packet sw=%s in_port=%s src=%s dst=%s out_port=%s" \
                  % (event.dpid, event.port, packet.src, packet.dst, out_port))


def launch():
    core.openflow.miss_send_len = 1024
    core.registerNew(aula2ex1)

