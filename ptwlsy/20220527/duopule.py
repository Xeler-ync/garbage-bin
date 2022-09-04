import math
import numpy as np


class celiang():
    # def __init__(self,datas:dict[np.array[float]],m1:float,m2:float,x1:float,x2:float,name:str,exp_type = 'tx') -> None: # m as gram, x as cm
    def __init__(self,datas:dict[str,float],name:str,f:float = 37000.0,c0:float = 330.0) -> None: # m as gram, x as cm
        self.datas = datas # Vs:float,f_positive:float,f_negetive:float
        self.delta_f_positive = np.array([f-i for i in self.datas['f_positive']])
        self.delta_f_negetive = np.array([f-i for i in self.datas['f_negetive']])
        self.name = name
        self.f = f
        self.c0 = c0
        self.fuck_out_result()

    def _calc_avg(self,data:list) -> float:
        # if len(data) == 0:
        #     return 0
        try:
            tmp_sum = data.sum()
        except Exception:
            tmp_sum = sum(data)
        return tmp_sum/len(data)

    def _fuck_result(self) -> list[float]:
        self.delta_f = np.array([(abs(i)+abs(j))/2 for i,j in zip(self.delta_f_positive,self.delta_f_negetive)])
        self.V = np.array([i*self.f/j for i,j in zip(self.datas['Vs'],self.delta_f)])
        self.V_avg = self._calc_avg(self.V)
        self.delta_avg = (self.V_avg - self.c0) / self.c0

    def fuck_out_result(self) -> None:
        self._fuck_result()
        print('name             =',self.name)
        print('delta_f_positive =',self.delta_f_positive)
        print('delta_f_negetive =',self.delta_f_negetive)
        print('delta_f          =',self.delta_f)
        print('V                =',self.V)
        print('V_avg            =',self.V_avg)
        print('delta_avg        =',self.delta_avg)
        print()


class celiang1():
    def __init__(self,datas:dict[str,float],name:str,f:float = 37000.0,c0:float = 330.0,multipy_rate:int = 1,divide_rate:int = 100) -> None:
        self.datas = datas
        self.datas['Li'] = [i/divide_rate for i in datas['Li']]
        self.name = name
        self.f = f
        self.c0 = c0
        self.multipy = multipy_rate
        self.divide_rate = divide_rate
        self.fuck_out_result()

    def _calc_avg(self,data:list) -> float:
        # if not data:
        #     return 0
        try:
            tmp_sum = data.sum()
        except Exception:
            tmp_sum = sum(data)
        return tmp_sum/len(data)

    def _fuck_result(self) -> list[float]:
        self.lambda_ = np.array([(i-j)*self.multipy for i,j in zip(self.datas['Li'][:-1],self.datas['Li'][1:])])
        # print(self.datas['Li'][:math.ceil(len(self.datas['Li'])/2)+1])
        # print(math.ceil(len(self.datas['Li'])/2))
        self.lambda_avg = (( -self._calc_avg(self.datas['Li'][:math.ceil(len(self.datas['Li'])/2)+1]) + self._calc_avg(self.datas['Li'][math.ceil(len(self.datas['Li'])/2):]) ) / math.ceil(len(self.datas['Li'])/2)) * self.multipy
        self.V_avg = self.lambda_avg * self.f
        self.delta_avg = (self.V_avg-self.c0)/self.c0

    def fuck_out_result(self) -> None:
        self._fuck_result()
        print('name       =',self.name)
        print('lambda_    =',self.lambda_)
        print('lambda_avg =',self.lambda_avg)
        print('V_avg      =',self.V_avg)
        print('delta_avg  =',self.delta_avg)
        print()

result_list = [
    celiang(
        datas={
            "Vs":               np.array([0.059,0.087,0.115,0.142,0.168,0.193,0.218,0.243,0.266,0.288,0.311,0.334,0.355,0.375,0.397]),
            "f_positive":       np.array([37977,37979,37983,37986,37989,37991,37994,37996,37999,37998,38004,38008,38004,38014,38014]),
            "f_negetive":       np.array([37963,37960,37957,37954,37951,37949,37946,37943,37941,37938,37935,37932,37931,37929,37926])
        },
        f=37970.0,
        c0=331.45*math.sqrt((27+273.16)/273.16),
        name="多普勒法",
    ),
    celiang1(
        datas={
            "Li":   np.array([25.5,26.412,27.315,28.215,29.130,30.030,30.945,31.900,32.810,33.750,34.625]),
        },
        f=37970.0,
        c0=331.45*math.sqrt((27+273.16)/273.16),
        name="相位法",
        multipy_rate = 1,
        divide_rate = 100,
    ),
    celiang1(
        datas={
            "Li":   np.array([333.15,338.07,342.3,346.0,351.3,356.05,360.4,365.3,370.12,374.3,379,383.35]),
        },
        f=37970.0,
        c0=331.45*math.sqrt((27+273.16)/273.16),
        name="驻波法",
        multipy_rate = 2,
        divide_rate = 1000,
    ),
]