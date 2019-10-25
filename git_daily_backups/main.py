
import os
import time

myCmd = 'git clone https://github.com/eagleinvsys-sd/sd-core-17 .'
newFld = 'F:/SD-CORE-17-BACKUPS/' + time.strftime("%m_%d_%Y_%M_%S")
os.makedirs(newFld)
os.chdir(newFld)
#os.system('git-lfs install')
os.system(myCmd)