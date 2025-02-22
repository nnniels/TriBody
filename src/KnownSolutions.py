#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import numpy as np


def Newtonian(p1, p2):
    inits = [-1, 0, 1, 0, 0, 0, p1, p2, p1, p2, -2*p1, -2*p2]
    return inits

def KnownSolutions(SolNumber):
    # solution 1 to 17 found on github
    if SolNumber == 0:
        print("circle solution")
        r0 = 1
        m = 1
        G = 1
        beta = 2*np.pi/3
        alpha = (np.pi - beta) / 2
        L2 = (r0*(1-np.cos(beta)))**2 + (r0*np.sin(beta))**2
        a1x = 2*np.cos(alpha)*m*G/L2
        v1x = 0
        v1y = np.sqrt(a1x*r0)

        v2x = -v1y*np.sin(beta)
        v2y = v1y*np.cos(beta)

        v3x = -v1y*np.sin(2*beta)
        v3y = v1y*np.cos(2*beta)

        x1 = r0
        y1 = 0
        x2 = r0*np.cos(beta)
        y2 = r0*np.sin(beta)
        x3 = x2
        y3 = -y2
        inits = [x1, y1, x2, y2, x3, y3, v1x, v1y, v2x, v2y, v3x, v3y]
        tend = 2*np.pi*r0 / v1y

    
    
    elif SolNumber == -1:
        print("eight")
        tend = 6.32
        p1 = 0.347111
        p2 = 0.53728
        inits = Newtonian(p1, p2)
        
    elif SolNumber == -2:
        print("butterfly I")
        tend = 6.23
        p1 = 0.306893
        p2 = 0.12551
        inits = Newtonian(p1, p2)
    
    elif SolNumber == -3:
        print("butterfly II")
        tend = 7.0039
        p1 = 0.39295
        p2 = 0.09758
        inits = Newtonian(p1, p2)
        
    elif SolNumber == -4:
         print("bumblebee")
         tend = 63.5345
         p1 = 0.18428
         p2 = 0.058719
         inits = Newtonian(p1, p2)
         
    elif SolNumber == -5:
         print("moth I")
         tend = 14.8939
         p1 = 0.46444
         p2 = 0.39606
         inits = Newtonian(p1, p2)
    
    elif SolNumber == -6:
         print("butterfly III")
         tend = 13.8658
         p1 = 0.40592
         p2 = 0.23016
         inits = Newtonian(p1, p2)
    
    elif SolNumber == -7:
         print("moth III")
         tend = 25.8406
         p1 = 0.38344
         p2 = 0.37736
         inits = Newtonian(p1, p2)
    
    elif SolNumber == -8:
         print("goggles")
         tend = 10.4668
         p1 = 0.08330
         p2 = 0.12789
         inits = Newtonian(p1, p2)
        
    elif SolNumber == -9:
         print("butterfly IV")
         tend = 79.4759
         p1 = 0.350112
         p2 = 0.07934
         inits = Newtonian(p1, p2)
    
    elif SolNumber == -10:
         print("dragonfly")
         tend = 21.2710
         p1 = 0.08058
         p2 = 0.58884
         inits = Newtonian(p1, p2)
    
    elif SolNumber == -11:
         print("yarn")
         tend = 55.5018
         p1 = 0.55906
         p2 = 0.34919
         inits = Newtonian(p1, p2)
    
    elif SolNumber == -12:
         print("yinyang Ia")
         tend = 17.3284
         p1 = 0.51394
         p2 = 0.30474
         inits = Newtonian(p1, p2)
    
    elif SolNumber == -13:
         print("yinyang Ib")
         tend = 10.9626
         p1 = 0.28270
         p2 = 0.32721
         inits = Newtonian(p1, p2)
    
    elif SolNumber == -14:
         print("yinyang IIa")
         tend = 55.7898
         p1 = 0.41682
         p2 = 0.33033
         inits = Newtonian(p1, p2)
         
    elif SolNumber == -15:
         print("yinyang IIb")
         tend = 54.2076 
         p1 = 0.41734
         p2 = 0.31310
         inits = Newtonian(p1, p2)        

    elif SolNumber == 1:
        # Triple rings lined up
        print('Triple rings lined up solution returned.')
        inits = [
            -0.0347,
            1.1856,
            0.2693,
            -1.0020,
            -0.2328,
            -0.5978,
            0.2495,
            -0.1076,
            0.2059,
            -0.9396,
            -0.4553,
            1.0471]
        tend = 2.9623

    elif SolNumber == 2:
        # Flower in circle (at last!)
        print('Flower in circle.')
        inits = [-0.602885898116520,
                 1.059162128863347e-1,
                 0.252709795391000,
                 1.058254872224370e-1,
                 -0.355389016941814,
                 1.038323764315145e-1,
                 0.122913546623784,
                 0.747443868604908,
                 -0.019325586404545,
                 1.369241993562101,
                 -0.103587960218793,
                 -2.116685862168820]
        tend = 2.246101255307486
    elif SolNumber == 3:
        # Classic montgomery 8
        print('Montgomery 8 returned.')
        inits = [-0.97000436,
                 0.24308753,
                 0.97000436,
                 -0.24308753,
                 0,
                 0,
                 -0.5*0.93240737,
                 -0.5*0.86473146,
                 -0.5*0.93240737,
                 -0.5*0.86473146,
                 0.93240737,
                 0.86473146]
        tend = 6.32

    elif SolNumber == 4:
        # Ovals with flourishes. Took a very long time!
        print('Ovals with flourishes. Takes very high tolerances to work.')
        inits = [
            0.716248295712871,
            0.384288553041130,
            0.086172594591232,
            1.342795868576616,
            0.538777980807643,
            0.481049882655556,
            1.245268230895990,
            2.444311951776573,
            -0.675224323690062,
            -0.962879613630031,
            -0.570043907205925,
            -1.481432338146543]
        tend = 8.094721472532424

    elif SolNumber == 5:
        # 3 diving into the middle
        print('Three diving into middle. Can tune velocity multiplier for more solutions.')
        initPos = [1, 0, -0.5, np.sqrt(3)/2, -0.5, -np.sqrt(3)/2]
        initVel = [0, 1, -np.sqrt(3)/2, -0.5,  np.sqrt(3)/2, -0.5]
        inits = initPos + initVel
        tend = 12

    elif SolNumber == 6:
        # Two ovals
        print('Two ovals (2 on one, 1 on other).')
        inits = [0.486657678894505,
                 0.755041888583519,
                 -0.681737994414464,
                 0.293660233197210,
                 -0.022596327468640,
                 -0.612645601255358,
                 -0.182709864466916,
                 0.363013287999004,
                 -0.579074922540872,
                 -0.748157481446087,
                 0.761784787007641,
                 0.385144193447218]
        tend = 4.012156415940929

    elif SolNumber == 7:
        # Oval,catface,starship
        print('Oval, catface, and starship.')
        inits = [0.536387073390469,
                 0.054088605007709,
                 -0.252099126491433,
                 0.694527327749042,
                 -0.275706601688421,
                 -0.335933589317989,
                 -0.569379585580752,
                 1.255291102530929,
                 0.079644615251500,
                 -0.458625997341406,
                 0.489734970329286,
                 -0.796665105189482]
        tend = 5.026055004808709

    elif SolNumber == 8:
        # 3 lined up ovals, but with extra phase
        print('3 lined-up ovals, but with extra phase.')
        inits = [0.517216786720872,
                 0.556100331579180,
                 0.002573889407142,
                 0.116484954113653,
                 -0.202555349022110,
                 -0.731794952123173,
                 0.107632564012758,
                 0.681725256843756,
                 -0.534918980283418,
                 -0.854885322576851,
                 0.427286416269208,
                 0.173160065733631]
        tend = 5.179484537709100

    elif SolNumber == 9:
        # Skinny pineapple
        print('Skinny pineapple.')
        inits = [
            0.419698802831451,
            1.190466261251569,
            0.076399621770974,
            0.296331688995343,
            0.100310663855700,
            -0.729358656126973,
            0.102294566002840,
            0.687248445942575,
            0.148950262064203,
            0.240179781042517,
            -0.251244828059670,
            -0.927428226977280]
        tend = 5.095053913455357
    elif SolNumber == 10:
        # Hand-in-hand-in-oval.
        print('Hand-in-hand-in-oval.')
        inits = [0.906009977920936,
                 0.347143444586515,
                 -0.263245299491018,
                 0.140120037699958,
                 -0.252150695248079,
                 -0.661320078798829,
                 0.242474965162160,
                 1.045019736387070,
                 -0.360704684300259,
                 -0.807167979921595,
                 0.118229719138103,
                 -0.237851756465475,]
        tend = 6.868155929188273
    elif SolNumber == 11:
        # Beauteliful loop-ended triangles inside an oval
        print('Beauteliful loop-ended triangles inside an oval.')
        inits = [1.666163752077218e-1,
                 -1.081921852656887e+1,
                 0.974807336315507e-1,
                 -0.545551424117481e+1,
                 0.896986706257760e-1,
                 -1.765806200083609e+1,
                 0.841202975403070,
                 0.029746212757039,
                 0.142642469612081,
                 -0.492315648524683,
                 -0.983845445011510,
                 0.462569435774018]
        tend = 3.820761325134286
    elif SolNumber == 12:
        # Lined-up 3 ovals with nested ovals inside. Looks like newton's
        # cradle type effect.
        print('Lined-up 3 ovals with nested ovals inside. Looks like newtons cradle type effect.')
        inits = [1.451145020734434,
                 -0.209755165361865,
                 -0.729818019566695,
                 0.408242931368610,
                 0.509179927131025,
                 0.050853900894748,
                 0.424769074671482,
                 -0.201525344687377,
                 0.074058478590899,
                 0.054603427320703,
                 -0.498827553247650,
                 0.146921917372517]
        tend = 3.550943103767421
    elif SolNumber == 13:
        # Oval and crossed triple loop
        print('Oval and crossed triple loop.')

        inits = [0.654504904492769,
                 1.135463234751087,
                 -0.008734462769570,
                 -1.481635584087405,
                 -0.487782115417060,
                 0.236845409927442,
                 0.294339951803385,
                 -0.605376046698418,
                 0.038678643994549,
                 0.434105189236202,
                 -0.333018595797923,
                 0.171270857462206]
        tend = 5.377356578372074

    elif SolNumber == 14:
        # Most complicated sqigglies I've seen.
        # TODO: refine this one a bit
        print('Hard to describe squigglies PT1.')
        inits = [0.708322208567308,
                 0.473311928206857,
                 0.167739458699109,
                 -0.057913961029346,
                 -0.506578687023757,
                 -0.306825234531109,
                 0.824266639919723,
                 0.522197827478425,
                 -0.077017015655090,
                 -0.167288552679470,
                 -0.747249624264592,
                 -0.354909274799606]
        tend = 5.403010724273298

    elif SolNumber == 15:
        # Most complicated sqigglies I've seen.
        # TODO: refine this one a bit
        print('Hard to describe squigglies PT2.')

        inits = [0.865355422048074,
                 0.629488893636092,
                 0.085036793558805,
                 -0.013305780703954,
                 -0.090983494772311,
                 -0.892179296799402,
                 0.288687787606716,
                 0.171289709266963,
                 -0.220256752038501,
                 0.090375753070602,
                 -0.068431035568003,
                 -0.261665462337436]
        tend = 5.427986085939034

    elif SolNumber == 16:
        # Gear inside larger oval.
        print('Gear inside larger oval. VERY VERY STelifF WARNING. SEE CODE COMMENTS.')
        inits = [0.335476420318203,
                 -0.243208301824394,
                 0.010021708193205,
                 0.363104062311693,
                 0.030978712523174,
                 0.423035485079015,
                 1.047838171160758,
                 0.817404215288346,
                 -0.847200907807940,
                 -0.235749148338353,
                 -0.200636552532016,
                 -0.581655492859626]
        tend = 5.956867234319493
    elif SolNumber == 17:
        # 3 bouncing in a line
        print('3 bouncing in a line (almost).')
        inits = [-0.015958157830872,
                 0.829387672711051,
                 -0.023912093175726,
                 0.211010340157083,
                 -0.035305026035053,
                 -0.728544174709096,
                 0.008894140366887,
                 0.735934914230558,
                 -0.012693330102595,
                 -1.001493752025633,
                 0.003743585058501,
                 0.265560077637935]
        tend = 1.253088248568183

    else:
        print('Invalid solution number.')
        inits = None
        tend = None

    return inits, tend
