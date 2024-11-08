import der
from cryptography.fernet import Fernet
import subprocess
import os
import sys
from os.path import isfile

#set root paths here
cryptSource = './decrypted/'
cryptDest = './encrypted/'

# set ignored folder names here. Only works with folder names
ignorePaths = ['test1', 'test2']

hasFiles = False
dirs = os.listdir(cryptSource)
for any in dirs:
    hasFiles = True
    break

if not hasFiles:
    input("No files to encrypt, press Enter to continue.")
    sys.exit(-1)

key = der.deriveKey()
fernet = Fernet(key)

def recursiveEncrypt(dir):
    print ("starting relative dir " + dir)

    dirs = os.listdir(cryptSource + dir)

    funcRoot = cryptSource + dir

    for file in dirs:
        fullPath = funcRoot + file

        if file in ignorePaths:
            continue

        if not isfile(fullPath):
            recursiveEncrypt(dir + file + "/")
            continue

        with open(fullPath, 'rb') as file:
            original = file.read()
            
        encrypted = fernet.encrypt(original)

        newFile = file.name.split("/")
        newFile = newFile[len(newFile)-1]
        newFile = cryptDest + dir + newFile + ".txt"

        os.makedirs(os.path.dirname(newFile), exist_ok=True)

        with open(newFile, 'wb') as encrypted_file:
            encrypted_file.write(encrypted)

    
    print ("Finished dir " + dir)


subprocess.check_call('rm -rf *', shell=True, cwd=cryptDest)

recursiveEncrypt("")