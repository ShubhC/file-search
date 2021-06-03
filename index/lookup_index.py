from pathlib import Path
from adapter.whoosh_adapter import WhooshAdapter
from index.search_index import SearchIndex
from index.index_name import SearchIndexName
from typing import List

class LookupIndex(SearchIndex):
    
    def __init__(self, whoosh_adapter: WhooshAdapter) -> None:
        self._index_name = SearchIndexName.LookupIndex
        super().__init__(self._index_name)
        self._whoosh_adapter = whoosh_adapter

    def search(self, query: str, **kwargs) -> List[Path]:
        query = query.lower()
        return self._whoosh_adapter.contains_or_wildcard_search(query)
        