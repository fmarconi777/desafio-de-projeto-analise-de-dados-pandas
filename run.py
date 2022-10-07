from src.handlers.data_frame_handler import DataFrameHandler
from src.services.csv_analyser import CsvAnalyser

if __name__ == '__main__':
    def make_data_frame_handler() -> DataFrameHandler:
        CSV_ANALYSER = CsvAnalyser()
        DATA_FRAME_HANDLER = DataFrameHandler(CSV_ANALYSER)
        return DATA_FRAME_HANDLER


    DATA_FRAME_HANDLER = make_data_frame_handler()
    DATA_FRAME_HANDLER.handler('data/homicidios-homens-nao-negros.csv')
    