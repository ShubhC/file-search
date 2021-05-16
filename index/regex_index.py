from index.search_index import SearchIndex
from index.index_name import SearchIndexName
from file_store import FileStore
from typing import List
from file import File
import re

class RegexIndex(SearchIndex):
    def __init__(self, file_store: FileStore) -> None:
        index_name = SearchIndexName.RegexIndex
        super().__init__(index_name)
        self._files_as_list = file_store.all_files_as_list

    def append(self, items: list):
        pass

    def search(self, query: str, **kwargs) -> List[File]:
        regex_pattern = re.compile(query)
        matched_files = []
        for file in self._files_as_list: 
            if regex_pattern.search(file.file_path):
                matched_files.append(file)
        return matched_files
