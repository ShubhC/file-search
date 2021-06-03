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
        query_tokens = list(set(query.split(split_token)))
        query_tokens = [query_token.lower() for query_token in query_tokens if query_token]
        return query_tokens

    def __init__(self, whoosh_adapter: WhooshAdapter) -> None:
        self._index_name = SearchIndexName.MultiWordLookupIndex
        super().__init__(self._index_name)
        self._whoosh_adapter = whoosh_adapter  

    def search(self, query: str, **kwargs) -> List[Path]:
        query_tokens = self._break_tokens(query)
        return self._whoosh_adapter.multi_word_contains_or_wildcard_search(query_tokens)
