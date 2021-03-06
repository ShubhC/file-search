from search_request import SearchRequest
import classifier
from classifier import classifier_names
from classifier.classifier import BinaryClassifier
from classifier.classifier_names import ClassifierNames

class TriggerAllClassifier(BinaryClassifier):
    
    def __init__(self) -> None:
        classifier_name = ClassifierNames.TriggerAll
        super().__init__(classifier_name)

    def predict(self, search_request: SearchRequest):
        return True