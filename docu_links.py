from msilib.schema import Error
import script_config as cfg
import os

start_folder =""

class SourceActionDFT:
    "identifying and executing source action"
    source_dir =""
    def __init__(self,start_folder,source_action):
        source_dir1 = start_folder
        print("Start working with directory:"+start_folder)
    
    def read_folder(self):
        print("read_folder()")
        with os.scandir(self.source_dir1) as entries:
           pass

try:
    start_folder = cfg.read_start_folder()
    # if source action = dft -> execute dft action
    if(cfg.source_action==cfg.build_dft):
        print("Desired source action = build_dft")
        item = SourceActionDFT(start_folder,cfg.source_action)
        item.read_folder()
    else:
        print("Unknown source action. Aborting...")
        exit()


except cfg.ConfigError as err:
    print("Fatal error: cannot proceed")
    print (err)
    print("Forced stop...")
    exit()

#some playing with changing file from github account - only educational purposes
#from now on i work on this project having it on my gitbug - another educational comment
#just nearly empty comment
print("Finish script.")
