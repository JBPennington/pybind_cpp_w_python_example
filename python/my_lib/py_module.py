import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt

class NumpyWrapper():
    def __init__(self, size: int):
        self.data = np.ones(size)
        
    def get_size(self):
        return int(self.data.shape[0])

    def plot(self):
        mpl.use('Qt5Agg')
        plt.style.use('_mpl-gallery')

        # make the data
        np.random.seed(3)
        x = 4 + np.random.normal(0, 2, 24)
        y = 4 + np.random.normal(0, 2, len(x))
        # size and color:
        sizes = np.random.uniform(15, 80, len(x))
        colors = np.random.uniform(15, 80, len(x))

        # plot
        fig, ax = plt.subplots()

        ax.scatter(x, y, s=sizes, c=colors, vmin=0, vmax=100)

        ax.set(xlim=(0, 8), xticks=np.arange(1, 8),
               ylim=(0, 8), yticks=np.arange(1, 8))

        plt.show()
