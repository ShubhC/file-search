from flask import Flask, request, jsonify
from index.index_instances import SearchIndexRepo
from search_plugins.search_results import SearchResult
from classifier.classifier_instances import ClassifierRepo
from path_store import PathStore
from adapter.whoosh_adapter import WhooshAdapter
from search_request import SearchMode, SearchRequest
from search_plugins import regex_search_plugin
from search_plugins.search_plugin_instances import SearchPluginRepo

app = Flask(__name__)

@app.route('/')
def home():
    return "Hello, Flask!"

def print_search_results(search_result: SearchResult) -> list:
    results = []
    if not search_result:
        return results
    for search_item in search_result.search_results:
        results.append({
            'classifier_score': search_item.classifier_score,
            'index_score': search_item.index_score,
            'file': str(search_item.item)
        })
    return results

# init vars
classifier_repo = ClassifierRepo()
path_store = PathStore()
whoosh_adapter = WhooshAdapter(path_store)
search_plugin_repo = SearchPluginRepo(classifier_repo, path_store, whoosh_adapter)

# all search plugin instances
all_search_plugin_instances = search_plugin_repo.all_search_plugin_instances

@app.route('/search', methods=['POST'])
def search():
    data = request.get_json()
    search_query = data.get('query')
    search_request = SearchRequest(search_query, SearchMode.Empty)
    results = []
    
    # call each search plugin to get results
    for search_plugin in all_search_plugin_instances:
        search_result = search_plugin.search(search_request)
        results.extend(print_search_results(search_result))
    
    return jsonify(results)

if __name__ == '__main__':
    app.run(debug=True)