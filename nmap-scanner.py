#!/usr/bin/python

"""Performs nmap network scanning on specified node"""

__AUTHOR__ = 'Maniek'
__VERSION__ = "0.10 November 2018"

"""
"""

import nmap
import time

nm = nmap.PortScanner()
nm.scan('192.168.1.1', '21,23,80,443,445,8080')
print("Poszlo\n")

print(nm.scaninfo())
# print()

# nm.listscan()
for host in nm.all_hosts():
    print('----------------------------------------------------')
    print('Host : %s (%s)' % (host, nm[host].hostname()))
    print('State : %s' % nm[host].state())
    for proto in nm[host].all_protocols():
        print('----------')
        print('Protocol : %s' % proto)
        lport = nm[host][proto].keys()
        lport.sort()

    for port in lport:
        print('port : %s\tstate : %s' % (port, nm[host][proto][port]['state']))
