class SourceInterface:
    def __init__(self):
        return
    
    def __str__(self):
        return str(type(self))

    def extract_index(self, index, source, start_time, end_time):
        raise Exception("this is virtual class")

    

