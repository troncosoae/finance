from datetime import datetime

from data_extract.pandas_interface import PandasInterface


class Analyzer:
    def __init__(self):
        self.x = 2
        self.interface = PandasInterface()
    
    def analyze_historical_correlations(self, portfolio):
        print(portfolio)
    
    def extract_historical_index_data(self, index, since, until=""):
        if until == "":
            until = datetime.today().strftime('%Y-%m-%d')
        return self.interface.extract_index(index, 'yahoo', start_time=since, end_time=until)

        
