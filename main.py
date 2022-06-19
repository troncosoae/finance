import pandas as pd
import pandas_datareader.data as web

from data_extract.pandas_interface import PandasInterface
from portfolio.manager import Portfolio
from portfolio.analysis import Analyzer


if __name__ == "__main__":
    print("hello world")

    pi = PandasInterface()
    ezu = pi.extract_index(index='ezu', source='yahoo', start_time='2021-01-01', end_time='2022-01-01')

    print(ezu)

    po = Portfolio(['ezu', 'ivv', 'ewg'])
    # po.add_index('ezu')
    # po.add_index('ivv')
    # po.add_index('ezu')

    an = Analyzer()
    an.analyze_historical_correlations(po, '2019-01-01')
    print(an.extract_historical_index_data('ezu', '2021-01-01'))

    print(po)
