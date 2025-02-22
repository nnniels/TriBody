#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Feb 22 09:17:41 2025

@author: niels
"""

import numpy as np


def Barycenter(sv, m1, m2, m3):
    assert(sv.shape == (12, ))
    # get position
    x1, y1, x2, y2, x3, y3 = sv[:6]
    # CoM
    x = (m1*x1 + m2*x2 + m3*x3)/(m1+m2+m3)
    y = (m1*y1 + m2*y2 + m3*y3)/(m1+m2+m3)
    return np.array([x, y, x, y, x, y])


def BaryTime(sv, m1, m2, m3):
    bary0 = Barycenter(sv[:, 0], m1, m2, m3)
    barytime = []
    for state in sv.T :
        bary = Barycenter(state, m1, m2, m3)
        delta = bary-bary0
        state[:6] -= delta[:]
        barytime.append(bary[0:2])
    barytime = np.array(barytime)
    return barytime
