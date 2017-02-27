#!/usr/bin/python
#
# We use the subprocess module to run other programs in python;
# We use the os module to set the working directoy

import subprocess
import os


# Get current working directory (cwd)
print os.getcwd()

# Change to another directory
os.chdir("/tmp")

# Execute another program
# The subprocess module captures output from the subprocess call
x = subprocess.call(["ls","-l","-a","-h"])
print x
