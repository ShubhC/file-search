import whoosh
from whoosh.query.terms import Regex
from path_store import PathStore
from pathlib import Path
from typing import List
from whoosh.fields import STORED, Schema, TEXT
from whoosh.query import Wildcard, Prefix
import os.path
from whoosh.index import create_in

class WhooshAdapter:
    
    def __init__(self, path_store: PathStore) -> None:
        self._path_store = path_store
        self._get_all_path = self._path_store.all_path_as_list
        self._whoosh_index = self._create_whoosh_index()
        self._update_index(self._get_all_path, None)
        self._file_or_dir_field_name = 'file_or_dir'
        self._path_field_name = 'path'
      
    def _create_whoosh_index(self):
        self._schema = Schema(file_or_dir=TEXT, path=STORED)
        whoosh_index_dir_name = 'index'
        if not os.path.exists(whoosh_index_dir_name):
            os.mkdir(whoosh_index_dir_name)
        whoosh_index = create_in(whoosh_index_dir_name, self._schema)
        return whoosh_index
    
    def _update_index(self, additions: List[Path], deletions: List[Path]):
        # TODO: implement deletions
        whoosh_index_writer = self._whoosh_index.writer()
        for path in additions:
            file_or_dir = path.name
            whoosh_index_writer.add_document(file_or_dir=file_or_dir, path=path)
            #print('adding {0} to index'.format(file_or_dir))
        whoosh_index_writer.commit()
    
    def _search_whoosh_query(self, whoosh_query) -> List[Path]:
        with self._whoosh_index.searcher() as searcher:
            search_results = searcher.search(whoosh_query, limit=100_000)
            search_paths = [Path(search_result[self._path_field_name]) for search_result in search_results]
            
        return search_paths
    
    def wildcard_search(self, query: str) -> List[Path]:
        whoosh_wildcard_search_query = Wildcard(self._file_or_dir_field_name, query)
        return self._search_whoosh_query(whoosh_wildcard_search_query)
        
    def regex_search(self, query: str) -> List[Path]:
        whoosh_regex_search_query = Regex(self._file_or_dir_field_name, query)
        return self._search_whoosh_query(whoosh_regex_search_query)    
        
    def _create_wildcard_search_query(self, query: str) -> Wildcard:
        if '*' in query:
            return Wildcard(self._file_or_dir_field_name, query)
        return Wildcard(self._file_or_dir_field_name, '*' + query + '*')        
        
    def contains_or_wildcard_search(self, query: str) -> List[Path]:
        if not query:
            return []
        whoosh_contains_query = self._create_wildcard_search_query(query)
        return self._search_whoosh_query(whoosh_contains_query)
        
    def multi_word_contains_or_wildcard_search(self, multi_word_query: List[str]) -> List[Path]:
        # create multi-word query
        if not multi_word_query:
            return []
        whoosh_multisearch_query = self._create_wildcard_search_query(multi_word_query[0])
        for i in range(1, len(multi_word_query)):
            whoosh_multisearch_query &= self._create_wildcard_search_query(multi_word_query[i])

        return self._search_whoosh_query(whoosh_multisearch_query)
    

