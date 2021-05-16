#import psutil
import sys
from pathlib import Path
from typing import List
from file import File

def get_all_storage_devices():
    p = r'C:\Users\Administrator\Desktop\practice'
    #p = 'C:\\'
    return [Path(p)]

def convert_from_pathlib_to_file(pathlib_files: List[Path]) -> List[File]:
    files = []
    for pathlib_file in pathlib_files:
        try:
            file = File(pathlib_file)
        except:
            continue
        files.append(file)
    return files

def get_all_files_in_dir(dir) -> List[File]:    
    path = Path(dir).glob('**/*')
    pathlib_files_in_dir = []
    for resource in path:
        try:
            if resource.is_file():
                pathlib_files_in_dir.append(resource)
        except:
            print('Got exception for file: {0}'.format(resource))
            continue

    files_in_dir = convert_from_pathlib_to_file(pathlib_files_in_dir)
    return files_in_dir

def get_all_files_on_device() -> List[File]:
    storage_devices = get_all_storage_devices()
    all_files = []
    for storage_device in storage_devices:
        storage_device_files = get_all_files_in_dir(storage_device)
        all_files += storage_device_files
        
    return all_files