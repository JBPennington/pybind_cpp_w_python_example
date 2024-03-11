import numpy as np

class NumpyWrapper():
    def __init__(self, size: int):
        self.data = np.ones(size)
        
    def get_size(self):
        return int(self.data.shape[0])