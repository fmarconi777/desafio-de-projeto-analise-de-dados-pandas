from abc import ABC, abstractmethod
from typing import Any


class CsvAnalyserInterface(ABC):

    @abstractmethod
    def get_data_frame(self, path: str) -> Any:
        pass

    @abstractmethod
    def drop_null_lines(self, data_frame: Any) -> Any:
        pass

    @abstractmethod
    def rename_columns(self, data_frame: Any, renamed_columns: dict) -> Any:
        pass

    @abstractmethod
    def groupby_sum_plot(self, data_frame: Any, groupby_plot: list[str], path: str) -> None:
        pass

    @abstractmethod
    def groupby_mean_plot(self, data_frame: Any, groupby_plot: list[str], path: str) -> None:
        pass
