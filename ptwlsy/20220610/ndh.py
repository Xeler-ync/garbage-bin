import math
import numpy as np


class celiang():
    def __init__(self,datas:dict[str,float],name:str,lambda_:float=589.3/1000) -> None: # lambda_ as nm -> mm
        self.datas = datas
        # self.datas['x0'] = [i/100 for i in datas['x0']]
        # self.datas['x_real'] = [i/100 for i in datas['x_real']]
        # self.datas['h_real'] = [i/100 for i in datas['h_real']]
        # self.datas['h_li'] = [i/100 for i in datas['h_li']]
        self.name = name
        self.lambda_ = lambda_
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
        self.Dm = np.array([i-j for i,j in zip(self.datas['Dml'],self.datas['Dmr'])])
        self.Dn = np.array([i-j for i,j in zip(self.datas['Dnl'],self.datas['Dnr'])])
        self.delta = np.array([pow(pow(i,2)-pow(j,2),0.5) for i,j in zip(self.Dm,self.Dn)])
        self.avg_Dm = self._calc_avg(self.Dm)
        self.avg_Dn = self._calc_avg(self.Dn)
        self.avg_m2_n2 = self._calc_avg(list(pow(i,2)-pow(j,2) for i,j in zip(self.Dm,self.Dn)))
        self.R = self.avg_m2_n2*1000/(4*(10)*self.lambda_)
        self.ua = math.sqrt(10*self.avg_m2_n2)/(10*9)
        self.ub = 0.015/math.pow(3,0.5)
        self.u = math.sqrt(pow(self.ua,2)+pow(self.ub,2))

    def fuck_out_result(self) -> None:
        self._fuck_result()
        print('name     =',self.name)
        print('Dm       =',self.Dm)
        print('Dn       =',self.Dn)
        print('delta    =',self.delta)
        print('avg_Dm   =',self.avg_Dm)
        print('avg_Dn   =',self.avg_Dn)
        print('avg_m2_n2=',self.avg_m2_n2)
        print('R        =',self.R)
        print('ua       =',self.ua)
        print('ub       =',self.ub)
        print('u        =',self.u)
        print()


class celiang1():
    def __init__(self,datas:dict[str,float],name:str,lambda_:float=589.3/1000,L:float=4.25) -> None: # lambda_ as nm -> mm L as cm
        self.datas = datas
        self.name = name
        self.lambda_ = lambda_
        self.L = L
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
        self.D = np.array([i*self.lambda_/(j*2) for i,j in zip(self.datas['l1'],self.datas['l0'])])
        self.avg_l = self._calc_avg(self.datas['l0'])
        self.I = np.array([i-j for i,j in zip(self.datas['l0'],self.datas['l1'])])
        temp_sum = 0
        for i in self.datas['l0']:
            temp_sum += pow(i-self.avg_l,2)
        self.ua = math.sqrt(temp_sum/(len(self.datas['l0'])-1))

    def fuck_out_result(self) -> None:
        self._fuck_result()
        print('name     =',self.name)
        print('D        =',self.D)
        print('ua       =',self.ua)
        print('I        =',self.I)
        print()


result_list = [
    celiang(
        datas={
            "m":            np.array([30,29,28,27,26,25]), #mm
            "Dml":          np.array([27.332,27.265,27.215,27.156,27.081,27.010]), #mm
            "Dmr":          np.array([19.040,19.090,19.150,19.210,19.283,19.346]), #mm
            "n ":           np.array([20,19,18,17,16,15]), #mm
            "Dnl":          np.array([26.658,26.588,26.515,26.444,26.362,26.280]), #mm
            "Dnr":          np.array([19.663,19.771,19.839,19.917,20.003,20.100]), #mm
        },
        name="牛顿环",
    ),
    celiang1(
        datas={
            "l0":            np.array([22.698,22.693,22.687,22.678,22.679,22.684]), #mm
            "l1":            np.array([22.273,22.260,22.270,22.260,22.240,22.241]), #mm
        },
        name="劈尖",
    ),
]

# result_list = [
#     celiang(
#         datas={
#             "m":            np.array([30,29,28,27,26,25]), #mm
#             "Dml":          np.array([30.593,30.525,30.475,30.395,30.324,30.278]), #mm
#             "Dmr":          np.array([21.596,21.661,21.719,21.782,21.845,21.910]), #mm
#             "n ":           np.array([20,19,18,17,16,15]), #mm
#             "Dnl":          np.array([29.910,29.833,29.760,29.680,29.602,29.525]), #mm
#             "Dnr":          np.array([22.269,22.342,22.432,22.505,22.581,22.610]), #mm
#         },
#         name="牛顿环",
#     ),
#     celiang1(
#         datas={
#             "l0":            np.array([0.282,0.280,0.285,0.282,0.280,0.285]), #mm
#             "l1":            np.array([0,0,0,0,0,0]), #mm
#         },
#         name="劈尖",
#     ),
# ]