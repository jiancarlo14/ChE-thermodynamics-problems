# units
# P in bar
# V in m3 per mol
# T in K

import matplotlib.pyplot as plt
# from utils import ls
import numpy as np
import sympy as sp
from scipy.constants import R

R_bar = R*10**(-5)
Cp = 7/2*R_bar
Cv = 5/2*R_bar

# 1 -> 2
p12 = sp.symbols( 'p12' )
V12 = sp.lambdify( p12, R_bar * 600 / p12 )

x12 = np.linspace( 10, 3, 100 )
y12 = V12(x12)

# 2 -> 3
V23 = y12[-1]

x23 = [ 3, 2 ]
y23 = np.full( 2, V23 )

# 3 -> 4
V3 = V23
V4 = ( x12[0] / 2 * ( y12[0] ) ** ( Cp / Cv ) ) ** ( Cv / Cp )

x34 = np.full( 2, 2 )
y34 = [ V3, V4 ]

# 4 -> 1
# constant: P * V ** ( Cp / Cv ) = k41
k41 = x12[0] * y12[0] ** ( Cp / Cv )
p41 = sp.symbols( "p41" )
V41 = sp.lambdify( p41, ( k41 / p41 ) ** ( Cv / Cp ) )

x41 = np.linspace( 2, 10, 100 )
y41 = V41(x41)

# ls(globals())

# Plot
plt.rcParams['text.usetex'] = True
plt.rcParams['font.family'] = 'serif'
plt.xlabel(r"Pressure/$\mathrm{bar}$", fontsize=14)
plt.ylabel(r"Volume/$\mathrm{m}^3\mathrm{mol}^{-1}$", fontsize=14)
plt.plot(x12, y12, label="Isothermal", color="purple") 
plt.plot(x23, y23, label="Isochoric", color="green")
plt.plot(x34, y34, label="Isobaric", color="blue")
plt.plot(x41, y41, label="Adiabatic", color="red")

plt.scatter(x12[0], y12[0], label="_nolegend_", facecolors='none', s=10, edgecolors='black' )
plt.scatter(x12[-1], y12[-1], label="_nolegend_", facecolors='none', s=10, edgecolors='black' )
plt.scatter(x34[0], y34[0], label="_nolegend_", facecolors='none', s=10, edgecolors='black' )
plt.scatter(x34[-1], y34[-1], label="_nolegend_", facecolors='none', s=10, edgecolors='black' )

plt.text(x12[0]+0.1, y12[0], "State 1",)
plt.text(x12[-1], y12[-1]+0.0001, "State 2", ) 
plt.text(x34[0], y34[0]+0.0001, "State 3", )
plt.text(x34[-1]+0.1, y34[-1], "State 4", )

plt.grid()
plt.legend()

plt.show()
