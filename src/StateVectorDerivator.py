#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import numpy as np


""" Time derivative of state vector sv
    sv is [position, speed, mass]
    sv = [x1, y1, x2, y2, x3, y3,
          xdot1, ydot1 ...
          m1, m2, m3]
"""


def StateVectorDerivator(t, sv, m1=1, m2=1, m3=1, Tend=1):
    assert(sv.shape == (12, ))
    # get position
    x1, y1, x2, y2, x3, y3 = sv[:6]
    # get speeds
    vx1, vy1, vx2, vy2, vx3, vy3 = sv[6:]
    
    # compute distances
    d12 = np.sqrt( (x1-x2)**2 + (y1-y2)**2 )
    d13 = np.sqrt( (x1-x3)**2 + (y1-y3)**2 )
    d23 = np.sqrt( (x3-x2)**2 + (y3-y2)**2 )
    
    # directions
    f1to2 = np.array([x2-x1, y2-y1])
    f1to3 = np.array([x3-x1, y3-y1])
    f2to3 = np.array([x3-x2, y3-y2])

    # Gravitationnal constant
    G = 1 #6.67e-11
    
    # accelerations
    ax1, ay1 = G * (f1to2 * m2/d12**3  + f1to3 * m3/d13**3)
    ax2, ay2 = G * (-f1to2 * m1/d12**3 + f2to3 * m3/d23**3)
    ax3, ay3 = G * (-f1to3 * m1/d13**3 - f2to3 * m2/d23**3)

    svdot = np.array([vx1, vy1,
                      vx2, vy2,
                      vx3, vy3,
                      
                      ax1, ay1,
                      ax2, ay2,
                      ax3, ay3
                      ])
    return svdot*Tend


