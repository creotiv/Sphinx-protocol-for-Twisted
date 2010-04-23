# -* coding: utf-8 -*-
from twisted.internet import reactor
from lib.server.twisted_sphinx import Sphinx
from twisted.internet.defer import inlineCallbacks

   
from twisted.internet import protocol

from pprint import pprint

@defer.inlineCallbacks
def main():
    clientCreator = protocol.ClientCreator(reactor, Sphinx)
    conn = yield clientCreator.connectTCP('127.0.0.1',9312)
    
    res = yield conn.Query('hello')
    pprint(res)

main()

reactor.run()
