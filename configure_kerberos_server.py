#!/usr/bin/python
# This script is intended to work on RHEL7 

import os
import sys
import platform
import math
import os.path
from os import path

# initializing the packages that needs to be installed 
server_packages ="krb5-server krb5-workstation pam_krb5"

# Defining some helper functions 

# Check OS 
def check_os():
    (os,version,release) = platform.linux_distribution()
    if 'Red Hat' in os and math.floor(float(version)) == 7.0:
        print("\033[1;41m OS is %s %s \033[1;m"%(os,version))
    else:
        print("\033[1;41m OS is %s %f, We need Red Hat 7, exiting... \033[1;m"%(os,float(version)))
        sys.exit()

# Install Package
def install_func(package):
    print("\n\033[1;41m Installing %s\033[1;m"%package)
    os.system("yum install -y %s" %(package))


### Main code starts here 

# Check OS
check_os()

# Install kerberos server packages
install_func(server_packages)



