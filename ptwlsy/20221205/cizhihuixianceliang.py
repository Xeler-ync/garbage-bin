import math

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
    plt.plot(datas['x'],datas['y'],'r-',)
    plt.title(datas['name'])
    plt.xlabel(datas['xn'])
    plt.ylabel(datas['yn'])
    plt.legend()
    plt.show()
    plt.savefig(f'{datas["name"]}.png')
    plt.clf()

def parse_DAT():
    with open('20221205\SDS00002.DAT', 'r') as f:
        x = np.array([])
        y = np.array([])
        try:
            while 1:
                line = f.readline()
                line_list = line.split(',')
                # x.append(int(line_list[1]))
                # y.append(int(line_list[2]))
                x = np.append(x, float(line_list[1]))
                y = np.append(y, float(line_list[2]))
        except Exception:
            return x, y



x, y = parse_DAT()

draw_pic({
    'x': x,
    'y': y,
    'xn': 'X/格',
    'yn': 'Y/格',
    'name': '磁滞回线',
})