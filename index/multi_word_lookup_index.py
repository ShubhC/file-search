from index.search_index import SearchIndex
from index.index_name import SearchIndexName
from index.lookup_index import LookupIndex
from typing import List
from file import File

class MultiWordLookup(LookupIndex):

    def _break_tokens(self, query: str) -> List[str]:
        split_token = ' '
        query_tokens = query.split(split_token)
        strip_stars = lambda x : x.replace('*','')
        query_tokens = [strip_stars(query_token) for query_token in query_tokens]
        query_tokens = [query_token for query_token in query_tokens if query_token]
        return query_tokens

    def __init__(self) -> None:
        index_name = SearchIndexName.MultiWordLookupIndex
        super().__init__(index_name)

    def append(self, items: list) -> None:
        return super().append(items)

    def search(self, query: str, **kwargs) -> List[File]:
        query_tokens = self._break_tokens(query)
        return super().search(query, **kwargs)
