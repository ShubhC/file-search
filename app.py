import pickle
from flask import Flask, request, jsonify
from index.index_instances import SearchIndexRepo
from search_plugins.search_results import SearchResult
from classifier.classifier_instances import ClassifierRepo
from path_store import PathStore
from adapter.whoosh_adapter import WhooshAdapter
from search_request import SearchMode, SearchRequest
from search_plugins import regex_search_plugin
from search_plugins.search_plugin_instances import SearchPluginRepo
import os
from quickstart import generate_keywords

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


indexing_done_flag = False
pickle_file = 'search_plugin_repo.pkl'
if os.path.exists(pickle_file):
    indexing_done_flag = True

# init vars
classifier_repo = ClassifierRepo(indexing_done_flag)
path_store = PathStore(indexing_done_flag)
whoosh_adapter = WhooshAdapter(path_store, indexing_done_flag)

# Check if the pickle file exists
if indexing_done_flag:
    with open(pickle_file, 'rb') as f:
        search_plugin_repo = pickle.load(f)
else:
    search_plugin_repo = SearchPluginRepo(classifier_repo, path_store, whoosh_adapter)
    with open(pickle_file, 'wb') as f:
        pickle.dump(search_plugin_repo, f)

# all search plugin instances
all_search_plugin_instances = search_plugin_repo.all_search_plugin_instances

@app.route('/search', methods=['POST'])
def search():
    data = request.get_json()
    search_query = data.get('query')
    
    search_request = SearchRequest(search_query, SearchMode.Empty)
    results = []

    for search_plugin in all_search_plugin_instances:
        search_result = search_plugin.search(search_request)
        results.extend(print_search_results(search_result))

    return jsonify(results)

@app.route('/deep-search', methods=['POST'])
def deep_search():
    data = request.get_json()
    search_query = data.get('query')
     # Generate keywords using quickstart.py
    keywords = generate_keywords(search_query)

    # Split the keywords into a list
    keyword_list = [keyword.strip() for keyword in keywords.split(',')]

    search_request = SearchRequest(search_query, SearchMode.Empty)
    results = []

    # call each search plugin to get results
    for keyword in keyword_list:
        print(keyword)
        search_request = SearchRequest(keyword, SearchMode.Empty)
        for search_plugin in all_search_plugin_instances:
            search_result = search_plugin.search(search_request)
            results.extend(print_search_results(search_result))

    return jsonify(results)

if __name__ == '__main__':
    app.run(debug=True)