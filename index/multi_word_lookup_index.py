from pathlib import Path
from adapter.whoosh_adapter import WhooshAdapter
from index.search_index import SearchIndex
from index.index_name import SearchIndexName
from index.lookup_index import LookupIndex
from typing import List
from file import File

class MultiWordLookupIndex(SearchIndex):

    def _break_tokens(self, query: str) -> List[str]:
        split_token = ' '
        query_tokens = query.split(split_token)
        strip_stars = lambda x : x.replace('*','')
        query_tokens = [strip_stars(query_token) for query_token in query_tokens]
        query_tokens = [query_token for query_token in query_tokens if query_token]
        return query_tokens

    def __init__(self, whoosh_adapter: WhooshAdapter) -> None:
        self._index_name = SearchIndexName.MultiWordLookupIndex
        super().__init__(self._index_name)
        self._whoosh_adapter = whoosh_adapter  

    def search(self, query: str, **kwargs) -> List[Path]:
        