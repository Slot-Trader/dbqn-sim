"""Reproduce the values in Tables 2-5 and Figure 3 of the DBQN paper.  Usage: python3 calc.py"""
import math

print("Table 2: verification rounds k")
for p in (0.5, 0.25):
    print(f"  p={p}:", [math.ceil(math.log(1 / eps) / math.log(1 / (1 - p))) for eps in (1e-6, 1e-9)])

print("Table 3: Grover break-even (t_c = 1 ns, t_q = 1 ms)")
t_c, t_q = 1e-9, 1e-3
for overhead in (1, 10, 100, 1000):
    n_star = ((math.pi / 4) * overhead * t_q / t_c) ** 2
    print(f"  bk={overhead}: N*={n_star:.2e}, T={n_star * t_c:.3g} s ({n_star * t_c / 86400:.3g} days)")

print("Table 4: fidelity F^g")
for f in (0.86, 0.99, 0.999):
    print(f"  F={f}:", [f"{f ** g:.3g}" for g in (10, 100, 1000)])

print("Table 5: repeaterless bound over 0.2 dB/km fibre")
for km in (10, 50, 100, 200, 500, 1000):
    eta = 10 ** (-0.02 * km)
    bound = -math.log2(1 - eta) if eta > 1e-15 else eta / math.log(2)  # small-eta limit avoids rounding to 0
    print(f"  {km} km: eta={eta:.2g}, bound={bound:.3g}")

print("Figure 3: classical time at break-even, t_q/t_c = 1e6, constants omitted")
for a in (2, 4):
    print(f"  a={a}:", [f"{(bk * 1e6) ** (a / (a - 1)) * t_c:.3g} s" for bk in (1, 10, 100, 1000)])
