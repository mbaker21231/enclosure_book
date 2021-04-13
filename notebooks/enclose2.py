# Code for Enclosure project 
# jupyter notebooks and code at https://github.com/jhconning/enclosure
# Matthew J. Baker and Jonathan Conning


import numpy as np
import matplotlib.pyplot as plt
from ipywidgets import interact, fixed

Tbar=100
Lbar=100

def f(T, L, a=1/2, th=1):
    '''production technology on commons/un-enclosed land'''
    return th * T**(1-a) * L**a

def g(T, L, a=1/2, th=1):
    '''production technology on commons/un-enclosed land'''
    return th * T**(1-a) * L**a

def mplu(te, le, a=1/2, th=1, tlbar=Tbar/Lbar):
    '''marginal product of Labor on unenclosed land
       same tech but useful to have other name'''
    return th*a* f(te,le,a,th)/le  * tlbar**(1-a)

def aplu(te,le, a=1/2, th=1, tlbar=Tbar/Lbar):
    '''average product of Labor on unenclosed land'''
    return f(te,le,a,th)/le  * tlbar**(1-a)


def mple(te, le, a=1/2, th=1, tlbar=Tbar/Lbar):
    '''marginal product of Labor on enclosed land'''
    return th*mplu(te, le, a, th, tlbar)

def aple(te, le, a=1/2, th=1, tlbar=Tbar/Lbar):
    '''average product of Labor '''
    return th*aple(te, le, a, th, tlbar)



def mpte(te, le, a=1/2, th=1, tlbar=Tbar/Lbar):
    '''marginal product of Land on enclosed land'''
    return th*(1-a)* f(te,le,a,th)/te  * tlbar**(-a)




def weq(te, th=1, alp=1/2, tlbar=1):
    lam = (th*alp)**(1/(1-alp))
    return (1-te+lam*te)**(1-alp) * (tlbar)**(1-alp)

def req(te, th=1, alp=1/2, tlbar=1):
    lam = (th*alp)**(1/(1-alp))
    return (1-alp)*th * lam**alp * (1-te+lam*te)**(-alp) * (tlbar)**(-alp)

def leo(te, th, alp):
    '''optimal labor allocation (from MPLe = MPLu) given enclosed land a'''
    lam = th**(1/(1-alp))
    return lam*te/(1-te+lam*te)

def le(te, th, alp):
    '''eqn labor share on enclosed for given te when APL=MPL  '''
    lam = (th*alp)**(1/(1-alp))
    return lam*te/(1-te+lam*te)

def totalq(te, th, alp):
    '''total output in the economy given.
       This is net output as costs of enclosure are not subtracted.'''
    leq = le(te, th, alp)
    return f(Tbar,Lbar,alp, th) * ( th*f(te, leq, alp, th) + f(1-te, 1-leq, alp, 1) )

def plotY(alp = 0.5, th = 1, c = 1):
    '''Plot total income net of clearing costs'''
    te = np.linspace(0, 1.0, 20)
    plt.title("Output net of enclosure costs as function of te")
    plt.plot(te, totalq(te, th, alp) - c*te*Tbar)
    plt.xlabel(r'$t_e$')
    plt.xlim(0,1)



def plotle(te=1/2, th=1, alp=1/2):
    '''Draw edgeworth box and te/le(te) ratio'''
    fig, ax = plt.subplots(figsize=(7,7))
    tte = np.linspace(0,1,50)
    leq = le(te, th, alp)
    leop = leo(te, th, alp)
    ax.set_xlim(0,1)
    ax.set_ylim(0,1)
    ax.set_aspect('equal', 'box')
    ax.plot(tte, le(tte, th, alp), linewidth=2)
    ax.plot(tte, leo(tte, th, alp), linewidth=2)  
    ax.plot([0,1],[0, 1],linestyle=':')
    ax.plot([0,te],[0, leq],linestyle='-')
    ax.scatter(te, leq, label='private')
    ax.scatter(te, leop, label='social')
    ax.axhline(y=leq, xmin=0, xmax=te, linestyle=':')
    ax.axhline(y=leop, xmin=0, xmax=te, linestyle=':')
    ax.axvline(x=te, ymin=0, ymax=leq, linestyle=':')
    ax.axvline(x=te, ymin=0, ymax=leop, linestyle=':')
    ax.set_xlabel(r'$t_e$', fontsize=15)
    ax.set_ylabel(r'$l_e$', fontsize=15)
    lam = (th*alp)**(1/(1-alp))
    #ax.text(0.05, 0.9, r'$\theta=$' +f'{th: 2.1f}' r', $\Lambda =$'
    #      + f'{lam: 3.2f}' + r', $\ \ \ \frac{l_e}{t_e}=$'
    #      + f'{leq/(te+0.001):3.1f}', fontsize=16)
    ax.legend(loc='lower right', fontsize=14)

    

