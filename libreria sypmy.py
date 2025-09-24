# -*- coding: utf-8 -*-
"""
Created on Tue Aug 19 07:34:20 2025

@author: AULA
"""

import sympy as sp
x = sp.symbols("x")
x*2
y = sp.symbols("y")
x+y**2
a=2
a+x
M = sp.Matrix([[1,2,3],[4,5,6],[7,8,9]])

M

M.T

N = sp.Matrix([[0,1,2],[0,1,0],[0,1,0]])


M+N
M-N

I3= sp.eye(3)

I3

M@N

M.inv()

M.det()

A = sp.Matrix([[1,0,1],[2,3,4],[4,5,6]])
A.det()
A.inv()


#OPERACIONES POR FILA

M[0,0]
M[2,2]

M[0:]

sp.latex(M)

M[0,:]

M[:,2]

NM=M.elementary_row_op("n->kn",row=0, k=2,);NM

NM=M.elementary_row_op("n<->m",row1=0, row2=1,);NM
NM=M.elementary_row_op("n->n+km", k=-4, row1 = 1, row2 = 0);NM



