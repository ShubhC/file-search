
from typing import List
from pathlib import Path
import subprocess

class File:
    #(st_mode=33206, st_ino=281474976711694, st_dev=388544000, st_nlink=1, st_uid=0, st_gid=0, 
    # st_size=297, st_atime=1620803957, st_mtime=1620801881, st_ctime=1620801726)
    def __init__(self, pathlib_file : Path) -> None:
        self._pathlib_file = pathlib_file
        self._file_stat = self._pathlib_file.stat()
        self._file_name = self._pathlib_file.name
        self._file_name_stem = self._pathlib_file.stem
        self._file_path = str(self._pathlib_file)

    @property
    def file_path(self) -> str:
        """ 
            Returns file path. 
            e.g. C:/User/abc/test.txt
        """
        return self._file_path

    @property
    def file_name(self) -> str:
        """
            For file /home/test.txt, returns test.txt
        """
        return self._file_name

    @property
    def file_name_stem(self) -> str:
        """ 
            For file /home/test.txt, returns test
        """
        return self._file_name_stem

    @property
    def file(self) -> Path:
        return self._pathlib_file
    
    @property
    def created_date(self) -> str:
        return self._file_stat.st_ctime

    @property
    def modified_date(self) -> str:
        return self._file_stat.st_mtime
    
    @property
    def size(self) -> int:
        file_size_bytes = self._file_stat.st_size
        return file_size_bytes
