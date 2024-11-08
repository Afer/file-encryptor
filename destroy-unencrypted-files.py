import subprocess
import time
import os
from os.path import isfile

#Set root path here
cryptRoot = "./decrypted/"

#subprocess.check_call('rm -r ' + cryptRoot + 'node_modules', shell=True)

dirs = os.listdir(cryptRoot)

def recursiveShred(dir):
    print ("starting relative dir " + dir)

    dirs = os.listdir(cryptRoot + dir)

    funcRoot = cryptRoot + dir

    for file in dirs:
        fullPath = funcRoot + file

        if not isfile(fullPath):
            recursiveShred(dir + file + "/")
            continue

        subprocess.check_call('shred -n 1 -u "' + fullPath + '"' , shell=True)
    
    print ("Finished dir " + dir)

recursiveShred("")
subprocess.check_call('rm -r *', shell=True, cwd=cryptRoot)