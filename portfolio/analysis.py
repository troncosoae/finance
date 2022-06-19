from datetime import datetime
import pandas as pd

from data_extract.pandas_interface import PandasInterface
from .manager import Portfolio


class Analyzer:
    def __init__(self, source="yahoo"):
        self.source = source
        self.interface = PandasInterface()
    
    def analyze_historical_correlations(self, portfolio, since, until=""):
        assert isinstance(portfolio, Portfolio)
        if until == "":
            until = datetime.today().strftime('%Y-%m-%d')

        index_data = pd.DataFrame()
        for index in portfolio.indexes:
            index_data[index] = self.extract_historical_index_data(index, since, until)["Close"]
        print(index_data)
        print(index_data.corr())

    def extract_historical_index_data(self, index, since, until=""):
        if until == "":
            until = datetime.today().strftime('%Y-%m-%d')
        return self.interface.extract_index(index, self.source, start_time=since, end_time=until)

        
