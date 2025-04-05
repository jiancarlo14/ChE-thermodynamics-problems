mass_kg = 1
delta_T_K = 10
pressure_bar = 1 
beta_per_deg_C_per1000 = (1.08, 0.81, 1.12, 0.94, 1.15, 1.65, 1.40, 1.35, 0.99, 1.49, 1.14, 1.05, 1.21)
kappa_per_bar_per100000 = (9.08, 4.53, 9.38, 7.45, 11.3, 18.65, 11.19, 11.32, 8.46, 12.14, 10.5, 8.96, 9.96)
spec_vol_L_per_kg = (0.951, 0.976, 0.792, 0.904, 1.285, 1.401, 1.265, 1.110, 1.157, 1.262, 0.628, 1.154, 0.672)

spec_vol_m3_per_kg = tuple(vol * 0.001 for vol in spec_vol_L_per_kg)

delta_V = tuple(vol * beta / 1000 * delta_T_K for vol, beta in zip(spec_vol_m3_per_kg, beta_per_deg_C_per1000))

# for dv in delta_V:
#     print(f"{dv:.2e} \\\\")

work_Pa_m3 = tuple(-pressure_bar*dv for dv in delta_V)

for work in work_Pa_m3:
    print(f"{work:.2e} \\\\")
