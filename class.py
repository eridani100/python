#!/usr/bin/python

import time


class TcpServer:
    def __init__(self, address, port):
        self.address = address
        self.port = port
        self.running = False

    def start(self):
        print "Server started on address %s:%s" % (self.address, self.port)
        self.running = True

    def isrunning(self):
        if self.running:
            return True
        else:
            return False


server1 = TcpServer("localhost", 4000)
server2 = TcpServer("10.0.0.30", 5001)

while True:
    if not server1.isrunning():
        server1.start()
        print "Start : %s" % time.ctime()

    if not server2.isrunning():
        server2.start()
        print "Start : %s" % time.ctime()

    time.sleep(5)
    print "Checking status : %s" % time.ctime()
