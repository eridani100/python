

#!/usr/bin/env python
import sys

arguments = sys.argv

print("The number of arguments passed was: {0}".format(arguments))
i=0
for x in arguments:
    print("The {0} argument is {1}".format(i,x) )
    i+=1
#

