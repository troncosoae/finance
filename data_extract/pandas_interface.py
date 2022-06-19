import pandas as pd
import pandas_datareader as pdweb

from .base_interface import SourceInterface


class PandasInterface(SourceInterface):
    def __init__(self):
        self.x = 'x'
        SourceInterface.__init__(self)

    def extract_index(self, index, source, start_time, end_time):
        return pdweb.DataReader(name=index, data_source=source, start=start_time, end=end_time)
