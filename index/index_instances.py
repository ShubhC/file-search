from enum import Enum
from dataclasses import dataclass
from index.multi_word_lookup_index import MultiWordLookupIndex
from os import popen
from file_store import FileStore
from index.lookup_index import LookupIndex as LookupIndexClass
from index.regex_index import RegexIndex as RegexIndexClass
from index.index_name import SearchIndexName

class SearchIndexRepo:

    def __init__(self, file_store: FileStore) -> None:
        self._lookup_index = LookupIndexClass(file_store)
        self._regex_index = RegexIndexClass(file_store)
        self._multi_word_lookup_index = MultiWordLookupIndex(file_store)

    @property
    def lookup_index(self):
        return self._lookup_index

    @property
    def regex_index(self):
        return self._regex_index

    @property
    def multi_word_lookup_index(self):
        return self._multi_word_lookup_index