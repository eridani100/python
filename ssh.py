#!/usr//bin/env python3

#  ssh in Python

import paramiko

hostname = '192.168.1.224'
port = 22
username = 'maniek'
password = ''

if __name__ == "__main__":
    paramiko.util.log_to_file('paramiko.log')
    s = paramiko.SSHClient()
    s.load_system_host_keys()
    try:
        s.connect(hostname, port, username, password,timeout=5)
        stdin, stdout, stderr = s.exec_command('ifconfig')
        print(stdout.read())
        s.close()
    
    except Exception as e:
        print ('Error occured: ',e)


