from cryptography.fernet import Fernet
import subprocess
import os
import der
from os.path import isfile

#set root paths here
cryptSource = './decrypted/'
cryptDest = './encrypted/'

key = der.deriveKey()
fernet = Fernet(key)

dirs = os.listdir(cryptSource)

def recursiveDecrypt(dir):
    print ("starting relative dir " + dir)

    dirs = os.listdir(cryptSource + dir)

    funcRoot = cryptSource + dir

    for file in dirs:
        fullPath = funcRoot + file

        if not isfile(fullPath):
            recursiveDecrypt(dir + file + "/")
            continue

        with open(fullPath, 'rb') as filer:
            encrypted = filer.read()
        
        original = fernet.decrypt(encrypted)

        newFile = file.split("/")
        newFile = newFile[len(newFile)-1]
        newFile = newFile[:-4]
        newFile = cryptDest + dir + newFile

        os.makedirs(os.path.dirname(newFile), exist_ok=True)

        with open(newFile, 'wb') as restored_file:
            restored_file.write(original)

    
    print ("Finished dir " + dir)


recursiveDecrypt("")