def plotreq(th=1, alp=1/2, tlbar=1, c=0, wplot=True):
    '''plot rental rate as function of te
       optionally also plot wages '''
    tte = np.linspace(0,1,50)
    fig, ax =  plt.subplots(figsize=(5,5))
    r0 = req(0, th, alp, tlbar)
    r1 = req(1, th, alp, tlbar)
    ax.set_xlim(0,1)
    ax.set_ylim(0,1)
    ax.plot(tte, req(tte, th, alp, tlbar),  label= r'$r$')
    ax.set_xlabel(r'$t_e$', fontsize=15)
    #ax.text(1.01,r1-0.025,r'$r^*(1)$',fontsize=13)
    #ax.text(-0.13,r0-0.025,r'$r^*(0)$',fontsize=13)
    ax.grid()
    ax.axhline(y=c,linestyle='--', label=r'$c$')
    if wplot:
        ax.plot(tte, weq(tte, th, alp, tlbar), label= r'$w$')
    lam = (th*alp)**(1/(1-alp))
    ax.legend()


def plotmpts(te=1/2, alp=1/2, th=1, tlbar=Tbar/Lbar):
    '''Plot a DMG stype partial eqn labor demand graph '''
    ll = np.linspace(0.001, 0.999, 50)
    leop = leo(te, th, alp)
    wc = mplu(te, leop)
    we = mpl
    fig, ax = plt.subplots(figsize=(10,6))
    ax.spines['top'].set_visible(False)
    ax.plot(ll, mplu(te, ll, alp, th, tlbar)) 
    ax.plot(ll, mple(te, 1-ll, alp, 1, tlbar), linewidth=4)
    ax.plot(ll, aplu(te, ll, alp, 1, tlbar), linewidth=4)
    ax.set_xlabel('l - labor')
    ax.vlines(x=1-le(te, th, alp), ymin=0, ymax=1, linestyle=':') 
    ax.vlines(x=leop, ymin=0, ymax=wc, linestyle=':') 
    ax.axhline(weq(te, th=1, alp=1/2, tlbar=1), linestyle=':')
    ax.set_title('Labor allocation given '+r'$t_e$')
    ax.set_ylim(0,1.5)
    ax.set_xlim(0,1)
   

def simplempl(te=1/2, alp=1/2, th=1, tlbar=Tbar/Lbar):
    ll = np.linspace(0.001, 0.999, 50)
    plt.figure(figsize=(10,6))
    plt.plot(ll, mple(te, ll, alp, 1, tlbar)) 
    plt.plot(ll, mplu(te, ll, 0.3, th, tlbar))
    plt.plot(ll, aple(te, ll, alp, 1, tlbar))
    plt.xlabel('l - labor')
    #plt.axvline(1-le(te, th, alp), linestyle='-') 
    #plt.axvline(lopt(te, alp, th), ymin=0, ymax=0.25, linestyle=':') 
    #plt.axhline(0.5,  linestyle=':') 
    plt.title('MPL and APL on enclosed and unenclosed lands')
    plt.ylim(0,2)
    plt.xlim(0,1)

def simplempl2(te=1/2, alp=1/2, th=1, tlbar=Tbar/Lbar):
    ll = np.linspace(0.001, 0.999, 50)
    lnl = np.log(ll)
    plt.figure(figsize=(10,6))
    plt.plot(lnl, np.log(mple(te, ll, alp, 1, tlbar))) 
    plt.plot(lnl, mplu(te, ll, 0.3, th, tlbar))
    plt.plot(lnl, aple(te, ll, alp, 1, tlbar))
    plt.xlabel('l - labor')
    #plt.axvline(1-le(te, th, alp), linestyle='-') 
    #plt.axvline(lopt(te, alp, th), ymin=0, ymax=0.25, linestyle=':') 
    #plt.axhline(0.5,  linestyle=':') 
    plt.title('MPL and APL on enclosed and unenclosed lands')
    #plt.ylim(0,2)
    #plt.xlim(0,1)



