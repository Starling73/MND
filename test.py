import math as mt
from pprint import pprint

from numpy.random import seed
from scipy.stats import t

x1_min = 20
x1_max = 70
x2_min = 25
x2_max = 65
x3_min = 25
x3_max = 35
m = 3
N = 4
print("x1_min = " + str(x1_min), "x2_min = " + str(x2_min), "x3_min = " + str(x3_min))
print("x1_max = " + str(x1_max), "x2_max = " + str(x2_max), "x3_max = " + str(x3_max))
print("")
y_min = 200 + round((x1_min + x2_min + x3_min) / 3)
y_max = 200 + round((x1_max + x2_max + x3_max) / 3)
print("y_min = " + str(y_min), "y_max = " + str(y_max))
print("")

mp = [["x0_ " + "x1_", "x2_ " + "x3_"],
      [1, -1, -1, -1],
      [1, -1, +1, +1],
      [1, +1, -1, +1],
      [1, +1, +1, -1]]
print("Матриця планування експерименту")
pprint(mp)
print("")
e1 = [rand.randint(y_min, y_max) for i in range(m)]
e2 = [rand.randint(y_min, y_max) for i in range(m)]
e3 = [rand.randint(y_min, y_max) for i in range(m)]
e4 = [rand.randint(y_min, y_max) for i in range(m)]
mt2 = [["x1 " + "x2 " + "x3 " + " Y1   " + "Y2   " + "Y3  "],
       [x1_min, x2_min, x3_min, e1],
       [x1_min, x2_max, x3_max, e2],
       [x1_max, x2_min, x3_max, e3],
       [x1_max, x2_max, x3_min, e4]]
print("Заповнена матриця планування")
pprint(mt2)
print("")
y1_ = sum(e1) / len(e1)
y2_ = sum(e2) / len(e2)
y3_ = sum(e3) / len(e3)
y4_ = sum(e4) / len(e4)
print("y1_=" + str(round(y1_, 3)) + " y2_=" + str(round(y2_, 3)) + " y3_=" + str(round(y3_, 3)) + " y4_=" + str(
    round(y4_, 3)))
print("")
mx1 = (mt2[1][0] + mt2[2][0] + mt2[3][0] + mt2[4][0]) / 4
mx2 = (mt2[1][1] + mt2[2][1] + mt2[3][1] + mt2[4][1]) / 4
mx3 = (mt2[1][2] + mt2[2][2] + mt2[3][2] + mt2[4][2]) / 4
my = (y1_ + y2_ + y3_ + y4_) / 4
print("mx1=" + str(round(mx1, 3)) + " mx2=" + str(round(mx2, 3)) + " mx3=" + str(round(mx3, 3)) + " my=" + str(
    round(my, 3)))
a1 = ((mt2[1][0] * y1_ + mt2[2][0] * y2_ + mt2[3][0] * y3_ + mt2[4][0] * y4_) / 4)
a2 = ((mt2[1][1] * y1_ + mt2[2][1] * y2_ + mt2[3][1] * y3_ + mt2[4][1] * y4_) / 4)
a3 = ((mt2[1][2] * y1_ + mt2[2][2] * y2_ + mt2[3][2] * y3_ + mt2[4][2] * y4_) / 4)
print("a1=" + str(round(a1, 3)) + " a2=" + str(round(a2, 3)) + " a3=" + str(round(a3, 3)))
a11 = (mt2[1][0] * mt2[1][0] + mt2[2][0] * mt2[2][0] + mt2[3][0] * mt2[3][0] + mt2[4][0] * mt2[4][0]) / 4
a22 = (mt2[1][1] * mt2[1][1] + mt2[2][1] * mt2[2][1] + mt2[3][1] * mt2[3][1] + mt2[4][1] * mt2[4][1]) / 4
a33 = (mt2[1][2] * mt2[1][2] + mt2[2][2] * mt2[2][2] + mt2[3][2] * mt2[3][2] + mt2[4][2] * mt2[4][2]) / 4
print("a11=" + str(round(a11, 3)) + " a22=" + str(round(a22, 3)) + " a33=" + str(round(a33, 3)))
a12 = (mt2[1][0] * mt2[1][1] + mt2[2][0] * mt2[2][1] + mt2[3][0] * mt2[3][1] + mt2[4][0] * mt2[4][1]) / 4
a13 = (mt2[1][0] * mt2[1][2] + mt2[2][0] * mt2[2][2] + mt2[3][0] * mt2[3][2] + mt2[4][0] * mt2[4][2]) / 4
a23 = (mt2[1][1] * mt2[1][2] + mt2[2][1] * mt2[2][2] + mt2[3][1] * mt2[3][2] + mt2[4][1] * mt2[4][2]) / 4
print("a12=" + str(round(a12, 3)) + " a13=" + str(round(a13, 3)) + " a23=" + str(round(a23, 3)))
print("")
b0 = (lg.det([[my, mx1, mx2, mx3],
              [a1, a11, a12, a13],
              [a2, a12, a22, a23],
              [a3, a13, a23, a33]])) / (lg.det([[1, mx1, mx2, mx3],
                                                [mx1, a11, a12, a13],
                                                [mx2, a12, a22, a23],
                                                [mx3, a13, a23, a33]]))
