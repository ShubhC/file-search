from file_store import FileStore
from utils import file_utils
from index.search_index import SearchIndex
from index.index_name import SearchIndexName
from index.lookup_index import LookupIndex
from typing import List
from file import File

class MultiWordLookupIndex(LookupIndex):

    def _break_tokens(self, query: str) -> List[str]:
        split_token = ' '
        query_tokens = query.split(split_token)
        strip_stars = lambda x : x.replace('*','')
        query_tokens = [strip_stars(query_token) for query_token in query_tokens]
        query_tokens = [query_token for query_token in query_tokens if query_token]
        return query_tokens

    def __init__(self, file_store: FileStore) -> None:
        super().__init__(file_store)
        self._index_name = SearchIndexName.MultiWordLookupIndex  

    def search(self, query: str, **kwargs) -> List[File]:
        multi_word_tokens = self._break_tokens(query)
        multi_word_lookup_files = []
        first_iteration = True
        for token in multi_word_tokens:
            # lookup search
            lookup_searched_files = super().search(token)

            if first_iteration:
                first_iteration = False
                multi_word_lookup_files = lookup_searched_files
                continue

            multi_word_lookup_files = file_utils.get_common_files(multi_word_lookup_files, 
                                                                  lookup_searched_files)
            if not multi_word_lookup_files:
                break

        return multi_word_lookup_files