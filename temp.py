# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import math

Nc = 100
λ = 1
s(0,0)*W = 0 
s(1,0)*W = Q(1,0) 
s(1,1)*W = Q(1,1) 

"number of cars parked at the upper floors"
def U(x):
    if x == 1:
        x = 0
    else:
        x = x
    return x

"number of cars parked at the lobby"
def L(x):
    if x == 1:
        x = 1
    else:
        x = x
    return x

"C: free cars"
for C in range(2,Nc):
    wT = s(C−1,U(C−1))*W 
    mincost = math.inf
    for u = 0 to C 
        if u = C 
            W(u) = 0 
        else 
            if u = U(C−1)
                W(u) = wT 
            else 
                w0 = s(C−1,u)*W 
                T = Time(C−1,u,U(C−1))
                Wu = w0−(w0−wT)*(1−exp(−λT))/(λT) 
        if u = 0
            Wl = 0 
        else 
            if u−1 = U(C−1) 
                Wl = wT 
            else 
                w(0) = s(C−1,u−1)*W 
                T = Time(C−1,u−1,U(C−1)) 
                Wl = w0−(w0−wT)*(1−exp(−λT))/(λT) 
        s(C,u)*W = Q(C−u,u)+s(C,u)*Pl*Wl + s(C,u)*Pu*Wu 
        if s(C,u)*W < mincost
            mincost = s(C,u)*W 
            U(C) = u
    L(C) =C−U(C) 
return L(Nc)
