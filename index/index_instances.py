from enum import Enum
from dataclasses import dataclass
from index.multi_word_lookup_index import MultiWordLookupIndex
from os import popen
from file_store import PathStore
from index.lookup_index import LookupIndex as LookupIndexClass
from index.regex_index import RegexIndex as RegexIndexClass
from index.index_name import SearchIndexName

class SearchIndexRepo:

    def __init__(self, path_store: PathStore) -> None:
        self._lookup_index = LookupIndexClass(path_store)
        self._regex_index = RegexIndexClass(path_store)
        self._multi_word_lookup_index = MultiWordLookupIndex(path_store)

    @property
    def lookup_index(self):
        return self._lookup_index

    @property
    def regex_index(self):
        return self._regex_index

    @property
    def multi_word_lookup_index(self):
        return self._multi_word_lookup_index