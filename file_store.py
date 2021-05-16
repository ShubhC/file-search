from dataclasses import dataclass, field
from utils import file_utils
from typing import List
from file import File

class FileStore:

    def __init__(self) -> None:
        self._all_files_as_list = file_utils.get_all_files_on_device()

    @property
    def all_files_as_list(self) -> List[File]:
        return self._all_files_as_list

    def update_latest(self, additions : List[File], deletions: List[File]):
        """
            Updates existing file_store
            TODO: add implementation
        """
        pass