# -*- coding: utf-8 -*-
"""
Created on Tue Sep 23 19:19:13 2025

@author: roger
"""

import numpy as np

# --- Punto 15: Determinantes ---
A = np.array([[-5, 3],
              [ 4, 2]])

B = np.array([[2, -1, 0],
              [4,  3, 2],
              [3,  0, 1]])

C = np.array([[1, 2, 3],
              [2, 3, 4],
              [3, 4, 5]])

D = np.array([[1, 0, 3],
              [2, 0, 4],
              [3, 1, 5]])

# Determinantes
det_A = np.linalg.det(A)
det_B = np.linalg.det(B)
det_C = np.linalg.det(C)
det_D = np.linalg.det(D)

print("Punto 15 - Determinantes:")
print(f"det(A) = {det_A:.0f}")
print(f"det(B) = {det_B:.0f}")
print(f"det(C) = {det_C:.0f}")
print(f"det(D) = {det_D:.0f}")

# Verificación propiedad det(AB) = det(A)*det(B) con una matriz Bp
Bp = np.array([[1, 2],
               [3, 4]])
product_det = np.linalg.det(A @ Bp)
separate_det = np.linalg.det(A) * np.linalg.det(Bp)

print("\nVerificación de la propiedad con A y Bp:")
print("Bp =\n", Bp)
print(f"det(A @ Bp) = {product_det:.0f}")
print(f"det(A)*det(Bp) = {separate_det:.0f}")

# --- Punto 16: Matrices casi singulares ---
E = np.array([[1, 1],
              [1, 1.0001]])

F = np.array([[1, 1],
              [1, 1]])

det_E = np.linalg.det(E)
det_F = np.linalg.det(F)

print("\nPunto 16 - Matrices casi singulares:")

if abs(det_E) > 1e-12:
    print(f"det(E) = {det_E:.10f}  -> invertible")
else:
    print(f"det(E) = {det_E:.10f}  -> no invertible")

if abs(det_F) > 1e-12:
    print(f"det(F) = {det_F:.10f}  -> invertible")
else:
    print(f"det(F) = {det_F:.10f}  -> no invertible")



