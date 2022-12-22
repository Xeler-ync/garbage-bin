import math

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


def draw_pic(datas:dict[str,np.array]) -> None:
    name = f'偏振_{datas[0]["name"]}'

    plt.plot(datas[0]['cos²θ'][0],datas[0]['I'][0],'r-',)
    plt.title(name)
    plt.xlabel('cos²θ/deg')
    plt.ylabel('I/mW')
    plt.legend()
    plt.show()
    plt.savefig(f'{name}.png')
    plt.clf()

def main():
    datas = {
        "cos²θ":[
            np.array(list(math.cos(math.pi*i/12)**2 for i in range(0,6+1))),
        ],
        "I":[
            np.array([
                1.469, 1.397, 1.212, 0.874, 0.469, 0.140, 0.007
            ]),
        ],
        "name":'马吕斯',
    },
    draw_pic(datas)


if __name__ == '__main__':
    main()