class Index:
    def __init__(self, index):
        assert isinstance(index, str)
        self.key = index
    
    def __str__(self):
        return index


class IndexPurchaseLog:
    def __init__(self, index, time, end_time):
        self.index = index
        self.time = time
    
    def __str__(self):
        return f"[{self.index}: {self.start_time}]"



class Portfolio:
    def __init__(self, indexes=[], purchase_history=[]):
        # TODO: process purchase_history
        self.indexes = {}
        self.purchase_history = []
        for index in indexes:
            self.add_index(index)
        for purchase in purchase_history:
            self.process_purchase(purchase)

    def __str__(self):
        res = ""
        for index in self.indexes:
            res += index + ", "
        return res
    
    def assert_index_key(self, index):
        assert isinstance(index, str)
    
    def add_index(self, index):
        self.assert_index_key(index)
        self.indexes[index] = Index(index)
    
    def process_purchase(self, purchase):
        assert isinstance(index, IndexPurchaseLog)
        self.purchase_index(purchase.index, purchase.time)
    
    def purchase_index(self, index, time):
        self.assert_index_key(index)
