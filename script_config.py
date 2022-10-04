#this is config file for script docu_links.py

import preprocessing
from os.path import exists
from os.path import isdir

print ("Loading configuration...")

start_folder = r'c:\Users\poczt\Dropbox\Dokumenty\KSIAZKI_EBOOKI\prawo-gumiakow.pdf' #write starting folder here, r' = means raw string

class ConfigError(Exception):
    pass

def read_start_folder():
    print ("read_start_folder()")
    
    #Check if start_folder is correct Path
    if(exists(start_folder)):
        print("Success: resource: "+start_folder+" exists")
        print("Continuing...")
    else:
        raise ConfigError("Resource: "+start_folder+" does not exists")
    
    #Check if start_folder is directory
    if(isdir(start_folder)):
        print("Another Success: resource: +"+start_folder+" is directory")
    else:
        raise ConfigError("Resource: "+start_folder+" is not directory")

    print("Successfully located start_folder")

