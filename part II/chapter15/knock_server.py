# 15.3.6 twisted

from twisted.internet import protocol, reactor

class Knock(protocol.Protocol):
    def dataReceived(self, data):
        print('Client:', data)
        if data.startswith("Knock knock"):
            response = "Who's there?"
        else:
            response = data + " who?"
            print('Server:', response)
            self.transport.write(response)

class KnockFactory(protocol.Factory):
    def buildProtocol(self, addr):
        return Knock()

if __name__ == '__main__':
    reactor.listenTCP(8000, KnockFactory())
    reactor.run()
