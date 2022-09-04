import math

neidan = 30.70
neidan_jiaobanqi = neidan + 2.15
shui = 62.33 - neidan_jiaobanqi
bing = 68.72 - neidan_jiaobanqi

c1 = 389
c2 = 389
c3 = 1800
c0 = 4180

T0 = 0
T1 = 0

T2 = 29.4
T3 = 6.8

L = (1/bing) * ((shui/1000)*c0 + (neidan_jiaobanqi/1000)*c1) * (T2 - T3) - c0*(T3) + c3*(T1)

print(L)