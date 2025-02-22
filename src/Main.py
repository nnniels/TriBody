#!/usr/bin/env python3
# -*- coding: utf-8 -*-


from KnownSolutions import KnownSolutions
from StateVectorDerivator import StateVectorDerivator
from Solver import Solve
from ImageMaker import ImageMaker
import time

Neval = 1000
Solutions = [k for k in range(-15, 18, 1)]
Solutions = [17]


""" 
    BE AWARE
    This code runs a certain number of simulations, 
    and creates the corresponding animations.
    
    Each simulation takes up to a few seconds to complete.
    Each plot takes a few seconds to complete.
    Each animation takes up to ***several minutes*** to complete.
"""

for Solution in Solutions :
    t0 = time.time()
    t, sv, Neval = Solve(Solution, Neval)
    img = ImageMaker(sv, Neval, Solution)
    
    
    #img.Plot()
    img.Animation()
    print(f"-> done for solution {Solution}\n in {time.time()-t0}s\n")

