#!/usr/bin/env python
"""
This script tests the conversions between real and complex spherical harmonics
coefficients
"""

#standard imports:
import os, sys
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt

#import shtools:
sys.path.append(os.path.join(os.path.dirname(__file__), "../../.."))
import pyshtools as shtools

#set shtools plot style:
sys.path.append(os.path.join(os.path.dirname(__file__), "../Common"))
from FigStyle import style_shtools
mpl.rcParams.update(style_shtools)

def main():
    test_MultitaperSE()

def test_MultitaperSE():
    print '\n---- testing SHReturnTapersM ----'
    theta0_deg = 20.
    theta0     = np.radians(theta0_deg)
    lmax       = 10
    orderM     = 2
    print 'creating spherical cap tapers with:',
    print 'size {:1.0f}deg, bandwidth {:d}, order {:d}'.format(theta0_deg,lmax,orderM)
    tapers,concentrations,shannon = shtools.SHReturnTapersM(theta0,lmax,orderM)
    print 'first 3 taper concentrations:'
    print concentrations[:3]

    print '\n---- testing SHReturnTapers ----'
    theta0_deg = 20.
    theta0     = np.radians(theta0_deg)
    lmax       = 10
    print 'creating spherical cap tapers of',
    print 'size {:1.0f}deg with bandwidth {:d}'.format(theta0_deg,lmax)
    tapers,concentrations,taperorder = shtools.SHReturnTapers(theta0,lmax)
    print 'first 3 taper concentrations:'
    print concentrations[:3]

    print '\n---- testing SHMultiTaperSE ----'
    lmax = 80
    ntapers = 3
    tapers = tapers[:,:ntapers]
    torders = taperorder[:ntapers]
    coeffs = np.random.normal(size = 2*(lmax+1)*(lmax+1)).reshape(2,lmax+1,lmax+1)
    localpower,localpower_sd = shtools.SHMultiTaperSE(coeffs,tapers,torders)
    print 'total power:',np.sum(localpower)

    print '\n---- testing SHMultiTaperCSE ----'
    lmax = 80
    ntapers = 3
    coeffs1 = np.random.normal(size = 2*(lmax+1)*(lmax+1)).reshape(2,lmax+1,lmax+1)
    coeffs2 = 0.5*(coeffs1+np.random.normal(size = 2*(lmax+1)*(lmax+1)).reshape(2,lmax+1,lmax+1))
    localpower,localpower_sd = shtools.SHMultiTaperCSE(coeffs1,coeffs2,tapers,torders)
    print 'total power:',np.sum(localpower)

#==== EXECUTE SCRIPT ====
if __name__ == "__main__":
    main()
