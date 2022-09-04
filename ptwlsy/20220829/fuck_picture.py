try: # check if they were installed
    import matplotlib.pyplot as plt
    import matplotlib
    import numpy as np
except Exception:
    import os
    os.system('pip install matplotlib; pip install numpy')
    import matplotlib.pyplot as plt
    import matplotlib
    import numpy as np


matplotlib.rcParams['font.sans-serif'] = ['KaiTi'] # 让这玩意能正常显示中文
matplotlib.rcParams['font.serif'] = ['KaiTi']

def main():
    datas = {
        "U":[
            np.array(range(-900,900+1,20)),
        ], #K
        "P":[
            np.array([
                0.28,0.36,0.43,0.51,0.57,0.64,0.69,0.72,0.78,0.80,0.83,0.83,0.85,0.84,0.82,
                0.79,0.76,0.71,0.66,0.60,0.52,0.45,0.36,0.29,0.22,0.16,0.11,0.07,0.05,0.04,
                0.04,0.07,0.11,0.16,0.23,0.32,0.40,0.49,0.58,0.66,0.73,0.81,0.88,0.94,0.99,
                1.03,1.07,1.09,1.09,1.09,1.07,1.05,1.02,0.97,0.92,0.85,0.79,0.72,0.63,0.54,
                0.45,0.36,0.29,0.22,0.18,0.14,0.12,0.12,0.13,0.17,0.22,0.26,0.34,0.42,0.49,
                0.55,0.62,0.68,0.74,0.79,0.84,0.88,0.89,0.92,0.93,0.93,0.92,0.90,0.87,0.83,
                0.79,
            ]),
        ], #K
    },
    plt.plot(datas[0]['U'][0],datas[0]['P'][0],'ro-',)
    plt.title('电光效应')
    plt.xlabel('U/V')
    plt.ylabel('P/mW')
    plt.legend()
    plt.show()
    plt.savefig('./fuck_picture.png')

if __name__ == '__main__':
    main()