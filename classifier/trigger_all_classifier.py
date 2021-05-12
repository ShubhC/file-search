import classifier
from classifier.classifier import BinaryClassifier
from classifier.classifier_instances import ClassifierNames

class TriggerAllClassifier(BinaryClassifier):
    
    def __init__(self) -> None:
        classifier_name = ClassifierNames.TriggerAll
        super().__init__(classifier_name)

    def predict(self):
        return True