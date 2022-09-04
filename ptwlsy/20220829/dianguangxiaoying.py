import math
import numpy as np


class celiang():
    def __init__(self,datas:dict[str,float],name:str="") -> None:
        self.datas = datas
        self.name = name
        self.result = []
        self.fuck_out_result()

    def _calc_avg(self,data:list) -> float:
        try:
            tmp_sum = data.sum()
        except Exception:
            tmp_sum = sum(data)
        return tmp_sum/len(data)

    def _fuck_result(self) -> list[float]:
        for pair in self.datas:
            dying_light_M = []

            high_low = [abs(pair["U"][i]-pair["U"][i+1]) for i in range(len(pair["U"])-1)]
            half_high_low = [(pair["U"][i] + pair["U"][i + 2]) / 2 for i in range(len(pair["U"]) - 2)]

            if pair["I"][0] < pair["I"][1]:
                dying_light_M.append(pair["I"][1]/pair["I"][0])
                for i in range(1,len(pair["U"])-1,2):
                    dying_light_M.extend((pair["I"][i] / pair["I"][i - 1], pair["I"][i] / pair["I"][i + 1]))

            else:
                for i in range(0,len(pair["U"])-1,2):
                    dying_light_M.extend((pair["I"][i] / pair["I"][i - 1], pair["I"][i] / pair["I"][i + 1]))

                dying_light_M.append(pair["I"][-1]/pair["I"][-2])

            pair_result = {"high_low":high_low,"half_high_low":half_high_low,"dying_light_M":dying_light_M}
            self.result.append(pair_result)

        high_low_total = []
        for pair in self.result:
            high_low_total.extend(pair["high_low"])
        half_high_low_total = []
        for pair in self.result:
            half_high_low_total.extend(pair["half_high_low"])
        dying_light_M_total = []
        for pair in self.result:
            dying_light_M_total.extend(pair["dying_light_M"])


        # high_low_total = [355,324,370,340,380]
        # half_high_low_total = [320,320,320,315,320]
        # dying_light_M_total = [5.57,73,10,79,10]


        self.high_low_avg = self._calc_avg(list(high_low_total))
        self.half_high_low_avg = self._calc_avg(list(half_high_low_total))
        self.dying_light_M_avg = self._calc_avg(list(dying_light_M_total))

        self.high_low_Da = math.sqrt(sum(pow(i-self.high_low_avg,2) for i in high_low_total)/len(high_low_total))
        self.half_high_low_Da = math.sqrt(sum(pow(i-self.half_high_low_avg,2) for i in half_high_low_total)/len(half_high_low_total))
        self.dying_light_M_Da = math.sqrt(sum(pow(i-self.dying_light_M_avg,2) for i in dying_light_M_total)/len(dying_light_M_total))

        self.high_low_Da_percent = self.high_low_Da / self.high_low_avg
        self.half_high_low_Da_percent = self.half_high_low_Da / self.half_high_low_avg
        self.dying_light_M_Da_percent = self.dying_light_M_Da / self.dying_light_M_avg

    def fuck_out_result(self) -> None:
        self._fuck_result()
        for index,pair in enumerate(self.result):
            print(f"-----{index}-----")
            print(f"high_low = {pair['high_low']}")
            print(f"half_high_low = {pair['half_high_low']}")
            print(f"dying_light_M = {pair['dying_light_M']}")

        print("-----Average-----")
        print(f"high_low_avg = {self.high_low_avg}")
        print(f"half_high_low_avg = {self.half_high_low_avg}")
        print(f"dying_light_M_avg = {self.dying_light_M_avg}")

        print("-----Da-----")
        print(f"high_low_Da = {self.high_low_Da}")
        print(f"half_high_low_Da = {self.half_high_low_Da}")
        print(f"dying_light_M_Da = {self.dying_light_M_Da}")

        print("-----Percent-----")
        high_low_Da_percent_split =  str(self.high_low_Da_percent*100).split('.')
        print(f"high_low_Da_percent = {high_low_Da_percent_split[0]}.{high_low_Da_percent_split[1][:2]}%")

        half_high_low_Da_percent_split =  str(self.half_high_low_Da_percent*100).split('.')
        print(f"half_high_low_Da_percent = {half_high_low_Da_percent_split[0]}.{half_high_low_Da_percent_split[1][:2]}%")

        dying_light_M_Da_percent_split =  str(self.dying_light_M_Da_percent*100).split('.')
        print(f"dying_light_M_Da_percent = {dying_light_M_Da_percent_split[0]}.{dying_light_M_Da_percent_split[1][:2]}%")
        print()

class drawer():
    def __init__(self,datas:dict[str,float],name:str) -> None:
        self.datas = datas
        self.name = name

    def _calc_avg(self,data:list) -> float:
        try:
            tmp_sum = data.sum()
        except Exception:
            tmp_sum = sum(data)
        return tmp_sum/len(data)

    def _fuck_result(self) -> list[float]:
        self.alpha = []
        self.beta = []
        self.t = []

    def fuck_out_result(self) -> None:
        self._fuck_result()
        print('t=',self.beta)
        print('t=',self.t)
        print()

result_list = [
    celiang(
        datas=[
                {
                    "I":[0.032,0.682,0.030,0.693,0.031],
                    "U":[-906,-311,-24,-396,-734],
                },
                {
                    "I":[0.040,0.688,0.030,0.687,0.029],
                    "U":[-870,-311,-30,400,730],
                },
                {
                    "I":[0.037,0.688,0.033,0.688,0.033],
                    "U":[-900,-307,-20,400,730],
                },
                {
                    "I":[0.648,0.519,0.663,0.636,0.677],
                    "U":[-870,-413,22,328,645],
                },
                {
                    "I":[0.650,0.517,0.663,0.636,0.678],
                    "U":[-872,-411,23,330,640],
                },
        ]
    ),
    drawer(
        datas={
            "calcer":[
            ],
        },
        name="",
    ),
]