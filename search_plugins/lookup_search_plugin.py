from search_plugins.search_plugins import SearchPlugin
from search_plugins.search_plugin_instances import SearchPluginName
from classifier.classifier_instances import ClassifierRepo
from index.index_instances import SearchIndexRepo

class LookupSearchPlugin(SearchPlugin):

    def __init__(self, index):
        self._model_name = SearchPluginName.LookupSeachPlugin
        self._index = SearchIndexRepo.LookupIndex
        self._classifier = ClassifierRepo.TriggerAllClassifier
        SearchPlugin.__init__(self, 
                              self._model_name, 
                              self._index,
                              self._classifier)