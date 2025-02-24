#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from scipy.integrate import solve_ivp

import numpy as np



from KnownSolutions import KnownSolutions
from StateVectorDerivator import StateVectorDerivator

"""
    Solve a problem given a solution number.
    
    Solve :
        Take a Solution number, and find the corresponding initial conditions.
        Adjust the number of iterations based on the period of the solution.
        NB : the period is normalized to 1 by StateVectorDerivator, hence the Tspan
        
    Load/ Save :
        works on Linux system only.
        save and load .npy corresponding to the state vector.
        Use it to save time or export data to another code.
        if text=True, you can save the state vector as a text file.

"""
class Solver():
    def __init__(self):
        self.sv = np.zeros((1,1))
        self.Solution = 1000
        self.periods = 0
        return None
    
    def Solve(self, Solution, Neval=200, periods=1):
    
        m1, m2, m3 = 1, 1, 1
        sv0, Tend = KnownSolutions(Solution)
        if Tend is None :
            return None, None, None
        sv0 = np.array(sv0)
        print(f"Loaded initial conditions with period {Tend}")
        print(f"Created init state vector sv0 {sv0.shape}")
        #Teval = np.linspace(0, Tend, Neval)
        EvalMax = 10000
        if Tend < 4 :
            print(f"short orbit for {Solution}")
            Neval *= 1
        elif Tend < 16:
            print(f"medium orbit for {Solution}")
            Neval *= 2
        else :
            print(f"long orbit for {Solution}")
            Neval *= 5
        if Neval > EvalMax:
            print("corrected Neval")
            Neval = EvalMax
        
        Teval = np.linspace(0, 1.1*periods, Neval)
        Tspan = (Teval[0], Teval[-1])
        print(f"solving for {periods} period(s)")
        print("solving...")
        methods = ["LSODA", "DOP853"]
        solution = solve_ivp(StateVectorDerivator, Tspan, sv0, method=methods[0],
                             rtol=1e-5, atol = 1e-6,
                             t_eval=Teval, args=[m1,m2,m3,Tend])
    
        print("solved")
        t = solution.t
        sv = solution.y
        print(f"solution {sv.shape}")
        print({1: "Integration step failed.",
         0: "The solver successfully reached the end of tspan.",
         1: "A termination event occurred."}[solution.status])
        self.sv = sv
        self.Solution = Solution
        self.period = periods
        return t, sv, Neval
    
    def Save(self, text=False):
        directory, filename = self.__FileSystem()
        np.save(directory + filename, self.sv)
        if text : np.savetxt(directory+filename, self.sv)
        print(f"saved {filename}")
    
    def Load(self):
        directory, filename = self.__FileSystem()
        sv = np.load(directory + filename)
        print(f"loaded {filename}")
        self.sv = sv
        return sv
    
    
    def __FileSystem(self):
        directory = "../TrajectoryNPY/"
        filename ="trajectory_" + str(self.Solution) + "_p-" + str(self.periods)+".npy"
        return directory, filename
        


























