from s13 import beta_per1000, kappa_per100000

P2 = tuple(1 + beta * (25-15) / kappa for beta, kappa in zip(beta_per1000, kappa_per100000) )

for P in P2:
    print(f"{P:.2f} \\\\")
