from abc import ABC, abstractmethod


class CsvAnalyserInterface(ABC):

    @abstractmethod
    def get_data_frame(self, path: str) -> object:
        pass

    @abstractmethod
    def drop_null_lines(self, data_frame: object) -> object:
        pass
