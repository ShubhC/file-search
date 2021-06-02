#import psutil
import sys
from pathlib import Path
from typing import List, Dict
from file import File

def get_all_storage_devices():
    #p = r'C:\Users\Administrator\Desktop\practice'
    p = r'S:\anstrig\AnswersTriggering\private\xapnext\AnswersTriggering'
    #p = 'C:\\'
    return [Path(p)]

def get_all_path_in_dir(dir) -> List[Path]:
    
    # get all files and subdirs in dir
    path = Path(dir).glob('**/*')
    
    pathlib_files_in_dir = []
    for resource in path:
        try:
            pathlib_files_in_dir.append(resource)
        except:
            print('Got exception for file: {0}'.format(resource))
            continue
    return pathlib_files_in_dir

def get_all_path_on_device() -> List[Path]:
    storage_devices = get_all_storage_devices()
    all_path = []
    for storage_device in storage_devices:
        storage_device_path = get_all_path_in_dir(storage_device)
        all_path += storage_device_path

    return all_path

def get_files_by_path(files: List[File]) -> Dict[str, File]:
    files_by_path = dict()
    for file in files:
        file_path = file.file_path
        if file_path in files_by_path:
            files_by_path[file_path].append(file)
        else:
            files_by_path[file_path] = [file]
    return files_by_path

def get_common_files(files_A: List[File],
                     files_B: List[File]) -> List[File]:
    files_by_path_A = get_files_by_path(files_A)
    files_by_path_B = get_files_by_path(files_B)
    files_path_A = files_by_path_A.keys()
    files_path_B = files_by_path_B.keys()
    common_file_path = files_path_A & files_path_B
    common_file_names = [files_by_path_A[file_path] for file_path in common_file_path] + \
                        [files_by_path_B[file_path] for file_path in common_file_path]
    return common_file_names
