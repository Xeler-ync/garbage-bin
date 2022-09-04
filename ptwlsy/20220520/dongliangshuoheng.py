import math
import numpy as np


class celiang():
    # def __init__(self,datas:dict[np.array[float]],m1:float,m2:float,x1:float,x2:float,name:str,exp_type = 'tx') -> None: # m as gram, x as cm
    def __init__(self,datas,m1:float,m2:float,x1:float,x2:float,name:str,exp_type = 'tx') -> None: # m as gram, x as cm
        self.datas = datas
        self.v10 = datas['v10']
        self.v11 = datas['v11']
        self.v21 = datas['v21']
        self.m1 = m1/1000
        self.m2 = m2/1000
        self.name = name
        self.exp_type = exp_type
        self.fuck_out_result()

    def _calc_avg(self,data:list) -> float:
        if len(data) != 0:
            try:
                sum = data.sum()
            except:
                sum = 0
                for i in data:
                    sum += i
            return i/len(data)
        else:
            return 0

    def _fuck_result(self) -> list[float]:
        # self.v10 = np.array([i/self.m1 for i in self.datas['t10']])
        # self.v11 = np.array([i/self.m1 for i in self.datas['t11']])
        # self.v21 = np.array([i/self.m1 for i in self.datas['t21']])
        self.C = [self.m1*i/(self.m1*j+self.m2*k) for i,j,k in zip(self.v10,self.v11,self.v21)]
        self.dalta_Ek = [0.5*(self.m1*j*j+self.m2*k*k)-0.5*self.m1*i*i for i,j,k in zip(self.v10,self.v11,self.v21)]
        self.e = [(k-j)/i for i,j,k in zip(self.v10,self.v11,self.v21)]
        self.C_avg = np.array(self._calc_avg(self.C))
        self.delta_Ek_avg = np.array(self._calc_avg(self.dalta_Ek))
        self.e_avg = np.array(self._calc_avg(self.e))

    def fuck_out_result(self) -> None:
        self._fuck_result()
        print('name =',self.name)
        print('v10 =',self.v10)
        print('v11 =',self.v11)
        print('v21 =',self.v21)
        print('C =',self.C)
        print('delta_Ek =',self.dalta_Ek)
        print('e =',self.e)
        print('C_avg =',self.C_avg)
        print('delta_Ek_avg =',self.delta_Ek_avg)
        print('e_avg =',self.e_avg)
        print()

result_list = [
    celiang(
        datas={
            "v10": np.array([0.3690,0.4451,0.5068,0.3229,0.566]),
            "v11": np.array([0,0,0,0,0]),
            "v21": np.array([0.3628,0.4380,0.50,0.3181,0.5607])
        },
        m1=181.34,
        m2=181.95,
        x1=0.0,
        x2=0.0,
        name="完全弹性碰撞-质量相等"
    ),
    celiang(
        datas={
            "v10": np.array([0.4615,0.5780,0.7634,0.8671,0.8310]),
            "v11": np.array([-0.0731,-0.1024,-0.1468,-0.1777,-0.1712]),
            "v21": np.array([0.3650,0.4566,0.5976,0.66,0.6329])
        },
        m1=181.95,
        m2=276.9,
        x1=0.0,
        x2=0.0,
        name="完全弹性碰撞-质量不等"
    ),
    celiang(
        datas={
            "v10": np.array([0.5566,0.8264,0.4839,0.4335,0.4983]),
            "v11": np.array([0.2123,0.3077,0.1801,0.1715,0.1919]),
            "v21": np.array([0.2141,0.3109,0.1839,0.1721,0.1952])
        },
        m1=178.60,
        m2=273.55,
        x1=0.0,
        x2=0.0,
        name="完全非弹性碰撞-质量随便"
    )
]