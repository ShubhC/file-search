from adapter import whoosh_adapter
from enum import Enum
from dataclasses import dataclass
from index.multi_word_lookup_index import MultiWordLookupIndex
from index.lookup_index import LookupIndex as LookupIndexClass
from index.regex_index import RegexIndex as RegexIndexClass
from index.index_name import SearchIndexName
from adapter.whoosh_adapter import WhooshAdapter

class SearchIndexRepo:

    def __init__(self, whoosh_adapter: WhooshAdapter) -> None:
        self._lookup_index = LookupIndexClass(whoosh_adapter)
        self._regex_index = RegexIndexClass(whoosh_adapter)
        self._multi_word_lookup_index = MultiWordLookupIndex(whoosh_adapter)

    @property
    def lookup_index(self) -> LookupIndexClass:
        return self._lookup_index

    @property
    def regex_index(self) -> RegexIndexClass:
        return self._regex_index

    @property
    def multi_word_lookup_index(self) -> MultiWordLookupIndex:
        return self._multi_word_lookup_index