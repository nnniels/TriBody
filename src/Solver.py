#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from scipy.integrate import solve_ivp

import numpy as np



from KnownSolutions import KnownSolutions
from StateVectorDerivator import StateVectorDerivator


def Solve(Solution, Neval=200):

    m1, m2, m3 = 1, 1, 1
    sv0, Tend = KnownSolutions(Solution)
    if Tend is None :
        return None, None
    sv0 = np.array(sv0)
    print(f"Loaded solution of period {Tend}")
    print(f"Created init state vector sv0 {sv0.shape}")
    #Teval = np.linspace(0, Tend, Neval)
    
    if Tend < 4 :
        print(f"short orbit for {Solution}")
        Neval *= 1
    elif Tend < 16:
        print(f"medium orbit for {Solution}")
        Neval *= 2
    else :
        print(f"long orbit for {Solution}")
        Neval *= 5
    if Neval > 5000:
        print("corrected Neval")
        Neval = 5000
    
    Teval = np.linspace(0, 1.2, Neval)
    Tspan = (Teval[0], Teval[-1])
    
    print("solving...")
    solution = solve_ivp(StateVectorDerivator, Tspan, sv0, method='DOP853',
                         rtol=1e-3, atol = 1e-8,
                         t_eval=Teval, args=[m1,m2,m3,Tend])

    print("solved")
    t = solution.t
    sv = solution.y
    print(f"solution {sv.shape}")
    return t, sv, Neval

