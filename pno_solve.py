import math


#in this file we solve method pho

"""
Метод визначення зон ризику при виникненні ударної хвилі;
Метод визначення зон ризику від теплового випромінювання, яке виникає під час пожежі проливу нафтопродуктів;
Метод визначення зон ризику при виникненні «вогняної кулі».
"""

#Метод визначення зон ризику при виникненні ударної хвилі

#fuel

#a_93
k = 1
mk = 98.2
ak = 4.12311
bk = 664.976
ck = 221.695
qk = 43641000
q0 = 4520000
z = 0.1
p0 = 101.3
mv = 0.06

tvip = 55
temperature = 29
volume = 40
g = 9.81



fb = volume*1000*0.15
print("fb ", fb)
ph = 10**(ak-(bk/(ck+temperature)))
print("ph ", ph)
w = (10**-6)*math.sqrt(mk)*ph
print("w ", w)
m = w*fb*tvip
print("m ", m)
mpr = (qk/q0)*m*z
print("mpr ",mpr)

r = 0.01
while r != 0:
    mpr = 827.75
    p_delta = p0 * (((0.8 * mpr ** 0.33) / r) + ((3 * mpr ** 0.66) / r) + ((5 * mpr) / r))
    p_delta = round(p_delta, 3)

#    print(r)
    if p_delta <= 101 and p_delta > 99:
        r_100 = r

    if p_delta <= 51 and p_delta > 49:
        r_50 = r

    if p_delta <= 31 and p_delta > 29:
        r_30 = r

    if p_delta <= 10:
        r_10 = r
        break
    r += 0.1
print("r_10 ", r_10, "r_30 ", r_30, "r_50 ", r_50, "r_100 ", r_100)



#Метод визначення зон ризику від теплового випромінювання, яке виникає під час пожежі проливу нафтопродуктів;

