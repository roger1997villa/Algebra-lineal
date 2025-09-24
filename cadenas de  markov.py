# -*- coding: utf-8 -*-
"""
Created on Mon Sep  8 21:08:08 2025

@author: roger
"""

import sympy as sp

# Definir matriz de transición
P = sp.Matrix([
    [0.8, 0.2, 0.05],
    [0.05, 0.75, 0.05],
    [0.15, 0.05, 0.9]
])

# Vector iniciales
x0_a = sp.Matrix([10000, 10000, 10000])
x0_b = sp.Matrix([0, 30000, 0])
x0_c = sp.Matrix([5000, 20000, 5000])

# Función para mostrar P^n y P^n * x
def mostrar_resultados(n, x0):
    Pn = P**n
    xn = Pn * x0
    print(f"\n--- Resultados para n={n} ---")
    sp.pprint(Pn, use_unicode=True)
    print("Distribución:", xn)

# Ejemplos como en el documento
for n in [5, 10, 15, 20, 25, 30, 35, 40, 45, 50]:
    mostrar_resultados(n, x0_a)

# Distribuciones para otros vectores iniciales
print("\n=== Caso x0 = (0,30000,0) ===")
for n in [5, 10, 15, 20, 25, 30, 35, 40, 45, 50]:
    mostrar_resultados(n, x0_b)

print("\n=== Caso x0 = (5000,20000,5000) ===")
for n in [5, 10, 15, 20, 25, 30, 35, 40, 45, 50]:
    mostrar_resultados(n, x0_c)

# ---------------------------
# Distribución estacionaria
# Resolver pi = P*pi con sum(pi)=1
pi = sp.symbols("pi1 pi2 pi3")
pi_vec = sp.Matrix(pi)

eqs = list(P.T * sp.Matrix(pi) - sp.Matrix(pi))
eqs.append(sum(pi) - 1)

sol = sp.solve(eqs, pi)
print("\nDistribución estacionaria (fracciones):")
print(sol)

# ---------------------------
# Segundo ejemplo (agencia renta)
P_renta = sp.Matrix([
    [0.8, 0.1, 0.1],
    [0.05, 0.75, 0.1],
    [0.15, 0.15, 0.8]
])

pi_r = sp.symbols("pi1 pi2 pi3")
eqs_r = list(P_renta.T * sp.Matrix(pi_r) - sp.Matrix(pi_r))
eqs_r.append(sum(pi_r) - 1)
sol_r = sp.solve(eqs_r, pi_r)
print("\nDistribución estacionaria para agencia de renta:")
print(sol_r)