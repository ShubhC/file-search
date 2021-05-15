from dataclasses import dataclass, field
from utils import file_utils
from typing import List
from file import File

class FileStore:
    all_files_as_list : List[File] = file_utils.get_all_files_on_device()