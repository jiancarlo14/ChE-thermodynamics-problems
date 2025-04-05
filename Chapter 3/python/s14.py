from s13 import mass_kg, kappa_per100000, spec_vol_m3


delta_V = tuple(-vol * kappa / 100000 * 99 for vol, kappa in zip(spec_vol_m3, kappa_per100000) )

# for dv in delta_V:
#     print(f"{dv:.2e} \\\\")

W = tuple(mass_kg * vol * kappa / 100000 / 2 * (100**2 - 1) for vol, kappa in zip(spec_vol_m3, kappa_per100000) )

# for w in W:
#     print(f"{w:.2e} \\\\")
