import numpy as np
import matplotlib.pyplot as plt
from sympy import symbols, lambdify
from scipy.constants import R

plt.rcParams['text.usetex'] = True
plt.rcParams['font.family'] = 'serif'

x = np.linspace(1, 10, 500)

# (a) Constant Volume
V_a = R*600/(8)
y_a = np.full(500, V_a)

# (b) Constant Temperature
P_b = symbols('P_b')
expr_b = R*600/(P_b)
V_b = lambdify(P_b, expr_b, 'numpy')

y_b = V_b(x)

# (c) Adiabatically
const = 8*V_a**(7/5)
P_c = symbols('P_c')
expr_c = (const/(P_c))**(5/7)
V_c = lambdify(P_c, expr_c, 'numpy')

y_c = V_c(x)

# PLOT
plt.plot(x, y_a, label="Constant Volume", color="blue")
plt.plot(x, y_b, label="Constant Temperature", color="green")
plt.plot(x, y_c, label="Adiabatically", color="red")

plt.ylabel(r"$V/\mathrm{m}^3\,\mathrm{mol}^{-1}$", fontsize=14)
plt.xlabel(r"$P/\mathrm{bar}^{-1}$", fontsize=14)
plt.legend(fontsize=14)
plt.grid(True)
plt.show()

