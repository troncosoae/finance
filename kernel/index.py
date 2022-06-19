import itertools


class AbstractIndexGroup:
    new_id = itertools.count().__next__
    def __init__(self, name):
        self.id = AbstractIndexGroup.new_id()
        self.name = name

class Index(AbstractIndexGroup):
    new_index_id = itertools.count().__next__
    def __init__(self, src_name, name=None):
        # TODO: names must be unique
        self.index_id = Index.new_index_id()
        self.src_name = src_name
        name = src_name if name is None else name
        AbstractIndexGroup.__init__(self, name)

    def __str__(self):
        return f"{self.name}({self.src_name}): -"


class IndexGroup(AbstractIndexGroup):
    new_group_id = itertools.count().__next__
    def __init__(self, name):
        # TODO: names must be unique
        self.group_id = IndexGroup.new_group_id()
        AbstractIndexGroup.__init__(self, name)
        self.indexes = {}

    def __str__(self):
        return f"{self.name}: "
    
    def print_recursive(self, steps=0):
        print("\t"*steps + str(self))
        for index_key in self.indexes:
            if isinstance(self.indexes[index_key], IndexGroup):
                self.indexes[index_key].print_recursive(steps=steps+1)
            elif isinstance(self.indexes[index_key], Index):
                print("\t"*(steps+1) + str(self.indexes[index_key]))
    
    def add_index(self, index):
        assert isinstance(index, AbstractIndexGroup)
        self.indexes[index.id] = index


class IndexFactory:
    def __init__(self, json, index_universe):
        self.json = json
        self.index_universe = index_universe
        self.process_json(json)
    
    def process_json(self, json):
        self.process_json_indexes(json["indexes"])
        self.process_json_index_groups(json["index_groups"])
    
    def process_json_indexes(self, json):
        for index_key in json:
            self.index_universe[index_key] = Index(json[index_key], index_key)
    
    def process_json_index_groups(self, json):
        for group_key in json:
            self.index_universe[group_key] = IndexGroup(group_key)
            for index_key in json[group_key]:
                self.index_universe[group_key].add_index(
                    self.index_universe[index_key]
                )


class IndexSession:
    def __init__(self):
        self.index_universe = {}
    
    def get_index(self, key):
        return self.index_universe[key]
    
    def enter_index(self, key, index):
        self.index_universe[key] = index
