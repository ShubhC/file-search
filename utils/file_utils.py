from utils import constants
import subprocess
import sys
from pathlib import Path

def get_all_storage_devices():
    # On windows
    # Get the fixed drives
    # wmic logicaldisk get name,description
    if constants.WindowsPlatformName in sys.platform:
        drivelist = subprocess.Popen('wmic logicaldisk get name,description', shell=True, stdout=subprocess.PIPE)
        drivelisto, _ = drivelist.communicate()
        driveLines = drivelisto.split('\n')
        return driveLines

    """
        if 'linux' in sys.platform:
            listdrives=subprocess.Popen('mount', shell=True, stdout=subprocess.PIPE)
            listdrivesout, _ = listdrives.communicate()
            for idx,drive in enumerate(filter(None,listdrivesout)):
                listdrivesout[idx] = drive.split()[2]
            return listdrivesout
    """
    raise NotImplementedError("Only windows is supported.")


def get_all_files_in_dir(dir):    
    path = Path(dir).glob('**/*')
    files_in_dir = [resource for resource in path if resource.is_file()]
    return files_in_dir

def get_all_files_on_device():
    storage_devices = get_all_storage_devices()
    all_files = []
    for storage_device in storage_devices:
        storage_device_files = get_all_files_in_dir(storage_device)
        all_files += storage_device_files
        
    return all_files