## for PaperDiagarmsAndAlgebra
## 

def z(te, th, alp, c, lbar):
    '''output per unit land net of enclosure cost
       $z(t_e) = \bar l^\alpha \left(1+(\Lambda^0-1)t_e\right)^{1-\alpha}-c\bar t_e$
       To find optimal enclosure rate, given MPLs equalized '''
    lam = th**(1/(1-alp))
    return lbar**alp * (1+(lam-1)*te)**(1-alp) - c*te

def teopt(th, alp, c, lbar):
    '''zprime= derivative of z. Determines efficient enclosure. If 
        zprime(0)<0  : no enclosure 
        zprime(1)>0  : full enclosure
        zprime(0)>0 and zprime(1)<0 : partial enclosure
           then solve for teopt from foc
        '''
    lam = th**(1/(1-alp))
    zprime = lambda te : (1-alp)*(lam-1)*lbar**alp  * (1+(lam-1)*te)**(-alp) - c
    if zprime(0)<0:
        teopt = 0
    elif zprime(1)>0:
        teopt = 1
    else:
        teopt = ( ( ((1-alp)*(lam-1)*lbar**alp)/c)**(1/alp)  -1  )/(lam-1)
    return teopt

def plotz(th, alp, c, lbar):
    teo= teopt(th, alp, c, lbar)
    tte = np.linspace(0,1,20)
    plt.scatter(teo,z(teo, th, alp, c, lbar), s=40, clip_on=False )
    plt.axvline(teo, ymin=0, ymax=z(teo, th, alp, c, lbar) ,  linestyle='dashed')
    plt.plot(tte, z(tte, th, alp, c, lbar) )
    plt.xlim(0,1)
    plt.xlabel(r'$t_e$'+' -- pct land enclosed')
    plt.ylabel(r'$z(t_e)$')
    #plt.ylim(1.1,1.5)
    # to plot y(te) and c*te as well:
    #plt.plot(tte,c*tte  )
    #plt.plot(tte, z(tte, th, alp, c, lbar)+c*tte )

## Log linear DMG type plot

def plotz2(ax=None, th=1, alp=1/2, c=1, lbar=Lbar):
    if ax is None:
        fig, ax =  plt.subplots(figsize=(5,5))
    teo= teopt(th, alp, c, lbar)
    tte = np.linspace(0,1,20)
    ax.scatter(teo,z(teo, th, alp, c, lbar), s=40, clip_on=False )
    ax.plot(tte, z(tte, th, alp, c, lbar) )
    ax.set_xlim(0,1)
    ax.axvline(teo, ymin=0, ymax=z(teo, th, alp, c, lbar) ,  linestyle='dashed')
    plt.xlabel(r'$t_e$'+' -- pct land enclosed')
    plt.ylabel(r'$z(t_e)$')
    #ax.axhline(c, color='red')
    #plt.ylim(1.1,1.5)
    #to plot y(te) and c*te as well:
    #plt.plot(tte,c*tte  )
    #plt.plot(tte, z(tte, th, alp, c, lbar)+c*tte )
    return ax


## Log linear DMG type plot




def plotdmg(te=1/2, alp=1/2, th=1, tlbar=Tbar/Lbar):
    '''like plotmpts but in logs to linearize'''
    ll = np.linspace(0.1, 99.9, 50)
    lnl = np.log(ll)
    plt.figure(figsize=(10,6))
    plt.plot(lnl, np.log(mple(te, ll, alp, th, tlbar)) ) 
    #plt.plot(lnl, np.log(mplu(te, ll, alp, 1, tlbar)))
    plt.plot(ll, aplu(te, ll, alp, 1, tlbar))
    plt.xlabel('l - labor')
    #plt.axvline(le(te, th, alp), linestyle=':') 
    #plt.axvline(lopt(te, alp, th), linestyle='-') 
    plt.title('MPL and APL on enclosed and unenclosed lands')
    #plt.ylim(0,3)
    #plt.xlim(0,1)

