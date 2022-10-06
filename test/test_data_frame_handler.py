import pytest
from pytest_mock import MockerFixture
from src.data_frame_handler import DataFrameHandler
from src.interfaces.csv_analyser_interface import CsvAnalyserInterface


class TestClassDataFrameHandler:

    class CsvAnalyserStub(CsvAnalyserInterface):

        def get_data_frame(self, path: str) -> object:
            return object

        def drop_null_lines(self, data_frame: object) -> object:
            return object

        def rename_columns(self, data_frame: object, renamed_columns: dict) -> object:
            return object

        def groupby_sum_plot(self, data_frame: object, groupby_plot: list[str]) -> object:
            return object

        def groupby_mean_plot(self, data_frame: object, groupby_plot: list[str]) -> object:
            return object

    CSV_ANALYSER_STUB: CsvAnalyserInterface = CsvAnalyserStub()
    SUT: DataFrameHandler = DataFrameHandler(CSV_ANALYSER_STUB)

    @pytest.mark.parametrize(
        "SUT, CSV_ANALYSER_STUB",
        [(SUT, CSV_ANALYSER_STUB)]
    )
    def test_should_call_get_data_frame_method_with_correct_path(
        self,
        SUT: DataFrameHandler,
        CSV_ANALYSER_STUB: CsvAnalyserInterface,
        mocker: MockerFixture
    ):
        SPY = mocker.spy(CSV_ANALYSER_STUB, 'get_data_frame')
        CSV_PATH = 'any_path'
        SUT.handler(CSV_PATH)
        SPY.assert_called_once_with(CSV_PATH)

    @pytest.mark.parametrize(
        "SUT, CSV_ANALYSER_STUB",
        [(SUT, CSV_ANALYSER_STUB)]
    )
    def test_should_call_drop_null_lines_with_correct_value(
        self,
        SUT: DataFrameHandler,
        CSV_ANALYSER_STUB: CsvAnalyserInterface,
        mocker: MockerFixture
    ):
        SPY = mocker.spy(CSV_ANALYSER_STUB, 'drop_null_lines')
        CSV_PATH = 'any_path'
        SUT.handler(CSV_PATH)
        SPY.assert_called_once_with(object)

    @pytest.mark.parametrize(
        "SUT, CSV_ANALYSER_STUB",
        [(SUT, CSV_ANALYSER_STUB)]
    )
    def test_should_call_rename_columns_with_correct_values(
        self,
        SUT: DataFrameHandler,
        CSV_ANALYSER_STUB: CsvAnalyserInterface,
        mocker: MockerFixture
    ):
        SPY = mocker.spy(CSV_ANALYSER_STUB, 'rename_columns')
        CSV_PATH = 'any_path'
        RENAMED_COLUMNS = {
            'cod': 'Código',
            'nome': 'Estado',
            'período': 'Período',
            'valor': 'Num. mortes'
        }
        SUT.handler(CSV_PATH)
        SPY.assert_called_once_with(object, RENAMED_COLUMNS)

    @pytest.mark.parametrize(
        "SUT, CSV_ANALYSER_STUB",
        [(SUT, CSV_ANALYSER_STUB)]
    )
    def test_should_call_groupby_sum_plot_with_correct_values(
        self,
        SUT: DataFrameHandler,
        CSV_ANALYSER_STUB: CsvAnalyserInterface,
        mocker: MockerFixture
    ):
        SPY = mocker.spy(CSV_ANALYSER_STUB, 'groupby_sum_plot')
        CSV_PATH = 'any_path'
        SUM_PLOT_VALUES = ['Período', 'Num. mortes', 'Total de mortes por período']
        SUT.handler(CSV_PATH)
        SPY.assert_called_once_with(object, SUM_PLOT_VALUES)

    @pytest.mark.parametrize(
        "SUT, CSV_ANALYSER_STUB",
        [(SUT, CSV_ANALYSER_STUB)]
    )
    def test_should_call_groupby_mean_plot_with_correct_values(
        self,
        SUT: DataFrameHandler,
        CSV_ANALYSER_STUB: CsvAnalyserInterface,
        mocker: MockerFixture
    ):
        SPY = mocker.spy(CSV_ANALYSER_STUB, 'groupby_mean_plot')
        CSV_PATH = 'any_path'
        MEAN_PLOT_VALUES = ['Período', 'Num. mortes', 'Média de mortes por período']
        SUT.handler(CSV_PATH)
        SPY.assert_called_once_with(object, MEAN_PLOT_VALUES)
