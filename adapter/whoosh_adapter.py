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
            print('adding {0} to index'.format(file_or_dir))
        whoosh_index_writer.commit()
    
    def _search_whoosh_query(self, whoosh_query) -> List[Path]:
        with self._whoosh_index.searcher() as searcher:
            search_results = searcher.search(whoosh_query)        
            for result in search_results:
                print(result)

        return search_results        
    
    def wildcard_search(self, query: str) -> List[Path]:
        whoosh_wildcard_search_query = Wildcard('file_or_dir', query)
        return self._search_whoosh_query(whoosh_wildcard_search_query)
        
    def regex_search(self, query: str) -> List[Path]:
        whoosh_regex_search_query = Regex('file_or_dir', query)
        return self._search_whoosh_query(whoosh_regex_search_query)



