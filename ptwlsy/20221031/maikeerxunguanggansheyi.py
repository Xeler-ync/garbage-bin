import math
import numpy as np


class celiang():
    def __init__(self, datas: dict[str,float], name: str) -> None: # lambda_ as nm -> mm
        self.datas = datas
        self.name = name
        self._calc_T()
        self._opt_T()

    def _calc_avg(self,data:list) -> float:
        try:
            tmp_sum = data.sum()
        except Exception:
            tmp_sum = sum(data)
        return tmp_sum/len(data)

    def _calc_T(self):
        self.avg_T = self._calc_avg(self.datas['T'])

    def _opt_T(self):
        print('T=',self.avg_T)

class celiang1(celiang):
    def __init__(self, datas: dict[str, float], name: str, T1:float, I1_dot: float) -> None:
        super().__init__(datas, name)
        self.T1 = T1
        self.I1_dot = I1_dot

    def _fuck_result(self) -> list[float]:
        self.delta_d = 1

    def fuck_out_result(self) -> None:
        print('delta_d=',self.delta_d)

result_list = [
    celiang(
        datas={
            "N":[
                np.array([33, 36, 39, 42, 45, 48, 51, 54, 57, 60, 63, 69, 72, 75, 81, 84, 87, 90, 93, 96, 99, 100]),
            ], #K
            "d":[
                np.array([226, 236, 244, 254.7, 262, 270, 276, 284, 292, 300.3, 307.3, 323, 331, 343.3, 350, 359.9, 367.5, 374.1, 382.3, 390.8, 398, 400.8]),
                np.array([24, 31, 39.5, 48, 56.7, 64, 72.3, 80.4, 89, 97.7, 105, 113, 121, 129.4, 136, 143, 150, 157, 165, 172, 179]),
                np.array([22.5,25.2,27.8,30.7,33.5,36.2,38.9,41.6,44.3,46.7,49.4,52.1,54.8,57.4,60.2,62.8,65.5,68.2,70.7,73.5]),
                np.array([22.0,24.6,27.2,29.8,32.4,35.0,37.6,40.2,42.8,45.4,48.0,50.6,53.2,55.8,58.4,61.0,63.6,66.2,68.8,71.4]),
            ], #K
        },
        name="",
    ),
]