from msilib.schema import Error
import script_config as cfg

class SourceAction:
    "identifying and executing source action"
    def __init__(self):
        pass
    

try:
    cfg.read_start_folder()
    # if source action = dft -> execute dft action
    if(cfg.source_action==cfg.build_dft):
        print("Desired source action = build_dft")
    else:
        print("Unknown source action. Aborting...")
        exit()


except cfg.ConfigError as err:
    print("Fatal error: cannot proceed")
    print (err)
    print("Forced stop...")
    exit()

print("hehe")