import math
from matplotlib import pyplot as plt
import numpy as np


def new_liner(x:np.array,y:np.array):
    plt.plot(x,y)
    pass

def main():
    new_liner(np.array(range(0,300+1,30)),np.array([29.4,29.3,29.3,29.2,29.1,29.0,29.0,28.9,28.8,28.8,28.6]))
    new_liner(np.array(range(0,620+1,30)),np.array([26.6, 26.6, 26.6, 26.7, 26.8, 26.8, 26.7, 26.7, 26.7, 26.6, 26.6]))
    plt.show()
    pass

if __name__ == '__main__':
    main()