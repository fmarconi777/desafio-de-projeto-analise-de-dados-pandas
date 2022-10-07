from abc import ABC, abstractmethod


class CsvAnalyserInterface(ABC):

    @abstractmethod
    def get_data_frame(self, path: str) -> object:
        pass

    @abstractmethod
    def drop_null_lines(self, data_frame: object) -> object:
        pass

    @abstractmethod
    def rename_columns(self, data_frame: object, renamed_columns: dict) -> object:
        pass

    @abstractmethod
    def groupby_sum_plot(self, data_frame: object, groupby_plot: list[str], path: str) -> None:
        pass

    @abstractmethod
    def groupby_mean_plot(self, data_frame: object, groupby_plot: list[str], path: str) -> None:
        pass
