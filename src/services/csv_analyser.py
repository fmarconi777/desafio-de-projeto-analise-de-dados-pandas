from src.handlers.interfaces.csv_analyser_interface import CsvAnalyserInterface
import pandas
import matplotlib.pyplot as plt

class CsvAnalyser(CsvAnalyserInterface):

    def get_data_frame(self, path: str) -> pandas.DataFrame:
        data_frame: pandas.DataFrame = pandas.read_csv(path, on_bad_lines='skip', sep=';')
        return data_frame

    def drop_null_lines(self, data_frame: pandas.DataFrame) -> pandas.DataFrame:
        DATA_FRAME: pandas.DataFrame = data_frame.dropna()
        return DATA_FRAME

    def rename_columns(self, data_frame: pandas.DataFrame, renamed_columns: dict) -> pandas.DataFrame:
        DATA_FRAME:pandas.DataFrame = data_frame.rename(columns=renamed_columns)
        return DATA_FRAME

    def groupby_sum_plot(self, data_frame: pandas.DataFrame, groupby_plot: list[str], path: str) -> None:
        FILE_NAME = path.split('/')
        data_frame.groupby(groupby_plot[0])[groupby_plot[1]].sum().plot.bar(title=groupby_plot[2])
        plt.savefig(f'images/{FILE_NAME[-1][0:-4]}')
        return

    def groupby_mean_plot(self, data_frame: pandas.DataFrame, groupby_plot: list[str], path: str) -> None:
        FILE_NAME = path.split('/')
        data_frame.groupby(groupby_plot[0])[groupby_plot[1]].mean().plot(title=groupby_plot[2])
        plt.savefig(f'images/{FILE_NAME[-1][0:-4]}-mean')
        return