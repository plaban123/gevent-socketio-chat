from socketio.namespace import BaseNamespace
from socketio.sdjango import namespace

@namespace('/echo')
class EchoNamespace(BaseNamespace):
    def on_msg(self, msg):
        print "ADF"
        pkt = {
            'type': 'event',
            'name': 'msg',
            'args': 'Someone said: {0}'.format(msg),
            'endpoint': self.ns_name
        }
        for sessid, socket in self.socket.server.sockets.itertimes():
            socket.send_packet(pkt)
