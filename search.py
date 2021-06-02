"""
    Entry point for a search query
"""
#import sys
#sys.path.append('.')
"""
from index.index_instances import SearchIndexRepo
from search_plugins.search_results import SearchResult


def print_search_results(search_result: SearchResult):
    print('Showing search results for plugin: {0}'.format(search_result.search_plugin_name))
    for search_item in search_result.search_results:
        print(search_item.item.file_path)

from search_request import SearchMode, SearchRequest
from search_plugins import regex_search_plugin
from search_plugins.search_plugin_instances import SearchPluginRepo

search_plugin_repo = SearchPluginRepo()
lookup_search_plugin = search_plugin_repo.lookup_search_plugin
regex_search_plugin = search_plugin_repo.regex_search_plugin
multi_word_search_plugin = search_plugin_repo.multi_word_search_plugin

while True:
    search_query = input('Enter Search Query ')
    search_request = SearchRequest(search_query, SearchMode.Empty)

    lookup_results = lookup_search_plugin.search(search_request)
    print_search_results(lookup_results)

    regex_results = regex_search_plugin.search(search_request)
    print_search_results(regex_results)

    multi_word_lookup_results = multi_word_search_plugin.search(search_request)
    print_search_results(multi_word_lookup_results)

"""

import sys
sys.path.append('.')

from path_store import PathStore
from adapter.whoosh_adapter import WhooshAdapter

path_store = PathStore()
whoosh_adapter = WhooshAdapter(path_store)
while 1:
    q = input()
    whoosh_adapter.wildcard_search(q)
    print('done searching')
