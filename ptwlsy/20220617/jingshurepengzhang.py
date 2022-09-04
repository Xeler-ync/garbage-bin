import math
import numpy as np


class celiang():
    def __init__(self,datas:dict[str,float],name:str,L:float=0.15) -> None: # lambda_ as nm -> mm
        self.datas = datas
        self.name = name
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
        self.alpha = []
        self.beta = []
        self.t = []
        for i,j in zip(self.datas['T'],self.datas['L']):
            avg_i = self._calc_avg(i)
            avg_j = self._calc_avg(j)
            tmp_sum = sum((l-avg_i)*(m-avg_j) for l, m in zip(i,j))
            tmp_sum1 = sum(pow(l-avg_i,2) for l in i)
            beta = tmp_sum/tmp_sum1
            self.beta.append(beta)
            self.alpha.append(avg_j-beta*avg_i)
            self.t.append(beta/self.L)

    def fuck_out_result(self) -> None:
        self._fuck_result()
        print('t=',self.beta)
        print('t=',self.t)
        print()

result_list = [
    celiang(
        datas={
            "T":[
                np.array([33, 36, 39, 42, 45, 48, 51, 54, 57, 60, 63, 69, 72, 75, 81, 84, 87, 90, 93, 96, 99, 100]),
                np.array([40.5, 43.5, 46.5, 49.5, 52.5, 55.5, 58.5, 61.5, 64.5, 67.5, 70.5, 73.5, 76.5, 79.5, 82.5, 85.5, 88.5, 91.5, 94.5, 97.5, 100.5]),
                np.array([40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59]),
                np.array([65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84]),
            ], #K
            "L":[
                np.array([226, 236, 244, 254.7, 262, 270, 276, 284, 292, 300.3, 307.3, 323, 331, 343.3, 350, 359.9, 367.5, 374.1, 382.3, 390.8, 398, 400.8]),
                np.array([24, 31, 39.5, 48, 56.7, 64, 72.3, 80.4, 89, 97.7, 105, 113, 121, 129.4, 136, 143, 150, 157, 165, 172, 179]),
                np.array([22.5,25.2,27.8,30.7,33.5,36.2,38.9,41.6,44.3,46.7,49.4,52.1,54.8,57.4,60.2,62.8,65.5,68.2,70.7,73.5]),
                np.array([22.0,24.6,27.2,29.8,32.4,35.0,37.6,40.2,42.8,45.4,48.0,50.6,53.2,55.8,58.4,61.0,63.6,66.2,68.8,71.4]),
            ], #K
        },
        name="",
    ),
]