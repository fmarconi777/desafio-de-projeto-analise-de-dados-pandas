from src.handlers.data_frame_handler import DataFrameHandler
from src.services.csv_analyser import CsvAnalyser

def make_data_frame_handler() -> DataFrameHandler:
    CSV_ANALYSER = CsvAnalyser()
    DATA_FRAME_HANDLER = DataFrameHandler(CSV_ANALYSER)
    return DATA_FRAME_HANDLER


if __name__ == '__main__':
    DATA_FRAME_HANDLER = make_data_frame_handler()
    DATA_FRAME_HANDLER.handler('data/homicidios-homens-nao-negros.csv')
    DATA_FRAME_HANDLER.handler('data/homicidios-homens-negros.csv')
    DATA_FRAME_HANDLER.handler('data/homicidios-homens.csv')
    DATA_FRAME_HANDLER.handler('data/homicidios-mulheres-nao-negras.csv')
    DATA_FRAME_HANDLER.handler('data/homicidios-mulheres-negras.csv')
    DATA_FRAME_HANDLER.handler('data/homicidios-mulheres.csv')
    DATA_FRAME_HANDLER.handler('data/taxa-de-homicidios-faixa-etaria-de-15-29-anos-homens.csv')
    DATA_FRAME_HANDLER.handler('data/taxa-de-homicidios-faixa-etaria-de-15-29-anos-mulheres.csv')
    