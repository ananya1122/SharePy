import os
import optparse

from twisted.internet import reactor, protocol, stdio, defer
from twisted.protocols import basic
from twisted.internet.protocol import ClientFactory

import re   


            
            
class InputForwarder(protocol.Protocol):
    def __init__(self):
        print 'welcome'
        self.output = None 
        self.normalizeNewlines = False
        self.sender = None
    def dataReceived(self, line):
        if self.output:
             
            #self.sender.transport.write(line)
            self.sender.sendLine(line)
        
    
        
        
class LOL(object):  
    def ___init___(self,mssg,point): 
        print mssg
        self.output = None 
        self.normalizeNewlines = False
    '''    
    def lineReceived(self, line):
        print 'what'
        if self.normalizeNewlines:  
            data = re.sub(r"(\r\n\n)", "\r\n", data)  
        if self.output:
            self.output.write(data)
     '''     

class StdioProxyProtocol(basic.LineReceiver):
    
    def __init__(self):
       
        #self.mayank = InputForwarder()
        print 'hey'
    
    
    def connectionMade(self):
        inputForwarder = InputForwarder()  
        inputForwarder.output = self.transport  
        inputForwarder.normalizeNewlines = True 
        inputForwarder.sender = self 
        stdioWrapper = stdio.StandardIO(inputForwarder)  
       # self.output = stdioWrapper
        
        
        print 'done'
        print "Connected to server. Press ctrl-C to close connection."
        
        
    def lineReceived(self, line):
        
        print ' 999 '+line
        
        
  
class StdioProxyFactory(protocol.ClientFactory):
    protocol = StdioProxyProtocol 
    def clientConnectionLost(self, transport, reason):
        reactor.stop()
    def clientConnectionFailed(self, transport, reason): 
        print reason.getErrorMessage()
        reactor.stop()     
        


if __name__ == '__main__':
    reactor.connectTCP('localhost', 8000, StdioProxyFactory())  
    reactor.run() 
  
    