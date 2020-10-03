#!/usr/bin/python3

###############################################################################
#
# A quick and dirty backup script for backing up minecraft worlds
# by Alex Oberhofer
#
###############################################################################
import os
import sys
import zipfile
import time
import getopt
import shutil
from datetime import datetime
from pathlib import Path


dateTimeObj = datetime.now()
datestring = dateTimeObj.strftime("%b%d%Y%H%M")
filestring = "world-"+ datestring

#########################
# function definitions
#########################

#TODO: validate world is in the path provided
#TODO: give backup filepath

def validateArgs():
    if len(sys.argv) != 2 :
        print("Usage: python3 backup-world.py </path/to/world/>")
        exit()
    print(PATH_TO_WORLD)
    

    # validate world folder path exists
    if not os.path.exists(PATH_TO_WORLD):
       print("###############################################################################")
       print("# INVALID WORLD PATH!!! : " + PATH_TO_WORLD)
       print("###############################################################################")
       exit()

    

def openBanner():
    print("###############################################################################")
    print("# Creating backup : " + filestring)
    print("###############################################################################")

def closeBanner():
    print("###############################################################################")
    print("# Backup : " + filestring + " created succesfully! ")
    print("###############################################################################")


#########################
# the script part
#########################

PATH_TO_WORLD = sys.argv[1]

validateArgs()

openBanner()

zippath = Path(PATH_TO_WORLD)

shutil.make_archive(filestring, 'zip', zippath)

closeBanner()

