from abc import ABC, abstractmethod


class CsvAnalyserInterface(ABC):

    @abstractmethod
    def get_data_frame(self, path: str) -> object:
        pass
