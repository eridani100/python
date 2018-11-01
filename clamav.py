#!/usr/local/bin/env python

import pyclamd


"""
Client for clamav running on the host
"""

class ClamavScan:

    def __init__(self, file_to_scan):
        self.file_to_scan = file_to_scan

        # check if clamav is reachable
        try:
            self.cd = pyclamd.ClamdUnixSocket()
            self.cd.ping()
        except pyclamd.ConnectionError:
            # if failed,  test for network socket
            self.cd = pyclamd.ClamdNetworkSocket()
            try:
                self.cd.ping()
            except pyclamd.ConnectionError:
                raise ValueError("could not connect to clamd server either by unix or network socket")

        print(self.cd.version().split()[0])
      #  print(self.cd.reload())
        print(self.cd.stats().split()[0])



    def scanfile(self):
        return self.cd.scan_file(self.file_to_scan)


scan = ClamavScan("/Users/menago/.malwaresample/samplefilewithvirus")
print(scan.scanfile())


#cd = pyclamd.ClamdAgnostic()
#cd.ping()
