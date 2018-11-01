#!/usr/bin/python


from threading import Thread
import time


def pingSweep(name,address):

	for host in nm.all_hosts():
		print('----------------------------------------------------')
		print('Host  : %s (%s)' % (host, nm[host].hostname()))
		print('State : %s' % nm[host].state())
		for proto in nm[host].all_protocols():
			print('----------')
			print('Protocol : %s' % proto)
			lport = nm[host][proto].keys()
			lport.sort()

		for port in lport:
			print ('port : %s\tstate : %s' % (port, nm[host][proto][port]['state']))


#def timer(name ,delay ,repeat):
#    print "Timer: " + name + "Started"
#    while repeat > 0:
#        time.sleep(delay)
#        print name +": " + str(time.ctime(time.time()))
#        repeat -= 1
#    print "Timer: " + name + "Completed"


def Main():
    t1 = Thread(target=scanner, args=("Thread1", '10.0.0.1-3', '80,22,110,21,443'))
    t2 = Thread(target=scanner, args=("Thread2", '10.0.0.173', '22,80'))
    t1.start()
    print "Thread %s started\n" % (t1.getName())
    t2.start()
    print "Thread %s started\n" % (t2.getName())

    print "Main Completed. To juz se leci tera samo..."


if __name__ == '__main__':
    Main()
