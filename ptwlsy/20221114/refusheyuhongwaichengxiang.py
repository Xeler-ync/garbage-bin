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
    # plt.show()
    plt.savefig(f'{datas["name"]}.png')
    plt.clf()


t = list(range(30, 80+1, 2))
T = [i+273.13 for i in range(30, 80+1, 2)]
S = list(range(0, 300+1, 10))

lambda_ = 2.8978e3

P1 = [i/1000 for i in [
    61,62,64,66,68,
    69,71,72,76,75,
    77,80,82,83,85,
    88,89,90,93,95,
    97,99,101,104,110,
    112,
]]

P2 = [i/1000 for i in [
    59,59,59,61,61,
    62,62,62,63,63,
    64,65,65,65,67,
    67,67,66,67,68,
    69,69,69,70,72,
    75,
]]

P3 = [i/1000 for i in [
    59,59,59,60,61,
    61,62,62,62,62,
    63,64,65,65,65,
    66,66,65,66,67,
    68,67,68,69,70,
    75,
]]

P4 = [i/1000 for i in [
    68,69,70,70,72,
    73,72,75,78,79,
    78,78,81,81,82,
    84,86,89,89,89,
    86,88,91,94,88,
    96,
]]

P5 = [i/1000 for i in [
    333,126,118,111,108,
    105,99,95,91,86,
    82,78,75,73,71,
    69,68,67,66,65,
    64,64,63,63,62,
    62,62,62,61,61,
    61,
]]

P6 = P1
lambda6 = [lambda_/i for i in T]

draw_pic({
    'x': t,
    'y': P1,
    'xn': 't/℃',
    'yn': 'P/V',
    'name': '黑面温度-辐射强度',
})

draw_pic({
    'x': t,
    'y': P2,
    'xn': 't/℃',
    'yn': 'P/V',
    'name': '糙面温度-辐射强度',
})

draw_pic({
    'x': t,
    'y': P3,
    'xn': 't/℃',
    'yn': 'P/V',
    'name': '光面温度-辐射强度',
})

draw_pic({
    'x': t,
    'y': P4,
    'xn': 't/℃',
    'yn': 'P/V',
    'name': '光面带孔温度-辐射强度',
})

draw_pic({
    'x': S,
    'y': P5,
    'xn': 'x/mm',
    'yn': 'P/V',
    'name': '距离-辐射强度',
})

draw_pic({
    'x': lambda6,
    'y': P6,
    'xn': 'lambda/nm',
    'yn': 'P/V',
    'name': '波长-辐射强度',
})