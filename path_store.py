from pathlib import Path
from utils import path_utils
from typing import List

class PathStore:

    def __init__(self, indexing_done: bool) -> None:
        if indexing_done:
            return
        self._all_path_as_list = path_utils.get_all_path_on_device()
        
    @property
    def all_path_as_list(self) -> List[Path]:
        return self._all_path_as_list

    def update(self, additions : List[Path], deletions: List[Path]):
        """
            Updates existing file_store
            TODO: add implementation
        """
        pass