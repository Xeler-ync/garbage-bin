import math
import numpy as np


class celiang:
    def __init__(self,datas:list,L:float,name:str,zhixinxishu:float,datas_type = 'zhijie') -> None:
        self.datas = datas
        self.L = L
        self.name = name
        self.delta_DB = zhixinxishu
        self.datas_type = datas_type
        self.sigma_L = 0.04
        self._calc_avg()
        self._calc_avg_divise_40()
        self._calc_sigma_t()
        self._calc_sigma_T()
        self._calc_avg_g()
        self._calc_sigma_g()
        
        # self._calc_buquedingdu()

    def reflash_data(self) -> None:
        self._calc_avg()
        self._calc_buquedingdu()

    def _calc_avg(self) -> None:
        try:
            self.avg = self.datas.sum() / self.datas.size
        except:
            self.avg = 0

    def get_avg(self) -> None:
        print('Avg of',self.name,'=',self.avg)

    def _calc_avg_divise_40(self)-> None:
        self.avg_divise_40 = self.avg / 40

    def get_avg_divise_40(self) -> None:
        print('Avg divise 40 of',self.name,'=',self.avg_divise_40)

    def _calc_sigma_t(self) -> None:
        if self.datas.size == 0: self.sigma_T = 0
        tmp_sum = 0
        for i in self.datas:
            tmp_sum += pow(self.avg-i,2)
        self.sigma_T = math.sqrt(tmp_sum/(self.datas.size*(self.datas.size-1)))

    def _calc_sigma_T(self) -> None:
        self.sigma_t = self.sigma_T/self.datas.size

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

    def _calc_avg_g(self) -> None:
        self.avg_g = 4*pow(math.pi,2)*self.L/pow(self.avg_divise_40,2)

    def _calc_sigma_g(self) -> None:
        self.sigma_g = self.avg_g*math.sqrt(math.pow(self.sigma_L/self.L,2)+4*pow(self.sigma_T/self.avg_divise_40,2))

    def print_calced_results(self) -> None:
        print('sigma_t of',self.name,'=',self.sigma_t)
        print('avg_t of',self.name,'=',self.avg)
        print('sigma_T of',self.name,'=',self.sigma_T)
        print('avg_divise_40 of',self.name,'=',self.avg_divise_40)
        print('avg_g of',self.name,'=',self.avg_g)
        print('sigma_g of',self.name,'=',self.sigma_g)
        print('g of',self.name,'=',self.avg_g,'±',self.sigma_g)


A40 = celiang(np.array([50.743,50.774,50.751,50.750,50.772,50.784,50.773,50.761],np.double),40,'40cm-5deg',0.04)
A60 = celiang(np.array([60.793,60.786,62.783,62.786,64.682,62.782,62.778,62.792],np.double),60,'60cm-5deg',0.04)
A70 = celiang(np.array([67.411,67.387,67.400,67.419,67.431,67.453,67.928,67.419],np.double),70,'70cm-5deg',0.04)
B40 = celiang(np.array([50.699,50.666,50.696,50.703,50.714,50.714,50.676,50.713],np.double),40,'40cm-3deg',0.04)
B60 = celiang(np.array([62.817,62.827,62.910,62.868,62.892,62.861,62.889,62.813],np.double),60,'60cm-3deg',0.04)
B70 = celiang(np.array([67.376,67.384,67.374,67.388,67.373,67.616,67.360,67.317],np.double),70,'70cm-3deg',0.04)


# A40 = celiang(np.array([51.267,51.281,51.290,51.276,51.271,51.272,51.283,51.270],np.double),40,'40cm-5deg',0.04)
# A60 = celiang(np.array([61.523,62.266,62.259,62.271,62.267,62.260,67.258,62.262],np.double),60,'60cm-5deg',0.04)
# A70 = celiang(np.array([67.328,67.321,67.331,67.329,67.326,67.330,67.324,67.326],np.double),70,'70cm-5deg',0.04)
# B40 = celiang(np.array([51.251,51.224,51.220,51.262,51.226,51.256,51.206,51.232],np.double),40,'40cm-3deg',0.04)
# B60 = celiang(np.array([62.196,62.232,62.258,62.260,62.237,62.242,62.257,62.243],np.double),60,'60cm-3deg',0.04)
# B70 = celiang(np.array([67.419,67.407,67.393,67.396,67.393,67.398,67.406,67.402],np.double),70,'70cm-3deg',0.04)

all_items = [A40,A60,A70,B40,B60,B70]

for item in all_items:
    # item.print_buquedingdu()
    item.print_calced_results()
    print()


