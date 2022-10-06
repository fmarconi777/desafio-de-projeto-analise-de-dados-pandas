from src.handlers.interfaces.csv_analyser_interface import CsvAnalyserInterface


class DataFrameHandler:

    def __init__(self, CSV_ANALYSER: CsvAnalyserInterface) -> None:
        self.__CSV_ANALYSER = CSV_ANALYSER

    def handler(self, path: str) -> None:
        data_frame = self.__CSV_ANALYSER.get_data_frame(path)
        data_frame = self.__CSV_ANALYSER.drop_null_lines(data_frame)
        RENAMED_COLUMNS = {
            'cod': 'Código',
            'nome': 'Estado',
            'período': 'Período',
            'valor': 'Num. mortes'
        }
        data_frame = self.__CSV_ANALYSER.rename_columns(data_frame, RENAMED_COLUMNS)
        SUM_PLOT_VALUES = ['Período', 'Num. mortes', 'Total de mortes por período']
        self.__CSV_ANALYSER.groupby_sum_plot(data_frame, SUM_PLOT_VALUES)
        MEAN_PLOT_VALUES = ['Período', 'Num. mortes', 'Média de mortes por período']
        self.__CSV_ANALYSER.groupby_mean_plot(data_frame, MEAN_PLOT_VALUES)
        return
