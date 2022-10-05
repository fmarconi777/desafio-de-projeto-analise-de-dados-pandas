from src.interfaces.csv_analyser_interface import CsvAnalyserInterface


class DataFrameHandler:

    def __init__(self, CSV_ANALYSER: CsvAnalyserInterface) -> None:
        self.__CSV_ANALYSER = CSV_ANALYSER

    def handler(self, path: str) -> None:
        data_frame = self.__CSV_ANALYSER.get_data_frame(path)
        self.__CSV_ANALYSER.drop_null_lines(data_frame)
        return
