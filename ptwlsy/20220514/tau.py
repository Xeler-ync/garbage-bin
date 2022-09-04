import math


def get_experiment_tau(T_half:float) -> float:
    return T_half/math.log(2,math.e)

def opt_tau(T_half:float,C:float,R:float) -> None:
    print(f"R = {R}(k), C = {C}, T_half = {T_half}, tau_exp = {get_experiment_tau(T_half)}, tau_calc = {R*C*1000}, percent = {math.fabs(((R*C*1000)-get_experiment_tau(T_half))/get_experiment_tau(T_half))*100}%")

T_half_list = [
    [550, 0.211, 3.9],
    [68, 0.1, 1.0],
    [390, 0.2, 3.0],
    [370, 0.191, 2.65],
    [520, 0.26, 3.05],
    [220, 0.3, 1.050],
    [470, 0.4, 1.7],
    [500, 0.47, 1.6],
    [590, 0.4255, 2.0],
    [560, 0.4543, 1.49]
] # (miu)/s, (miu)F, k(oum),



# T_half_list = [
#     [15,0.01,2.0],
#     [7.6,0.01,1.0],
#     [21.2,0.01,3.0],
#     [28.4,0.01,4.0],
#     [35.6,0.01,5.0],
#     [72,0.1,1.0],
#     [140,0.1,2.0],
#     [220,0.1,3.0],
#     [280,0.1,4.0],
#     [340,0.1,5.0]
# ] # (miu)/s, (miu)F, k(oum),

for i in T_half_list:
    opt_tau(i[0],i[1],i[2])