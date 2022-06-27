from kernel.index import Index, IndexGroup
from extraction.data_container import IndexDataExtractor


class IndexSession:
    def __init__(self, extracion_interface):
        self.index_dict = {}
        self.index_data_extractor = IndexDataExtractor(
            extracion_interface)
        self.data_dict = self.index_data_extractor.index_data_container_map

    def __getitem__(self, key):
        return self.index_dict[key]

    def __setitem__(self, key, value):
        self.index_dict[key] = value

    def __str__(self):
        return str(self.index_dict)

    def export_index_group_data(self, index_key):
        index = self.index_dict[index_key]
        assert isinstance(index, IndexGroup)
        print(self.data_dict)
        # print([self.data_dict[index.indexes[subindex_id].key]
        #     for subindex_id in index.indexes])
        return {
            index.indexes[subindex_id].key:
                self.data_dict[index.indexes[subindex_id].key]
            for subindex_id in index.indexes
        }


class IndexFactory:
    def __init__(self):
        self.json = None
        self.index_session = None

    def generate_session(self, json, extraction_interface):
        self.json = json
        self.index_session = IndexSession(extraction_interface)
        self.process_json()
        return self.index_session

    def process_json(self):
        self.process_json_indexes()
        self.process_json_index_groups()

    def process_json_indexes(self):
        for index_key in self.json["indexes"]:
            self.index_session[index_key] = Index(
                self.json["indexes"][index_key], index_key)

    def process_json_index_groups(self):
        for group_key in self.json["index_groups"]:
            self.index_session[group_key] = IndexGroup(group_key)
            indexes = {
                index_key: self.index_session[index_key]
                for index_key in self.json["index_groups"][group_key]
            }
            index_weights = {
                index_key: self.json["index_groups"][group_key][index_key]
                for index_key in self.json["index_groups"][group_key]
            }
            self.index_session[group_key].add_multiple_indexes(
                indexes, index_weights
            )