b1 = (lg.det([[1, my, mx2, mx3],
              [mx1, a1, a12, a13],
              [mx2, a2, a22, a23],
              [mx3, a3, a23, a33]])) / (lg.det([[1, mx1, mx2, mx3],
                                                [mx1, a11, a12, a13],
                                                [mx2, a12, a22, a23],
                                                [mx3, a13, a23, a33]]))
b2 = (lg.det([[1, mx1, my, mx3],
              [mx1, a11, a1, a13],
              [mx2, a12, a2, a23],
              [mx3, a13, a3, a33]])) / (lg.det([[1, mx1, mx2, mx3],
                                                [mx1, a11, a12, a13],
                                                [mx2, a12, a22, a23],
                                                [mx3, a13, a23, a33]]))
b3 = (lg.det([[1, mx1, mx2, my],
              [mx1, a11, a12, a1],
              [mx2, a12, a22, a2],
              [mx3, a13, a23, a3]])) / (lg.det([[1, mx1, mx2, mx3],
                                                [mx1, a11, a12, a13],
                                                [mx2, a12, a22, a23],
                                                [mx3, a13, a23, a33]]))
print("b0=" + str(round(b0, 3)) + " b1=" + str(round(b1, 3)) + " b2=" + str(round(b2, 3)) + " b3=" + str(round(b3, 3)))
Y1 = b0 + b1 * mt2[1][0] + b2 * mt2[1][1] + b3 * mt2[1][2]
Y2 = b0 + b1 * mt2[2][0] + b2 * mt2[2][1] + b3 * mt2[2][2]
Y3 = b0 + b1 * mt2[3][0] + b2 * mt2[3][1] + b3 * mt2[3][2]
Y4 = b0 + b1 * mt2[4][0] + b2 * mt2[4][1] + b3 * mt2[4][2]
print("y1_=" + str(round(y1_, 3)) + " y2_=" + str(round(y2_, 3)) + " y3_=" + str(round(y3_, 3)) + " y4_=" + str(
    round(y4_, 3)))
print("Y1 =" + str(round(y1_, 3)) + " Y2 =" + str(round(Y2, 3)) + " Y3 =" + str(round(Y3, 3)) + " Y4 =" + str(
    round(Y4, 3)))
if round(y1_, 3) == round(Y1, 3) and round(y2_, 3) == round(Y2, 3) and round(y3_, 3) == round(Y3, 3) and round(y4_,
                                                                                                               3) == round(
        Y4, 3):
    print("\033[1m\033[30m\033[42m{}\033[0m".format("Перевірка пройшла успішно, значення співпадають"))
print("")
d_y1 = (((e1[0] - y1_) ** 2) + ((e1[1] - y1_) ** 2) + ((e1[2] - y1_) ** 2)) / 3
d_y2 = (((e2[0] - y2_) ** 2) + ((e2[1] - y2_) ** 2) + ((e2[2] - y2_) ** 2)) / 3
d_y3 = (((e3[0] - y3_) ** 2) + ((e3[1] - y3_) ** 2) + ((e3[2] - y3_) ** 2)) / 3
d_y4 = (((e4[0] - y4_) ** 2) + ((e4[1] - y4_) ** 2) + ((e4[2] - y4_) ** 2)) / 3
print("d_y1=" + str(round(d_y1, 3)) + " d_y2=" + str(round(d_y2, 3)) + " d_y3=" + str(round(d_y3, 3)) + " d_y4=" + str(
    round(d_y4, 3)))
