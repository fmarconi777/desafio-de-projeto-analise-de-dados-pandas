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
