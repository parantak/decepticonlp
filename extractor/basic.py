_AUTHOR_ = "SOMESH"

import abc
import random

class ImportantWordExtractor(metaclass=abc.ABCMeta):
    """
        An abstract class used to represent the Keyword Extractor.SubClass should implement the extract method.
        Methods
        -------
        extract(self, words: list, **kwargs)
            - returns the important word's index.
    """

    @abc.abstractmethod
    def extract(self, words: list, top_k: int, **kwargs):
        """Applies perturbation and returns the word."""
        raise NotImplementedError

class RandomImportantWordExtractor(ImportantWordExtractor):
    """
        A class used to apply random word extractor.
        Methods
        -------
        extract(self, word: list, **kwargs)
            - applies the space perturbation on the word and returns it.
    """

    def extract(self, words: list, top_k=1, **kwargs):
        return random.sample(range(len(words)), top_k)