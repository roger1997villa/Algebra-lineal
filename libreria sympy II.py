# -*- coding: utf-8 -*-
"""
Created on Tue Aug 19 08:18:37 2025

@author: AULA
"""

import sympy as sp


A = sp.Matrix([[3,4,5,6],[7,8,9,1],[2,3,4,5],[6,7,8,9]])

AB = A.elementary_row_op("n->kn", row=1, k=3); AB
AB = AB.elementary_row_op("n->n+km", k = -7, row1=1, row2=0);AB
AB = AB.elementary_row_op("n->kn", row=2, k=3); AB
AB = AB.elementary_row_op("n->n+km",k=-2, row1=2, row2=0 );AB
AB = AB.elementary_row_op("n->kn", row=3, k=3); AB
AB = AB.elementary_row_op("n->n+km",k=-6, row1=3, row2=0 );AB
AB = AB.elementary_row_op("n<->m", row1=1, row2=2); AB
AB = AB.elementary_row_op("n->n+km",k= 4, row1=2, row2=1);  AB
AB = AB.elementary_row_op("n->n+km",k= 3, row1=3, row2=1);  AB
