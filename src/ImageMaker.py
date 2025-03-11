#!/usr/bin/env python3
# -*- coding: utf-8 -*-


import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation


"""
    ImageMaker is a class that plots the state vector, and create an animation
    of the trajectory.
    
    On initialisation : 
        load the state vector sv and the number of points.
    
    On Animation and Plot : 
        the trajectory is scaled to fit in a 4 by 4 graph.
    
    Alphas and Width :
        functions to shape the tail of the planets.
        
    update_line :
        internal use for the matplotlib.animation.animation thing.
        Basically return the positions of the planets and tails at a given frame.


"""
class ImageMaker():
    def __init__(self, sv, SolutionNumber):
        self.sv = sv
        _, self.Neval = sv.shape
        self.sol = SolutionNumber
        self.PlanetColor = ["darkorange", "darkturquoise", "orchid"]
        self.PlanetColor3 = ["gold", "mediumorchid", "deepskyblue"]
        self.PlanetColor2 = ["gold", "cyan", "fuchsia"]


        if sv is None :
            print(f"state vector is none for solution {SolutionNumber}")
            return None
        self.sv = self.Scaler(self.sv)
        print("scaled state vector")
        i0 = np.arange(0, self.Neval, 1)
        self.indices = np.hstack((i0, i0, i0))
    
    
    def SetTailParameters(self, Ltail, Ntail, Dplanet):
        self.Ltail=Ltail
        self.Ntail=Ntail
        self.Dplanet = Dplanet
        
        self.Ctail = Ltail / (Ntail+2)**1.5
        self.Ltails = np.round(self.Ctail*np.arange(1, self.Ntail+3, 1)**1.5)
    
    def AutoSetTailsParameters(self):
        Dplanet = 5
        Ltail = round(self.Neval * 0.8)
        Ntail = 20
        self.SetTailParameters(Ltail, Ntail, Dplanet)
    
    def Alphas(self, ntails, start=1):
        return [start*(1-k/ntails) for k in range(ntails)]
    
    def Widths(self, ntails, start=1):
        return [start*np.exp(-k/5)+1 for k in range(ntails)]
    
    """scale graph"""
    def Scaler(self, sv, scale=3):
        mxx = np.max(sv[[0, 2, 4], :])
        mnx = np.min(sv[[0, 2, 4], :])
        mxy = np.max(sv[[1, 3, 5], :])
        mny = np.min(sv[[1, 3, 5], :])
        
        centerx = 0.5*(mxx + mnx)
        centery = 0.5*(mxy + mny)
        sv[[0, 2, 4], :] -= centerx
        sv[[1, 3, 5], :] -= centery
        
        scalex = scale/(mxx - mnx)
        scaley = scale/(mxy - mny)
        sv[[0, 2, 4], :] *= scalex
        sv[[1, 3, 5], :] *= scaley
        return sv
    
    """
        return a circular slice of array sv
        slice : starting at a distance d from index p,
                length l
    """
    def CircularParser(self, sv, p, d, l):
        _, n = sv.shape
        p = int(p)
        d = int(d)
        l = int(l)
        if d+l-p > n+1 :
            # slice too far
            print(f" error n : {n} p : {p} d : {d} l : {l}")
            return None
        
        if (p - (d+l) ) >= 0 :
            # no circular slicing
            return sv[:, p-d-l+1 : p-d+1]
        elif (p-d) >= 0 :
            # slice includes both ends of array
            return np.concatenate( ( sv[:, n - (l-(p-d))+1 : n], sv[:, 0 : p-d+1] ), axis=1)
        else :
            # slice is a full array away from p
            return sv[:, n-(d-p)-l+1 : n-(d-p)+1]
    
    

    
    def update_line(self, frame, line1, line2, line3, pline1, pline2, pline3, hline1, hline2, hline3, sv, n):
        # planets position
        pline1.set_data(sv[0:2, :frame])
        pline2.set_data(sv[2:4, :frame])
        pline3.set_data(sv[4:6, :frame])
        
        hline1.set_data(sv[0:2, :frame])
        hline2.set_data(sv[2:4, :frame])
        hline3.set_data(sv[4:6, :frame])
        
        # tails positions
        Ntail = self.Ntail
        Ctail = self.Ctail
        # tails lengths
        Ltails = self.Ltails

        for i in range(Ntail) :
            tail = self.CircularParser(sv[:, :], frame, Ltails[i], Ltails[i+1]-Ltails[i])[:, :-1]
            t1 = tail[0:2, :]
            t2 = tail[2:4, :]
            t3 = tail[4:6, :]
            
            line1[i].set_data( t1 )
            line2[i].set_data( t2 )
            line3[i].set_data( t3 )
        return [l for l in line1] + [l for l in line2] + [l for l in line3] + [pline1, pline2, pline3, hline1, hline2, hline3] 
        
        
    
    def Animation(self):
        print("starting animation ...")
        fig1 = plt.figure(dpi=200)
        plt.style.use('dark_background')
        plt.tight_layout()
        plt.gca().set_aspect('equal', adjustable='box')
        
        l1 = []
        l2 = []
        l3 = []
        alphas = self.Alphas(self.Ntail, start=0.6)
        widths = self.Widths(self.Ntail, round(self.Dplanet*0.7))
        for i in range(self.Ntail):
            l, = plt.plot([], [], self.PlanetColor2[0], linestyle='-', linewidth=widths[i], alpha=alphas[i])
            l1.append(l)
            l, = plt.plot([], [], self.PlanetColor2[1], linestyle='-', linewidth=widths[i], alpha=alphas[i])
            l2.append(l)
            l, = plt.plot([], [], self.PlanetColor2[2], linestyle='-', linewidth=widths[i], alpha=alphas[i])
            l3.append(l)
        
        p1, = plt.plot([], [], self.PlanetColor2[0], marker='o', linestyle='', markevery=[-1], markersize=self.Dplanet)
        p2, = plt.plot([], [], self.PlanetColor2[1], marker='o', linestyle='', markevery=[-1], markersize=self.Dplanet)
        p3, = plt.plot([], [], self.PlanetColor2[2], marker='o', linestyle='', markevery=[-1], markersize=self.Dplanet)
        
        alpha0 = 0.5
        h1, = plt.plot([], [], "white", marker='o', linestyle='', markevery=[-1], markersize=self.Dplanet//1.4, alpha=alpha0 )
        h2, = plt.plot([], [], "white", marker='o', linestyle='', markevery=[-1], markersize=self.Dplanet//1.4, alpha=alpha0 )
        h3, = plt.plot([], [], "white", marker='o', linestyle='', markevery=[-1], markersize=self.Dplanet//1.4, alpha=alpha0 )

        
        plt.xlim(-2, 2)
        plt.ylim(-2, 2)
        plt.axis('off')
        plt.gca().set_position((0, 0, 1, 1))
        line_ani = animation.FuncAnimation(fig1, self.update_line, self.Neval, fargs=(l1, l2, l3, p1, p2, p3, h1, h2, h3, self.sv, self.Neval),
                                           interval=7, blit=True)
        
        line_ani.save("tribody_" + str(self.sol) +".mp4")
        print("done")
    
    def Plot(self):
        plt.figure(dpi=120, figsize=(7,7))
        plt.style.use('dark_background')
        plt.tight_layout()
        plt.title("solution " + str(self.sol))
        circle = plt.Circle((0, 0), 1, color='black', fill=False)
        plt.xlim(-2, 2)
        plt.ylim(-2, 2)
        ax = plt.gca()
        ax.set_aspect('equal', adjustable='box')
        #ax.add_patch(circle)
        plt.grid(color="dimgrey")
        s = ["-", "dotted", "--"]
        for k in range(3):
            plt.plot(self.sv[2*k], self.sv[2*k+1], marker='o', markevery=[0], linestyle=s[k], color=self.PlanetColor[k])
        #plt.plot(barytime[:, 0], barytime[:, 1], linestyle='--', color="black")
        plt.show()
    


