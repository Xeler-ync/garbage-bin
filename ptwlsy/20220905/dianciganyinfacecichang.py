import math
import numpy as np


_C = 2.926

def calc_B_celiang(f:float,Umax:float) -> float:
    return _C*Umax/f

def calc_B_calc(I:float,N0:int,X:float) -> float:
    return 4*math.pi*pow(10,-7)*N0*I*pow(105,2)/2*pow(pow(105,2)+pow(X,2),1.5)

def calc_B_calc1(Umax:float,theta:float) -> float:
    return Umax*math.cos(theta)

def _calc_avg(data:list) -> float:
    try:
        tmp_sum = data.sum()
    except Exception:
        tmp_sum = sum(data)
    return tmp_sum/len(data)


class celiang():
    def __init__(self,datas:dict[str,float],name:str="",f:int=120,I:int=60,N0:int=400) -> None:
        self.datas = datas
        self.name = name
        self.result = []
        self.f = f
        self.I = I
        self.N0 = N0
        self.fuck_out_result()

    def _fuck_result(self) -> list[float]:
        self.B_celiang = [calc_B_celiang(self.f, _Umax) for _Umax in self.datas['mv']]
        self.B_calc = [calc_B_calc(self.I, self.N0, _X) for _X in self.datas['mm']]

    def fuck_out_result(self) -> None:
        self._fuck_result()

        print(self.name)
        print("-----celiang-----")
        print(self.B_celiang)

        print("-----jisuan-----")
        print(self.B_calc)
        print()

class celiang1():
    def __init__(self,datas:dict[str,float],name:str="",f:int=120,) -> None:
        self.datas = datas
        self.name = name
        self.result = []
        self.f = f
        self.fuck_out_result()

    def _fuck_result(self) -> list[float]:
        self.B_celiang = [calc_B_celiang(self.f, _Umax) for _Umax in self.datas['mv']]

    def fuck_out_result(self) -> None:
        self._fuck_result()

        print(self.name)
        print("-----celiang-----")
        print(self.B_celiang)

        print()

class celiang2():
    def __init__(self,datas:dict[str,float],name:str="",Umax:float=0.0) -> None:
        self.datas = datas
        self.name = name
        self.result = []
        self.Umax = Umax
        self.fuck_out_result()

    def _fuck_result(self) -> list[float]:
        self.B_calc = [calc_B_calc1(self.Umax, theta) for theta in self.datas['deg']]

    def fuck_out_result(self) -> None:
        self._fuck_result()

        print(self.name)
        print("-----calc-----")
        print(self.B_calc)

        print()



result_list = [
    celiang(
        datas={
            "mv": np.array([3.51,3.99,4.49,4.97,5.42,5.79,6.04,6.14,6.07,5.84,5.49,5.04,4.56,4.05,3.57]),
            "mm": np.array(range(-70,70+1,10)),
        },
        name="圆电流线圈轴线上磁场的分布_0deg",
        f=120,I=60,N0=400,
    ),
    celiang(
        datas={
            "mv": np.array([3.48,3.93,4.43,4.91,5.34,5.73,5.98,6.07,6.01,5.78,5.44,5.01,4.51,4.03,3.56]),
            "mm": np.array(range(-70,70+1,10)),
        },
        name="圆电流线圈轴线上磁场的分布_180deg",
        f=120,I=60,N0=400,
    ),
    celiang1(
        datas={
            "mv": np.array([4.70,5.28,5.91,6.55,7.16,7.66,8.09,8.43,8.61,8.70,8.73,8.73,8.73,8.73,8.73,8.70,8.59,8.40,8.06,7.62,7.08,6.45,5.82,5.19,4.56]),
            "mm": np.array(range(-120,120+1,10)),
        },
        name="亥姆霍兹线圈轴线上磁场的分布",
    ),
    celiang(
        datas={
            "mv": np.array([8.52,8.67,8.71,8.73,8.74,8.73,8.73,8.70]),
            "mm": np.array(range(-50,20+1,10)),
        },
        name="圆电流线圈轴线上磁场的分布_径向",
    ),
    celiang2(
        datas={
            "mv": np.array([8.73,8.60,8.22,7.57,6.71,5.59,4.36,3.00,1.42,0.15,1.56,3.05,4.43,5.70,6.75,7.60,8.23,8.57,8.64]),
            "deg": np.array(range(0,180+1,10)),
        },
        name="圆电流线圈轴线上磁场的分布_线圈转角",
        Umax=8.73
    ),
    celiang1(
        datas={
            "mv": np.array([1.42,2.16,2.90,3.63,4.36,5.09,5.81,6.54,7.27,8.00,8.77,9.47]),
            "Hz": np.array(range(20,130+1,10)),
        },
        name="圆电流线圈轴线上磁场的分布_励磁电流频率改变",
    ),
]