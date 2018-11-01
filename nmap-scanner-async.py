#!/usr/bin/python


import nmap
import time

nma=nmap.PortScannerAsync()

def callback_result(host, scan_result):
	print '------------------'
	print host, scan_result
 
nma.scan(hosts='10.0.0.0/24', arguments='-sP', callback=callback_result)
while nma.still_scanning():
	print("Waiting >>>")
	nma.wait(2)   # you can do whatever you want but I choose to wait after the end of the scan

#nm = nmap.PortScannerYield()
#for progressive_result in nm.scan('127.0.0.1/24', '22-25'):
#	print(progressive_result)


