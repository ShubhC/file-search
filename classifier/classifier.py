from abc import ABC, abstractmethod, abstractproperty
from enum import Enum

class Classifier(ABC):    
    def __init__(self, classifier_name) -> None:
        self._classifier_name = classifier_name
    
    @property
    def classifier(self):
        return self._classifier_name
    
    @abstractmethod
    def predict(self):
        pass
    
class BinaryClassifier(Classifier):
    def __init__(self, classifier_name) -> None:
        super().__init__(classifier_name)

    def trigger(self):
        trigger_prediction = self.predict()
        return trigger_prediction