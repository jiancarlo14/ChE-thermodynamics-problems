from utils import ls
from scipy.constants import R
import numpy as np
import sympy as sp
import string

RBAR: float = R*10**(-5)

# a) Constant Temeprature
a_temperature_12 = 12/RBAR
a_p = sp.symbols("a_p")
a_volume_expr = sp.lambdify(a_p, RBAR*a_temperature_12/a_p)

a_pressure = np.linspace(1,12,100)
a_volume = a_volume_expr(a_pressure)

# b) Adiabatic, Constant Pressure
# P1 = 1,       V1 = 12
# P1.5 = 12     V1.5 = 
# P2 = 12       V2 = 1
b_p1i = sp.symbols("b_p1i")
b_volume_expr = sp.lambdify(b_p1i, ( 12**(5/3)/b_p1i )**(3/5) )

b_pressure_1i = np.linspace(1,12,100)
b_volume_1i = b_volume_expr(b_pressure_1i)

b_pressure_i2 = [12,12]
b_volume_i2 = [b_volume_1i[-1],1] 

b_pressure = np.concatenate((b_pressure_1i, b_pressure_i2))
b_volume = np.concatenate((b_volume_1i, b_volume_i2))

# c) Adiabatic, Constant Volume
# P1 = 1,       V1 = 12
# P1.5 =        V1.5 = 1
# P2 = 12       V2 = 1
c_p = sp.symbols("c_p")
c_volume_expr = sp.lambdify(c_p, ( 1/c_p*12**(5/3) )**(3/5) )
p_i = 12**(5/3)

c_pressure_1i = np.linspace(1,p_i,100)
c_volume_1i = c_volume_expr(c_pressure_1i)

c_pressure_i2 = [c_pressure_1i[-1], 12]
c_volume_i2 = [1,1]

c_pressure = np.concatenate((c_pressure_1i, c_pressure_i2))
c_volume = np.concatenate((c_volume_1i, c_volume_i2))

ls(globals())

# d) Constant Volume, Constant Pressure
# P1 = 1,       V1 = 12
# P1.5 = 12     V1.5 = 12
# P2 = 12       V2 = 1
d_pressure = [1,12,12]
d_volume = [12,12,1]

# e) Constant Pressure, Constant Volume
# P1 = 1,       V1 = 12
# P1.5 = 1      V1.5 = 1
# P2 = 12       V2 = 1
e_pressure = [1,1,12]
e_volume = [12,1,1]


# PLOT
import matplotlib.pyplot as plt

plots_x = [
    a_pressure,
    b_pressure,
    c_pressure,
    d_pressure,
    e_pressure
]
plots_y = [
    a_volume,
    b_volume,
    c_volume,
    d_volume,
    e_volume
]

for i, y in enumerate(plots_y):
    lw = 2 + 1.5  # Increased line width
    ls = ["-", "--", ":", "-."][i % 4]
    colors = ["blue", "orange", "green", "red", "purple"]  # Distinct colors
    lbl = list(string.ascii_lowercase[:5])[i]
    plt.plot(plots_x[i], y, label=f"Path {lbl}", linestyle=ls, linewidth=lw, alpha=0.85, color=colors[i])

plt.rcParams['text.usetex'] = True
plt.rcParams['font.family'] = 'serif'
plt.xlabel(r"Pressure/$\mathrm{bar}$", fontsize=14)
plt.ylabel(r"Volume/$\mathrm{m}^3\mathrm{mol}^{-1}$", fontsize=14)
plt.scatter(a_pressure[0],a_volume[0],facecolors="none",edgecolors="black",s=50,label="_nolegend_")
plt.scatter(a_pressure[-1],a_volume[-1],facecolors="none",edgecolors="black",s=50,label="_nolegend_")
plt.text(a_pressure[0],a_volume[0]+0.2,"State 1",fontsize=14)
plt.text(a_pressure[-1],a_volume[-1]-0.35,"State 2",fontsize=14)

plt.grid()
plt.legend()
plt.show()

