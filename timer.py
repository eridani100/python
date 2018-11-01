#!/usr/bin/python

from threading import Thread
import time

def timer(name ,delay ,repeat):
    print "Timer: " + name + "Started"
    while repeat > 0:
        time.sleep(delay)
        print name +": " + str(time.ctime(time.time()))
        repeat -= 1
    print "Timer: " + name + "Completed"


def Main():
    t1 = Thread(target=timer, args=("Timer1", 5, 10))
    t2 = Thread(target=timer, args=("Timer2", 8, 16))
    t1.start()
    print "Thread %s started\n" % (t1.getName())
    t2.start()
    print "Thread %s started\n" % (t2.getName())

    print "Main Completed. To juz se leci tera samo..."


if __name__ == '__main__':
    Main()
