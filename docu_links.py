from msilib.schema import Error
import script_config as cfg


print ("Starting doculinks...")


try:
    cfg.read_start_folder()
except cfg.ConfigError as err:
    print("Fatal error: cannot proceed")
    print (err)
    print("Forced stop...")
    exit()

print("hehe")