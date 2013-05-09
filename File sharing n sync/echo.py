import os
import optparse

from twisted.internet import reactor, protocol, stdio, defer
from twisted.protocols import basic



class Echo(basic.LineReceiver):
    
    def connectionMade(self):
        self.sendLine('Welcome\n')
        self.sendLine('Type help for list of all the available commands\n')
        self.sendLine('ENDMSG\n')
    
    
    def lineReceived(self, line):
        """
        As soon as any data is received, write it back.
        """
        self.sendLine('reply '+line)


def main():
    f = protocol.Factory()
    f.protocol = Echo
    reactor.listenTCP(8000, f)
    reactor.run()

if __name__ == '__main__':
    main()