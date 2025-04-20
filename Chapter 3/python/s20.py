import numpy as np
from scipy.constants import R
import sympy as sp
# from utils import ls
import matplotlib.pyplot as plt

R_bar = R*10**(-5)

# 1->2
p12 = sp.symbols("p12")
V12 = sp.lambdify(p12, R_bar*300/p12)

x12 = np.linspace(1,5,100)
y12 = V12(x12)

# 2->3
V1 = y12[0]
V2 = y12[-1]
V3 = V2
P3 = x12[0]*(V1/V2)**(7/5)
P2 = x12[-1]

x23 = [P2,P3]
y23 = np.full(2,y12[-1])

# 3->1
k31 = V1**(7/5)
p31 = sp.symbols("p31")
V31 = sp.lambdify(p31, (k31/p31)**(1/(7/5)))

x31 = np.linspace(P3,x12[0],100)
y31 = V31(x31)

# PLOT
plt.plot(x12,y12,label="Isothermal")
plt.plot(x23,y23,label="Isochoric")
plt.plot(x31,y31,label="Adiabatic")

plt.scatter(x12[0],y12[0],s=10,label="_nolegend_",facecolors="none",edgecolors="black")
plt.scatter(x12[-1],y12[-1],s=10,label="_nolegend_",facecolors="none",edgecolors="black")
plt.scatter(x31[0],y31[0],s=10,label="_nolegend_",facecolors="none",edgecolors="black")

plt.text(x12[0],y12[0]+0.0001,"State 1")
plt.text(x12[-1],y12[-1]+0.0001,"State 2")
plt.text(x31[0],y31[0]+0.0001,"State 3")

plt.rcParams['text.usetex'] = True
plt.rcParams['font.family'] = 'serif'
plt.xlabel(r"Pressure/$\mathrm{bar}$", fontsize=14)
plt.ylabel(r"Volume/$\mathrm{m}^3\mathrm{mol}^{-1}$", fontsize=14)

plt.grid()
plt.legend()
plt.show()

# ls(globals())
