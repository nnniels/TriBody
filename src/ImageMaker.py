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
        self.PlanetColor2 = ["gold", "mediumorchid", "deepskyblue"]

        if sv is None :
            print(f"state vector is none for solution {SolutionNumber}")
            return None
        self.sv = self.Scaler(self.sv)
        print("scaled state vector")

    
    def Alphas(self, ntails, start=1):
        return [start*(1-k/ntails) for k in range(ntails)]
    
    def Widths(self, ntails, start=1):
        return [start*np.exp(-k/5)+1 for k in range(ntails)]
    
    
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
    
    
    def update_line(self, frame, pline1, pline2, pline3, line1, line2, line3, sv, n):
        pline1.set_data(sv[0:2, :frame])
        pline2.set_data(sv[2:4, :frame])
        pline3.set_data(sv[4:6, :frame])
        Ntail = min(len(line1), len(line2), len(line3))
        deg = 4
        Ltail = max(n//(deg*Ntail), n//200)
        
        for i in range(Ntail) :
            line1[i].set_data(sv[0:2, frame-Ltail*(i+1):frame])
            line2[i].set_data(sv[2:4, frame-Ltail*(i+1):frame])
            line3[i].set_data(sv[4:6, frame-Ltail*(i+1):frame])
        return [pline1, pline2, pline3] + [l for l in line1] + [l for l in line2] + [l for l in line3]
    
    def update_line2(self, frame, pline1, pline2, pline3, line1, line2, line3, sv, n):
        pline1.set_data(sv[0:2, :frame])
        pline2.set_data(sv[2:4, :frame])
        pline3.set_data(sv[4:6, :frame])
        Ntail = min(len(line1), len(line2), len(line3))
        deg = 4
        Ltail = max(n//(deg*Ntail), n//200)
        
        for i in range(Ntail) :
            l = round(frame-Ltail*(i+1)**1.5)%self.Neval #gives funny results
            t1 = np.hstack(( sv[0:2, l:-1], sv[0:2, l:frame] ))
            t2 = np.hstack(( sv[2:4, l:-1], sv[2:4, l:frame] ))
            t3 = np.hstack(( sv[4:6, l:-1], sv[4:6, l:frame] ))

            line1[i].set_data( t1 )
            line2[i].set_data( t2 )
            line3[i].set_data( t3 )
        return [pline1, pline2, pline3] + [l for l in line1] + [l for l in line2] + [l for l in line3]
    
    
    def Animation(self):
        print("starting animation ...")
        fig1 = plt.figure(dpi=200)
        plt.style.use('dark_background')
        plt.tight_layout()
        plt.gca().set_aspect('equal', adjustable='box')
        p1, = plt.plot([], [], self.PlanetColor[0], marker='o', linestyle='', markevery=[-1])
        p2, = plt.plot([], [], self.PlanetColor[1], marker='o', linestyle='', markevery=[-1])
        p3, = plt.plot([], [], self.PlanetColor[2], marker='o', linestyle='', markevery=[-1])
        
        ntails = 20
        l1 = []
        l2 = []
        l3 = []
        alphas = self.Alphas(ntails, start=0.2)
        widths = self.Widths(ntails, 5)
        for i in range(ntails):
            l, = plt.plot([], [], self.PlanetColor[0], linestyle='-', linewidth=widths[i], alpha=alphas[i])
            l1.append(l)
            l, = plt.plot([], [], self.PlanetColor[1], linestyle='-', linewidth=widths[i], alpha=alphas[i])
            l2.append(l)
            l, = plt.plot([], [], self.PlanetColor[2], linestyle='-', linewidth=widths[i], alpha=alphas[i])
            l3.append(l)
        
        
        plt.xlim(-2, 2)
        plt.ylim(-2, 2)
        plt.axis('off')
        plt.gca().set_position((0, 0, 1, 1))
        line_ani = animation.FuncAnimation(fig1, self.update_line, self.Neval, fargs=(p1, p2, p3, l1, l2, l3, self.sv, self.Neval),
                                           interval=7, blit=True)
        
        # To save the animation, use the command: line_ani.save('lines.mp4')
        #plt.show()
        line_ani.save("tribody_" + str(self.sol) +".mp4")
        print("done")
    
    def Animation2(self):
        print("starting animation ...")
        fig1 = plt.figure(dpi=200)
        plt.style.use('dark_background')
        plt.tight_layout()
        plt.gca().set_aspect('equal', adjustable='box')
        p1, = plt.plot([], [], self.PlanetColor2[0], marker='o', linestyle='', markevery=[-1])
        p2, = plt.plot([], [], self.PlanetColor2[1], marker='o', linestyle='', markevery=[-1])
        p3, = plt.plot([], [], self.PlanetColor2[2], marker='o', linestyle='', markevery=[-1])
        
        ntails = 20
        l1 = []
        l2 = []
        l3 = []
        alphas = self.Alphas(ntails, start=0.2)
        widths = self.Widths(ntails, 5)
        for i in range(ntails):
            l, = plt.plot([], [], self.PlanetColor2[0], linestyle='-', linewidth=widths[i], alpha=alphas[i])
            l1.append(l)
            l, = plt.plot([], [], self.PlanetColor2[1], linestyle='-', linewidth=widths[i], alpha=alphas[i])
            l2.append(l)
            l, = plt.plot([], [], self.PlanetColor2[2], linestyle='-', linewidth=widths[i], alpha=alphas[i])
            l3.append(l)
        
        
        plt.xlim(-2, 2)
        plt.ylim(-2, 2)
        plt.axis('off')
        plt.gca().set_position((0, 0, 1, 1))
        line_ani = animation.FuncAnimation(fig1, self.update_line2, self.Neval, fargs=(p1, p2, p3, l1, l2, l3, self.sv, self.Neval),
                                           interval=7, blit=True)
        
        # To save the animation, use the command: line_ani.save('lines.mp4')
        #plt.show()
        line_ani.save("tribody_beg_" + str(self.sol) +".mp4")
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
    


