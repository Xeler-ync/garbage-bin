import math


def opt_lisaru(C:float,D:float,S:float) -> float:
    move = 0
    if S > 90:
        print(f"C = {C}, D = {D}, S = {S}, calc = {180-(math.asin(C/D)/math.pi*180)}, percent = {math.fabs((180-(math.asin(C/D)/math.pi*180)-S)/S)*100}%")
    else:
        print(f"C = {C}, D = {D}, S = {S}, calc = {math.asin(C/D)/math.pi*180}, percent = {math.fabs((math.asin(C/D)/math.pi*180-S)/S)*100}%")

def opt_shuangzong(xT:float,x:float,S:float) -> float:
    print(f"x = {x}, xT = {xT}, S = {S}, calc = {(x/xT)*360}, percent = {math.fabs((((x/xT)*360)-S)/S)*100}%")


# ync
lisaru = [
    [1.4,4.04,20],
    [2.0,4.06,30],
    [2.8,4.08,45],
    [3.06,4.06,50],
    [3.42,4.06,60],
    [4.0,4.1,90],
    [3.48,4.1,120],
    [2.82,4.1,135],
    [2.0,4.1,150],
    [0.0,4.1,180],
    [3.84,4.1,45],
    [2.8,4.08,45],
    [2.84,4.08,45]
]

shuangzong = [
    [1000,56,20],
    [1000,84,30],
    [1000,128,45],
    [1000,136,50],
    [1000,164,60],
    [1000,252,90],
    [1000,332,120],
    [1000,376,135],
    [1000,416,150],
    [1000,500,180],
    [668,84,45],
    [500,64,45],
    [400,52,45]
]




## xj
# lisaru = [
#     [1.440,4.04,20],
#     [1.960,4.02,30],
#     [2.8,4.04,45],
#     [3.06,4.04,50],
#     [3.46,4.02,60],
#     [4.02,4.02,90],
#     [3.44,4.02,120],
#     [2.88,4.02,135],
#     [2.06,4.02,150],
#     [0.0,4.02,180],
#     [2.8,4.02,45],
#     [2.82,4.02,45],
#     [2.82,4.02,45]
# ]

# shuangzong = [
#     [1000,60,20],
#     [1000,84,30],
#     [1000,132,45],
#     [1000,144,50],
#     [1000,172,60],
#     [1000,264,90],
#     [1000,348,120],
#     [1000,380,135],
#     [1000,432,150],
#     [1000,512,180],
#     [668,88,45],
#     [500,64,45],
#     [400,52,45]
# ]

print("lisaru")
for i in lisaru:
    opt_lisaru(i[0],i[1],i[2])

print()

print("shuangzong")
for i in shuangzong:
    opt_shuangzong(i[0],i[1],i[2])