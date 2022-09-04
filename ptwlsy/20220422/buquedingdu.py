import math
import numpy as np


class celiang:
    def __init__(self,datas:list,name:str,zhixinxishu:float,datas_type = 'zhijie') -> None:
        self.datas = datas
        self.name = name
        self.delta_DB = zhixinxishu
        self.datas_type = datas_type
        self._calc_avg()
        self._calc_buquedingdu()

    def reflash_data(self) -> None:
        self._calc_avg()
        self._calc_buquedingdu()

    def _calc_avg(self) -> None:
        sum = 0
        for data in self.datas:
            sum += data
        self.avg = sum/len(self.datas)

    def get_avg(self) -> None:
        print('Avg of',self.name,'=',self.avg)

    def _calc_buquedingdu(self) -> None:
        if self.datas_type == 'zhijie':
            Da_sum = 0
            for i in self.datas:
                Da_sum += math.pow(i-self.avg,2)
            self.delta_DA = math.sqrt(Da_sum/(len(self.datas)*(len(self.datas)-1)))
            self.delta_D = math.sqrt(pow(self.delta_DA,2)+pow(self.delta_DB,2))
            self.ED = self.delta_D/self.avg
        elif self.datas_type == 'chengchu':
            pass

    def print_buquedingdu(self) -> None:
        print('delta_DA of',self.name,'=',self.delta_DA)
        print('delta_DB of',self.name,'=',self.delta_DB)
        print('delta_D of',self.name,'=',self.delta_D)
        print('ED of',self.name,'=',self.ED)


D = np.array([20,20.1,20,20.04,20,20,20,20,20,19.84])
d = np.array([28.10,28.10,28.10,28.10,28.10,28.10,28.10,28.10,28.22,28.08])
H = np.array([30.30,30.24,30.32,30.30,30.30,30.26,30.30,30.28,30.28,30.30])
D1 = np.array([8.041,8.042,8.040,8.043,8.038,8.042,8.041,8.038,8.041,8.035])
D2 = np.array([15.081,15.079,15.081,15.081,15.079,15.078,15.070,15.080,15.078,15.054])

# zipper = [D,d,H,D1,D2]

tonghuanneijin = celiang(d,'铜环内径',0.02/math.sqrt(2))
tonghuanwaijin = celiang(D,'铜环外径',0.02/math.sqrt(2))
tonghuangaodu = celiang(H,'铜环高度',0.02/math.sqrt(2))
tongzhugaodu = celiang(D1,'铜柱高度',0.004/3)
qiuzhijin = celiang(D2,'球直径',0.004/3)

all_items = [tonghuanneijin,tonghuanwaijin,tonghuangaodu,tongzhugaodu,qiuzhijin]

for item in all_items:
    item.print_buquedingdu()
    print('\n')


