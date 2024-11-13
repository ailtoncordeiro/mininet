import pox.openflow.libopenflow_01 as of
from pox.core import core

log = core.getLogger()

def launch():
    def _handle_ConnectionUp(event):
        msg = of.ofp_flow_mod()
        msg.match.in_port = 1
        msg.actions.append(of.ofp_action_output(port=3))
        event.connection.send(msg)

        msg = of.ofp_flow_mod()
        msg.match.in_port = 3
        msg.actions.append(of.ofp_action_output(port=1))
        event.connection.send(msg)
        log.info("Flow rules installed on %s", event.connection)

    core.openflow.addListenerByName("ConnectionUp", _handle_ConnectionUp)
    log.info("Custom app launched")
