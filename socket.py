#!/usr/bin/env python

import socket

def main():
    ports = [21,23,22]
    ips = "192.168.195."
    for octet in range(0,255):
        for port in ports:
            ip = ips + str(octet)
            #print("[*] Testing port %s at IP %s") % (port, ip)
            try:
                socket.setdefaulttimeout(1)
                s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
                s.connect((ip,port))
                output = s.recv(1024)
                print("[+] The banner: {0} for IP: {1} at Port: {2}".format(output,ip,port) )
            except:
                print("[-] Failed to Connect to {0}:{1}".format(ip, port) )
            finally:
                s.close()


if __name__ == "__main__":
    main()