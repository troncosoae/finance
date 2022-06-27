from itertools import count


class AbstractIndexGroup:
    new_id = count().__next__

    def __init__(self, key):
        self.id = AbstractIndexGroup.new_id()
        self.key = key


# Node leaf
class Index(AbstractIndexGroup):
    new_id = count().__next__

    def __init__(self, src_name, key=None):
        self.index_id = Index.new_id()
        self.src_name = src_name
        key = src_name if key is None else key
        AbstractIndexGroup.__init__(self, key)

    def __str__(self):
        return f"{self.key}({self.src_name}): -"


# Node other than leaf.
class IndexGroup(AbstractIndexGroup):
    new_id = count().__next__

    def __init__(self, key):
        self.group_id = IndexGroup.new_id()
        AbstractIndexGroup.__init__(self, key)
        self.indexes = {}
        self.index_weights = {}

    def __str__(self):
        return f"{self.key}: "

    def print_recursive(self, steps=0):
        print(self)
        for index_key in self.indexes:
            print(
                "\t"*steps + f"{self.index_weights[index_key]:.3f}",
                end=" -> "
            )
            if isinstance(self.indexes[index_key], IndexGroup):
                self.indexes[index_key].print_recursive(steps=steps+1)
            elif isinstance(self.indexes[index_key], Index):
                print(self.indexes[index_key])

    def add_index(self, index, weight):
        assert isinstance(index, AbstractIndexGroup)
        assert index.id not in self.indexes
        assert index.id not in self.index_weights
        self.__check_weight_correction()
        assert weight <= 1
        self.indexes[index.id] = index
        prev_portion = 1 - weight
        for index_id in self.index_weights:
            self.index_weights[index_id] = \
                self.index_weights[index_id]*prev_portion
        self.index_weights[index.id] = weight

    def add_multiple_indexes(self, indexes, index_weights):
        assert isinstance(index_weights, dict)
        assert isinstance(indexes, dict)
        assert len(indexes) == len(index_weights)
        sum = 0
        for index_key in indexes:
            assert index_key in index_weights
            assert isinstance(indexes[index_key], AbstractIndexGroup)
            sum += index_weights[index_key]
            self.indexes[index_key] = indexes[index_key]
            self.index_weights[index_key] = index_weights[index_key]
        assert sum == 1

    def __check_weight_correction(self):
        sum = 0
        assert len(self.indexes) == len(self.index_weights)
        if len(self.index_weights) == 0:
            return
        for index_id in self.index_weights:
            assert index_id in self.indexes
            sum += self.index_weights[index_id]
        assert sum == 1
