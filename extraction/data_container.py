from kernel.index import AbstractIndexGroup, Index, IndexGroup
from .interface import SourceInterface


# Must be able to map this back to original index
class IndexDataContainer:
    def __init__(self, index):
        self.key = index.key
        self.data = None
        self.index = index

    def extract_data(self, extraction_interface, start_time, end_time):
        assert isinstance(extraction_interface, SourceInterface)
        if isinstance(self.index, Index):
            self.data = extraction_interface.extract_index(
                self.index, start_time, end_time)

    def is_empty(self):
        return self.data is None

    def get_data(self):
        return self.data


# Meant to extract data to a container
# must contain data extracted for each index
# for leaf indexes data must be extracted only once
# must be able to get the download of an index
class IndexDataExtractor:
    def __init__(self, extracion_interface, index_data_container_map={}):
        assert isinstance(extracion_interface, SourceInterface)
        self.extracion_interface = extracion_interface
        self.index_data_container_map = index_data_container_map
        assert self.index_data_container_map is index_data_container_map

    def __str__(self):
        pass

    # Method that given an index, extracts data for it using
    # the extracion_interface
    def extract_data(self, index, start_time, end_time):
        assert isinstance(index, AbstractIndexGroup)
        key = index.key
        self.index_data_container_map[key] = IndexDataContainer(index)
        if isinstance(index, Index):
            self.index_data_container_map[key].extract_data(
                self.extracion_interface, start_time, end_time)
        elif isinstance(index, IndexGroup):
            is_first = True
            for sub_index_key in index.indexes:
                self.extract_data(
                    index.indexes[sub_index_key],
                    start_time,
                    end_time
                )
                if is_first:
                    self.index_data_container_map[key].data = \
                        self.index_data_container_map[
                            sub_index_key].data.copy()
                    is_first = False
                else:
                    self.index_data_container_map[key].data += \
                        self.index_data_container_map[sub_index_key].data
