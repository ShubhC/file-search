from adapter.whoosh_adapter import WhooshAdapter
from index.search_index import SearchIndex
from index.index_name import SearchIndexName
from typing import List
from file import File
import re

class RegexIndex(SearchIndex):
    def __init__(self, whoosh_adapter: WhooshAdapter) -> None:
        index_name = SearchIndexName.RegexIndex
        super().__init__(index_name)
        self._whoosh_adapter = whoosh_adapter

    def search(self, query: str, **kwargs) -> List[File]:
        return self._whoosh_adapter.regex_search(query)