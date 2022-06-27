import pandas_datareader as pdweb

from kernel.index import Index


class SourceInterface:
    def __init__(self):
        return

    def __str__(self):
        return str(type(self))

    def extract_index(self, index, start_time, end_time):
        raise Exception("this is virtual class")


class PandasInterface(SourceInterface):
    def __init__(self, source="yahoo"):
        SourceInterface.__init__(self)
        self.source = source

    def extract_index(self, index, start_time, end_time, cols=["Close"]):
        assert isinstance(index, Index)
        return pdweb.DataReader(
            name=index.src_name,
            data_source=self.source,
            start=start_time,
            end=end_time
        )[cols]
