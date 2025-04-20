import numpy as np
import matplotlib.pyplot as plt
from sympy import symbols, lambdify
from scipy.constants import R

plt.rcParams['text.usetex'] = True
plt.rcParams['font.family'] = 'serif'

x = np.linspace(1*10**5, 20*10**5, 500)

# (a) Constant Volume
V_a = R*800/(6*10**5)
y_a = np.full(500, V_a)

# (b) Constant Temperature
P_b = symbols('P_b')
expr_b = R*800/(P_b)
V_b = lambdify(P_b, expr_b, 'numpy')

y_b = V_b(x)

# (c) Adiabatically
const = 6*10**5*V_a**(5/3)
P_c = symbols('P_c')
expr_c = (const/(P_c))**(3/5)
V_c = lambdify(P_c, expr_c, 'numpy')

y_c = V_c(x)

# PLOT
plt.plot(x, y_a, label="Constant Volume", color="blue")
plt.plot(x, y_b, label="Constant Temperature", color="green")
plt.plot(x, y_c, label="Adiabatically", color="red")

plt.ylabel(r"$V/\mathrm{m}^3\,\mathrm{mol}^{-1}$", fontsize=14)
plt.xlabel(r"$P/\mathrm{Pa}^{-1}$", fontsize=14)
plt.legend(fontsize=14)
plt.grid(True)
plt.show()

