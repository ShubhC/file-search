"""
    Entry point for a search query
"""
#import sys
#sys.path.append('.')

from file_store import FileStore
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

while True:
    search_query = input('Enter Search Query ')
    search_request = SearchRequest(search_query, SearchMode.Empty)

    lookup_results = lookup_search_plugin.search(search_request)
    print_search_results(lookup_results)

    regex_results = regex_search_plugin.search(search_request)
    print_search_results(regex_results)
