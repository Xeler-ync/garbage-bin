from dataclasses import dataclass
import math
from tkinter import N
import numpy as np


class celiang():
    def __init__(self,datas:dict[str,float],name:str,M:float,m:float,d:float,y0:float,g:float=9.81) -> None: # m as gram, x as cm
        self.datas = datas # x0:float,score_real:float,x_real:float,h_real:float   # ,h_li:float
        self.datas['x0'] = [i/100 for i in datas['x0']]
        self.datas['x_real'] = [i/100 for i in datas['x_real']]
        self.datas['h_real'] = [i/100 for i in datas['h_real']]
        # self.datas['h_li'] = [i/100 for i in datas['h_li']]
        self.name = name
        self.M = M/1000 # from g
        self.m = m/1000 # from g
        self.d = d/1000 # from mm
        self.y0 = y0/1000 # from mm
        self.g = g
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
        self.h_li = np.array([pow(self.M+self.m,2)*pow(i,2)/(16*pow(self.M,2)*(self.y0-self.d/2))+self.y0 for i in self.datas['x0']])
        # if len(self.datas['x0']) == len(self.datas['x_real']):
            # self.delta_E = np.array([(i-j)*self.m*self.g for i,j in zip(self.datas['h_li'],self.datas['h_real'])])
        self.delta_E = np.array([(i-j)*self.m*self.g for i,j in zip(self.h_li,self.datas['h_real'])])

    def fuck_out_result(self) -> None:
        self._fuck_result()
        print('name     =',self.name)
        print('h_li     =',self.h_li)
        # if len(self.datas['x0']) == len(self.datas['x_real']):
        print('delta_E  =',self.delta_E)
        print()


result_list = [
    celiang(
        datas={
            "x0":           np.array([9,12,14,22]),
            "score_real":   np.array([10,9,8,8]),
            "x_real":       np.array([8.85,11.1,12.1]),
            "h_real":       np.array([14.09,15.4,16.5,23.0]),
            # "h_li":         np.array([]),
        },
        M = 63.97,
        m = 55.41,
        d = 23.16,
        y0 = 101.1+23.16, # 23.16 should be divided by 2 actually
        name="Untitled",
    ),
]