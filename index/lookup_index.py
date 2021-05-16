from dataclasses import field
from file_store import FileStore
from index.search_index import SearchIndex
from index.index_name import SearchIndexName
from typing import List
from file import File
from utils import file_utils

class LookupIndex(SearchIndex):
    
    def __init__(self, file_store: FileStore) -> None:
        self._index_name = SearchIndexName.LookupIndex
        super().__init__(self._index_name)
        self._dictionary = dict()
        all_files = file_store.all_files_as_list
        self.append(all_files)

    def _append_entry(self, entry: str, file: File):
        if entry in self._dictionary:
            self._dictionary[entry].append(file)
            return
        self._dictionary[entry] = [file]

    def _append_file(self, file: File):
        file_name_stem = file.file_name_stem
        file_name = file.file_name
        self._append_entry(file_name_stem, file)
        self._append_entry(file_name, file)

    def append(self, files: List[File]):
        for file in files:
            self._append_file(file)

    def search(self, query: str, **kwargs) -> List[File]:
        if not (query in self._dictionary):
            return []

        index_search_results = self._dictionary[query]
        return index_search_results
