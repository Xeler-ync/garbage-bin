import math
from scipy import optimize
import numpy as np
import  matplotlib.pyplot as plt
import matplotlib

matplotlib.rcParams['font.family'] = 'FangSong'
matplotlib.rcParams['font.size'] = 15
plt.rcParams['axes.unicode_minus'] = False

g = 9.81
D1 = 3.474/100
D2 = 3.306/100

# surface tension
s_st = 72.8/1000
y_st = 22.3/1000
g_st = 63.3/1000

def get_avg(arr):
    return sum(arr) / len(arr)

def residuals(p):
    k, b = p
    return y_k - (k * x_k + b)

x_k = np.array([i/1000*g for i in [0.5, 1, 1.5, 2, 2.5, 3, 3.5]])
y_k = np.array([i/1000 for i in [8.6, 10.7, 25.7, 34.2, 42.3, 51.2, 59.6]])


r = optimize.leastsq(residuals,[1,0])
k, b = r[0]

X=np.linspace(0,4/100,100)
plt.plot(X,k*X+b,label=u"拟合直线")
plt.plot(x_k,y_k,"og",label=u"原始数据")
plt.legend()
plt.ylabel("U/V")
plt.xlabel("F/N")
plt.title(u"灵敏度k")
plt.show()
plt.savefig(f'用拉脱法测定液体表面张力系数')

print(f"k = {k}\nb = {b}")
print()

s_U1 = np.array([i/1000 for i in [20.3, 21.1, 21.5, 21.0, 20.3]])
s_U2 = np.array([i/1000 for i in [-7.1, -5.2, -5.4, -5.3, -5.2]])
s_dU = s_U1 - s_U2
s_F = s_dU / k
s_alpha = s_F / (math.pi * (D1 + D2))
s_alpha_avg = get_avg(s_alpha)

print(f"s_U1 = {s_U1}")
print(f"s_U2 = {s_U2}")
print(f"s_dU = {s_dU}")
print(f"s_F = {s_F}")
print(f"s_alpha = {s_alpha}")
print(f"s_alpha_avg = {s_alpha_avg}")
print(f"s_alpha_avg_d = {(s_st - s_alpha_avg) / s_st}")
print()


y_U1 = np.array([i/1000 for i in [1.2, 1.6, 1.6, 1.7, 1.6]])
y_U2 = np.array([i/1000 for i in [-6.9, -6.6, -6.6, -6.6, -6.6]])
y_dU = y_U1 - y_U2
y_F = y_dU / k
y_alpha = y_F / (math.pi * (D1 + D2))
y_alpha_avg = get_avg(y_alpha)

print(f"y_U1 = {y_U1}")
print(f"y_U2 = {y_U2}")
print(f"y_dU = {y_dU}")
print(f"y_F = {y_F}")
print(f"y_alpha = {y_alpha}")
print(f"y_alpha_avg = {y_alpha_avg}")
print(f"s_alpha_avg_d = {(y_st - y_alpha_avg) / y_st}")
print()


g_U1 = np.array([i/1000 for i in [16, 16.1, 16.4, 16.4, 16.3]])
g_U2 = np.array([i/1000 for i in [-7.3, -7.2, -7.2, -6.8, -7.2]])
g_dU = g_U1 - g_U2
g_F = g_dU / k
g_alpha = g_F / (math.pi * (D1 + D2))
g_alpha_avg = get_avg(g_alpha)

print(f"g_U1 = {g_U1}")
print(f"g_U2 = {g_U2}")
print(f"g_dU = {g_dU}")
print(f"g_F = {g_F}")
print(f"g_alpha = {g_alpha}")
print(f"g_alpha_avg = {g_alpha_avg}")
print(f"g_alpha_avg_d = {(g_st - g_alpha_avg) / g_st}")
print()
