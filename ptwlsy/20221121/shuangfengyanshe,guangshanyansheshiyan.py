try: # check if they were installed
    import matplotlib
    import matplotlib.pyplot as plt
    import numpy as np
except Exception:
    import os
    os.system('pip install matplotlib; pip install numpy')
    import matplotlib
    import matplotlib.pyplot as plt
    import numpy as np


matplotlib.rcParams['font.sans-serif'] = ['KaiTi'] # 让这玩意能正常显示中文
matplotlib.rcParams['font.serif'] = ['KaiTi']


def draw_pic(datas:dict[str,np.array]) -> None:
    name = f'{datas["name"]}'

    plt.plot(datas['X'],datas['P'],'r-',)
    plt.title(name)
    plt.xlabel('X/mm')
    plt.ylabel('P/μW')
    plt.legend()
    # plt.show()
    plt.savefig(f'{name}.png')
    plt.clf()

def main():
    datas = {
        "X": np.array([
                34.700, 34.700,
                35.100, 35.30, 35.50, 35.70, 35.90, 36.10, 36.30, 36.50, 36.70, 36.90,
                37.225, 37.42, 37.62, 37.82, 38.02, 38.22, 38.42, 38.62, 38.82, 39.02,
                39.470, 39.67, 39.87, 40.07, 40.27, 40.47, 40.67, 40.87, 41.07, 41.27,
                41.620, 41.82, 42.02, 42.22, 42.42, 42.62, 42.82, 43.02, 43.22, 43.42,
                43.742, 43.942, 44.142,
            ]),
        "P": np.array([
                0.6, 0.89,
                1.25, 1.02, 0.68, 0.41, 0.18, 0.97, 3.33, 4.08, 5.82, 8.01,
                8.40, 7.68, 5.980, 3.31, 1.53, 0.28, 1.21, 5.94, 7.75, 12.23,
                12.45, 10.75, 8.81, 4.88, 2.16, 0.36, 0.55, 1.35, 4.06, 5.17,
                7.30, 6.42, 5.73, 4.21, 2.32, 1.06, 0.30, 0.18, 0.52, 1.20,
                1.41, 1.37, 0.82,
            ]),
        "name":'双缝衍射',
    }
    draw_pic(datas)

    datas1 = {
        "X": np.array([
                16.96, 17.96,
                18.96, 20.16, 21.36, 22.56, 23.76, 24.96, 26.16, 27.36, 28.56, 29.56,
                29.73, 30.83, 31.93, 33.03, 34.13, 35.23, 36.33, 37.43, 38.53, 39.63,
                40.29, 41.95, 43.15, 44.35, 45.55, 46.75, 47.95, 49.15, 50.35, 51.45,
                52.65, 53.66, 54.66, 55.66, 56.66, 57.66, 58.66, 59.66, 60.66, 61.66,
                62.66, 63.66, 64.66,
            ]),
        "P": np.array([
                0.2, 4.2,
                10.5, 1.0, 0.2, 0.1, 0.1, 0.1, 0.1, 0.5, 1.2, 25.4,
                26.4, 7.6, 0.3, 0.2, 0.2, 0.1, 0.1, 0.5, 0.8, 8.6,
                164.8, 5.3, 0.5, 0.2, 0.1, 0.1, 0.1, 0.2, 1.0, 22.3,
                23.3, 0.3, 0.2, 0.2, 0.1, 0.1, 0.1, 0.1, 0.2, 3.5,
                7.4, 0.9, 0.1,
            ]),
        "name":'光栅衍射',
    }
    draw_pic(datas1)

if __name__ == '__main__':
    main()