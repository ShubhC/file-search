from index.search_index import SearchIndex
from index.index_instances import SearchIndexName
from typing import List
from file_store import File

class LookupIndex(SearchIndex):
    
    def __init__(self) -> None:
        self._index_name = SearchIndexName.LookupIndex
        SearchIndex.__init__(self, self._index_name)

        self._dictionary = dict()        
                
    def append(self, items: List[File]):
        for item in items:
            item_file_name_stem = item.file_name_stem
            if item_file_name_stem in self._dictionary:
                self._dictionary[item_file_name_stem].append(item)
            else:
                self._dictionary[item_file_name_stem] = [item]

    def search(self, query: str, **kwargs) -> List[File]:
        index_search_results = self._dictionary[query]
        return index_search_results
