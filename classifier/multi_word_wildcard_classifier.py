from search_request import SearchRequest
import classifier
from classifier import classifier_names
from classifier.classifier import BinaryClassifier
from classifier.classifier_names import ClassifierNames
from search_request import SearchMode

class MultiWordWildcardClassifier(BinaryClassifier):
    
    def __init__(self) -> None:
        classifier_name = ClassifierNames.MultiWordWildcard
        super().__init__(classifier_name)

    def predict(self, search_request: SearchRequest):
        return search_request.mode == SearchMode.Empty