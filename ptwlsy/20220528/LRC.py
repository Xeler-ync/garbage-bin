import math
import numpy as np


class celiang():
    def __init__(self,datas:dict[str,float],name:str,L:float=10,C:float=0.01,R:float=1) -> None: # m as gram, x as cm
        self.datas = datas # f:float
        self.datas['f'] = [i/1000 for i in datas['f']] # from kHz
        self.name = name
        self.L = L/1000 # from mH
        self.C = C/1000000 # from miu_F
        self.R = R*1000 # from k_oum
        self.fuck_out_result()

    def _calc_avg(self,data:list) -> float:
        try:
            tmp_sum = data.sum()
        except Exception:
            if not data:
                return 0
            tmp_sum = sum(data)
        return tmp_sum/len(data)

    def _fuck_result(self) -> list[float]:
        self.f0 = 1/(2*math.pi*math.sqrt(self.L*self.C))
        self.f_avg = self._calc_avg(self.datas['f'])
        self.deviation = (self.f0-self.f_avg)/self.f0

    def fuck_out_result(self) -> None:
        self._fuck_result()
        print('name         =',self.name)
        print('f0           =',self.f0)
        print('f_avg        =',self.f_avg)
        print('deviation    =',self.deviation)
        print()

class celiang1():
    def __init__(self,datas:dict[str,float],name:str,U:float,L:float=10,C:float=0.01,R:float=1) -> None: # m as gram, x as cm
        self.datas = datas # f:float,UR:float,delta_t:float
        self.datas['f'] = [i*1000 for i in datas['f']] # from kHz
        self.datas['delta_t'] = [i/1000000 for i in datas['delta_t']] # from miu_A
        self.name = name
        self.U = U
        self.L = L/1000 # from mH
        self.C = C/1000000 # from miu_F
        self.R = R*1000 # from k_oum
        self.fuck_out_result()

    def _calc_avg(self,data:list) -> float:
        try:
            tmp_sum = data.sum()
        except Exception:
            if not data:
                return 0
            tmp_sum = sum(data)
        return tmp_sum/len(data)

    def _fuck_result(self) -> list[float]:
        self.I = self.datas['UR']/self.R
        self.phy = np.array([2*math.pi*i*j for i,j in zip(self.datas['delta_t'],self.datas['f'])])

    def fuck_out_result(self) -> None:
        self._fuck_result()
        print('name =',self.name)
        print('I    =',self.I)
        print('phy  =',self.phy)
        print()

class celiang2():
    def __init__(self,datas:dict[str,float],name:str,U:float,L:float=10,C:float=0.01,R:float=1) -> None: # m as gram, x as cm
        self.datas = datas # Uc:float
        self.name = name
        self.fuck_out_result()

    def _calc_avg(self,data:list) -> float:
        try:
            tmp_sum = data.sum()
        except Exception:
            if not data:
                return 0
            tmp_sum = sum(data)
        return tmp_sum/len(data)

    def _fuck_result(self) -> list[float]:
        self.unnamed = []
        for i in self.datas['Uc']:
            try:
                self.unnamed.append(math.log(abs(i),math.e))
            except Exception:
                self.unnamed.append(0)


    def fuck_out_result(self) -> None:
        self._fuck_result()
        print('name     =',self.name)
        print('unnamed  =',self.unnamed)
        print()



result_list = [
    celiang(
        datas={
            "f":           np.array([15.590,15.664,15.564,15.563,15.556]),
        },
        name="幅频特性测试",
    ),
    celiang1(
        datas={
            "f":           np.array([2,4,6,10,14,16,18,33,48,54]),
            "UR":          np.array([0.6,1.08,1.64,2.92,3.8,3.84,3.62,1.62,0.74,0.6]),
            "delta_t":     np.array([112,177.2,30,11.3,2.44,0.72,2.6,5.48,5.7,5.84]),
        },
        U = 4,
        R = 1000,
        name="相频特性测试",
    ),
    celiang2(
        datas={
            "Uc":           np.array([0,4325,0,-3837,0,3286,0,-3072,0,2692,0,-2438]),
        },
        U = 4,
        R = 1000,
        name="串联电路的暂态特性",
    ),
]