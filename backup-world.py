#!/usr/bin/env python

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
from datetime import datetime




PATH_TO_WORLD = "F:\\Minecraft\\world\\"

dateTimeObj = datetime.now()
dateObj = dateTimeObj.date()
datestring = dateObj.strftime("%b%d%Y")

filestring = "world-"+ datestring + ".zip"

#########################
# function definitions
#########################

#TODO: validate world is in the path provided
#TODO: give backup filepath

def validateArgs():
    if len(sys.argv) != 2 :
        print("Usage: python3 backup-world.py </path/to/world/>")
        exit()
    
    PATH_TO_WORLD = sys.argv[1:]
    print(PATH_TO_WORLD)
    exit()

    # validate backup folder exists
    #if not os.path.exists(PATH_TO_WORLD):
     #   print("###############################################################################")
      #  print("# INVALID WORLD PATH!!! : " + PATH_TO_WORLD)
       # print("###############################################################################")
        #exit()

    

def openBanner():
    print("###############################################################################")
    print("# Creating backup : " + filestring)
    print("###############################################################################")

def closeBanner():
    print("###############################################################################")
    print("# Backup : " + filestring + " created succesfully! ")
    print("###############################################################################")

def zipdir(path, ziph):
    # ziph is zipfile handle
    for root, dirs, files in os.walk(path):
        for file in files:
            ziph.write(os.path.join(root, file))


#########################
# the script part
#########################

#validateArgs()

openBanner()

zipf = zipfile.ZipFile(filestring, 'w', zipfile.ZIP_DEFLATED)

zipdir(PATH_TO_WORLD, zipf)

zipf.close()

closeBanner()

