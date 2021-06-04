"""
    Entry point for a search query
"""
#import sys
#sys.path.append('.')
from index.index_instances import SearchIndexRepo
from search_plugins.search_results import SearchResult
from classifier.classifier_instances import ClassifierRepo
from path_store import PathStore
from adapter.whoosh_adapter import WhooshAdapter
from search_request import SearchMode, SearchRequest
from search_plugins import regex_search_plugin
from search_plugins.search_plugin_instances import SearchPluginRepo

def print_search_results(search_result: SearchResult) -> None: 
    if not search_result:
        return
    print('Showing search results for plugin: {0}'.format(search_result.search_plugin_name))
    for search_item in search_result.search_results:
        print('classifier_score: {0}, index_score: {1}, file: {2}'
              .format(search_item.classifier_score, search_item.index_score, search_item.item))

# init vars
classifier_repo = ClassifierRepo()
path_store = PathStore()
whoosh_adapter = WhooshAdapter(path_store)
search_plugin_repo = SearchPluginRepo(classifier_repo, path_store, whoosh_adapter)

# all search plugin instances
all_search_plugin_instances = search_plugin_repo.all_search_plugin_instances

while True:
    search_query = input('Enter Search Query ')
    search_request = SearchRequest(search_query, SearchMode.Empty)

    # call each search plugin to get results
    for search_plugin in all_search_plugin_instances:
        search_result = search_plugin.search(search_request)
        print_search_results(search_result)
        