Gp = max(d_y1, d_y2, d_y3, d_y4) / (d_y1 + d_y2 + d_y3 + d_y4)
f1 = m - 1
f2 = N
print("f1 = " + str(f1))
print("f2 = " + str(f2))
GT = 0.7679
if Gp < GT:
    print("\033[1m\033[30m\033[43mGp={} < GT={} – Дисперсія однорідна\033[0m".format(round(Gp, 3), GT))
print("")
S2b = (d_y1 + d_y2 + d_y3 + d_y4) / N
S2bs = (S2b) / (N * m)
Sbs = mt.sqrt(S2bs)
print("S2b=" + str(round(S2b, 5)) + " S2bs=" + str(round(S2bs, 5)) + " Sbs=" + str(round(Sbs, 5)))
bi0 = (y1_ * mp[1][0] + y2_ * mp[2][0] + y3_ * mp[3][0] + y4_ * mp[4][0]) / 4
bi1 = (y1_ * mp[1][1] + y2_ * mp[2][1] + y3_ * mp[3][1] + y4_ * mp[4][1]) / 4
bi2 = (y1_ * mp[1][2] + y2_ * mp[2][2] + y3_ * mp[3][2] + y4_ * mp[4][2]) / 4
bi3 = (y1_ * mp[1][3] + y2_ * mp[2][3] + y3_ * mp[3][3] + y4_ * mp[4][3]) / 4
print("bi0=" + str(round(bi0, 3)) + " bi1=" + str(round(bi1, 3)) + " bi2=" + str(round(bi2, 3)) + " bi3=" + str(
    round(bi3, 3)))
t0 = abs(bi0) / Sbs
t1 = abs(bi1) / Sbs
t2 = abs(bi2) / Sbs
t3 = abs(bi3) / Sbs
print("t0=" + str(round(t0, 3)) + " t1=" + str(round(t1, 3)) + " t2=" + str(round(t2, 3)) + " t3=" + str(round(t3, 3)))
print("")
print("\033[1m\033[4mКритерій Стюдента по методичці\033[0m")
f3 = f1 * f2
print("f3 = " + str(f3))
t_tab = 2.306
print("T_tab = {!s}".format(t_tab))
if t0 > t_tab:
    print(" t0>t_tab")
if t3 > t_tab:
    print(" t3>t_tab")
if t1 < t_tab:
    print(" t1<t_tab")
if t2 < t_tab:
    print(" t2<t_tab")
print("")
print("b1, b2 коефіцієнти рівняння регресії приймаємо незначними \nпри рівні значимості 0.05,(виключаються з рівняння)")
print("")
print("\033[1m\033[4mКритерій Стюдента через Scipy.stats.t.ppf\033[0m")
seed(1)
alpha = 0.05
df = len(e1) + len(e2) + len(e3) + len(e4) - 4  # Число степеней свободы
cv = t.ppf(1.0 - alpha / 2, df)  # Критическое значение
print("CV = {!s}, df = {!s}".format(cv, df))
if t0 > cv:
    print(" t0>cv")
if t3 > cv:
    print(" t3>cv")
if t1 < cv:
    print(" t1<cv")
if t2 < cv:
    print(" t2<cv")
print("")
print("b1, b2 коефіцієнти рівняння регресії приймаємо незначними \nпри рівні значимості 0.05,(виключаються з рівняння)")

y1_fin = b0 + b3 * mt2[1][2]
y2_fin = b0 + b3 * mt2[2][2]
y3_fin = b0 + b3 * mt2[3][2]
y4_fin = b0 + b3 * mt2[4][2]
print("y1_fin=" + str(round(y1_fin, 3)) + " y2_fin=" + str(round(y2_fin, 3)) + " y3_fin=" + str(
    round(y3_fin, 3)) + " y4_fin=" + str(round(y4_fin, 3)))
d = 2
f4 = N - d
S2ad = (m / N - d) * ((y1_fin - y1_) ** 2 + (y2_fin - y2_) ** 2 + (y3_fin - y3_) ** 2 + (y4_fin - y4_) ** 2)
Fp = S2ad / S2b
FT = 4.5
if Fp < FT:
    print(
        "\033[1m\033[30m\033[43mFp={} < FT={} – рівняння регресії неадекватно оригіналу при рівні значимості 0.05\033[0m".format(
            round(Fp, 3), FT))
