import pandas as pd
from extraction.data_container import IndexDataContainer
from kernel.index import IndexGroup


class Analyzer:
    # Analyzers must operate over a single group of indexes
    def __init__(self):
        self.index_group = None
        self.data = pd.DataFrame()
        self.data_returns = pd.DataFrame()
        self.data_means = pd.DataFrame()
        self.data_variances = pd.DataFrame()
        self.data_correlations = pd.DataFrame()
        self.returns_already_calculated = False
        self.means_already_calculated = False
        self.variances_already_calculated = False
        self.correlations_already_calculated = False

    def set_group(self, index_group, data):
        assert isinstance(index_group, IndexGroup)
        assert len(index_group.indexes) == len(data)
        self.index_group = index_group
        self.returns_already_calculated = False
        self.means_already_calculated = False
        self.variances_already_calculated = False
        self.correlations_already_calculated = False
        for index_id in index_group.indexes:
            assert index_group.indexes[index_id].key in data
            subindex_key = index_group.indexes[index_id].key
            assert isinstance(data[subindex_key], IndexDataContainer)
            assert not data[subindex_key].is_empty()
            self.data[subindex_key] = data[subindex_key].get_data()

    def group_is_set(self):
        return self.index_group is not None and \
               not self.data.empty

    def get_returns(self):
        assert self.group_is_set()
        if self.returns_already_calculated:
            return self.data_returns
        # self.data_returns = self.data.diff().dropna()
        data_diff = -1*self.data.diff(periods=-1)
        # data_diff.reset_index(inplace=True, drop=True)
        print(self.data)
        print(data_diff)
        self.data_returns = (data_diff / self.data).dropna()
        print(self.data_returns)
        self.returns_already_calculated = True
        return self.data_returns

    def get_means(self):
        if self.means_already_calculated:
            return self.data_means
        self.data_means = self.get_returns().mean()
        self.means_already_calculated = True
        return self.data_means

    def get_variances(self):
        if self.variances_already_calculated:
            return self.data_variances
        self.data_variances = self.get_returns().var()
        self.variances_already_calculated = True
        return self.data_variances

    def get_correlations(self):
        if self.correlations_already_calculated:
            return self.data_correlations
        self.data_correlations = self.get_returns().corr()
        self.correlations_already_calculated = True
        return self.data_correlations
