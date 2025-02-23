#!/usr/bin/env python3
# -*- coding: utf-8 -*-


from KnownSolutions import KnownSolutions
from StateVectorDerivator import StateVectorDerivator
from Solver import Solver
from ImageMaker import ImageMaker
import time

Neval = 1000

# the initial conditions you want to solve the problem for
Solutions = [k for k in range(-15, 18, 1)]
Solutions = [17]


""" 
    BE AWARE
    This code runs a certain number of simulations, 
    and creates the corresponding animations.
    
    Each simulation takes up to a few seconds to complete for ~400 evals.
    Each plot takes a few seconds to complete.
    Each animation takes up to ***several minutes*** to complete.
"""

for Solution in Solutions :
    # time execution
    t0 = time.time()
    # create solver and solve problem
    sol = Solver()
    t, sv, Neval = sol.Solve(Solution, Neval, periods=0.6)
    print(f"-> solved {Solution}\n in {time.time()-t0}s\n")
    
    # create plots and animations maker
    img = ImageMaker(sv, Neval, Solution)
    
    # this is fast and sufficient to check correct solving
    img.Plot()
    # this can take a looooong time
    img.Animation()
    # all done !
    print(f"-> done for solution {Solution}\n in {time.time()-t0}s\n")

