# Code for Enclosure projects 
# jupyter notebooks and code at https://github.com/jhconning/enclosure
# Matthew J. Baker and Jonathan Conning

# Things to fix
# plotY doesnt account for Tbar/Lbar. rescale
# check:  8/18/20 added mu option for most relevant functions
# finish: tepvt for interior private..


import numpy as np
import matplotlib.pyplot as plt
from ipywidgets import interact, fixed

Tbar=100
Lbar=100

def f(T, L, a=1/2, th=1):
    '''production technology on commons/un-enclosed land'''
    return th * T**(1-a) * L**a

def mple(te, le, a=1/2, th=1, tlbar=Tbar/Lbar):
    '''marginal product of Labor on enclosed land'''
    return a* f(te,le,a,th)/le  * tlbar**(1-a)

def aple(te, le, a=1/2, th=1, tlbar=Tbar/Lbar):
    '''average product of Labor '''
    return f(te,le,a,th)/le  * tlbar**(1-a)

def mpte(te, le, a=1/2, th=1, tlbar=Tbar/Lbar):
    '''marginal product of Land on enclosed land'''
    return (1-a)* f(te,le,a,th)/te  * tlbar**(-a)

def mplu(te, le, a=1/2, th=1, tlbar=Tbar/Lbar):
    '''marginal product of Labor on unenclosed land
       same tech but useful to have other name'''
    return mple(te, le, a, th, tlbar)

def aplu(te, le, a=1/2, th=1, tlbar=Tbar/Lbar):
    '''average product of Labor on unenclosed land'''
    return aple(te, le, a, th, tlbar)

def Lambda(th, alp, mu):
    ''' Key expression for private enclosure.
      mu = 0 : APL=MPL
      mu = 1 : MPL = MPL etc
    '''
    return ( (alp*th)/(1-mu+alp*mu) )**(1/(1-alp))


def req(te, th=1, alp=1/2, ltbar=1, mu=0):
    '''Decentralized Equilibrium rental'''
    lam = Lambda(th, alp, mu)
    return (1-alp)*th * lam**alp * (1+(lam-1)*te)**(-alp) * (ltbar)**(alp)


def weq(te, th=1, alp=1/2, tlbar=1, mu =0):
    '''Decentralized Equilibrium wage'''
    lam = Lambda(th, alp, mu)
    return (1-te+lam*te)**(1-alp) * (tlbar)**(1-alp)

def leo(te, th, alp):
    '''optimal labor allocation (from MPLe = MPLu) given enclosed land share te'''
    lam = th**(1/(1-alp))
    return (lam*te)/(1+lam*te-te)

def le(te, th, alp, mu):
    '''eqn labor share on enclosed for given te when 
       (1-mu*alp*mu)*APL=MPL  
       mu = 0:   APLc = MPLe,   le* in paper
       mu = 1:   MPLc = MPLe,   leo in paper
       mu in (0,1)   in between partly secure
       '''
    lam = Lambda(th, alp, mu)
    return (lam*te)/(1+lam*te-te)

def totalq(te, th, alp, mu):
    '''total output in the economy given te and mu.
       Note costs of enclosure are not subtracted.'''
    leq = le(te, th, alp, mu)
    return f(Tbar, Lbar,alp, th) * ( th*f(te, leq, alp, th) + f(1-te, 1-leq, alp, 1) )

def plotY(th = 1, lbar = 1, alp = 0.5,  c = 1, mu=0):
    '''Plot total income net of clearing costs'''
    te = np.linspace(0, 1.0, 20)
    plt.figure(figsize=(8,6))
    plt.title("Output net of enclosure costs as function of te")
    plt.plot(te, ( totalq(te, th, alp, mu) ),  label= r'total' )
    plt.plot(te, ( totalq(te, th, alp, mu)-c*te*Tbar),  label= r'total-cTe' )
    #plt.plot(te, req(te, th, alp, lbar, mu)*te*Tbar,  label= r'$r*Te$')
    #plt.plot(te, c*te*Tbar,   label= r'$c*Te$')
    teo = teopt(th, alp, c, lbar)
    plt.axhline(totalq(0, th, alp, mu), xmin=0, xmax=1, linestyle=':', alpha=0.3)
    plt.xlabel(r'$t_e$')
    plt.xlim(0,1), plt.ylim(70, 120)
    plt.legend()



def plotle(te=1/2, th=1, alp=1/2, mu=0.5):
    '''Draw edgeworth box and te/le(te) ratio'''
    fig, ax = plt.subplots(figsize=(7,7))
    tte = np.linspace(0,1,50)
    leq = le(te, th, alp, mu=0)
    leop = le(te, th, alp, mu=1)
    ax.set_xlim(0,1)
    ax.set_ylim(0,1)
    ax.set_aspect('equal', 'box')
    ax.plot(tte, le(tte, th, alp, mu=0), linewidth=2)
    ax.plot(tte, le(tte, th, alp, mu=1), linewidth=2)  
    ax.plot(tte, le(tte, th, alp, mu), linewidth=2) 
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
    #lam = (th*alp)**(1/(1-alp))
    #ax.text(0.05, 0.9, r'$\theta=$' +f'{th: 2.1f}' r', $\Lambda =$'
    #      + f'{lam: 3.2f}' + r', $\ \ \ \frac{l_e}{t_e}=$'
    #      + f'{leq/(te+0.001):3.1f}', fontsize=16)
    ax.legend(loc='lower right', fontsize=14)
    print(leq, leop)


def plotreq(th=1, alp=1/2, tlbar=1, c=0, wplot=True):
    '''plot rental rate as function of te
       optionally also plot wages '''
    tte = np.linspace(0,1,50)
    fig, ax =  plt.subplots(figsize=(5,5))
    r0 = req(0, th, alp, tlbar)
    r1 = req(1, th, alp, tlbar)
    ax.set_xlim(0,1)
    #ax.set_ylim(0,2)
    ax.plot(tte, req(tte, th, alp, tlbar),  label= r'$r$')
    ax.set_xlabel(r'$t_e$', fontsize=15)
    #ax.text(1.01,r1-0.025,r'$r^*(1)$',fontsize=13)
    #ax.text(-0.13,r0-0.025,r'$r^*(0)$',fontsize=13)
    ax.grid()
    ax.axhline(y=c,linestyle='--', label=r'$c$')
    if wplot:
        ax.plot(tte, weq(tte, th, alp, tlbar), label= r'$w$')
        # plot output net of enclosure costs relative to non-enclose output.
        #ax.plot(tte,  (totalq(tte, th, alp) - c*tte*Tbar)/f(Tbar,Lbar,alp, th),label= r'$net$' )
        
    lam = (th*alp)**(1/(1-alp))
    ax.legend()


def plotmpts(te=1/2, alp=1/2, th=1, tlbar=Tbar/Lbar, mu = 0):
    '''Plot partial eqn labor demand graph 
       TODO: not yet working for mu different from 0'''
    ll = np.linspace(0.0001, 0.9999, 400)
    leop = leo(te, th, alp)         #optimal 
    leam = le(te, th, alp, mu)      #private
    WindowsError = weq(te, th, alp, tlbar)
    we = weq(te, th, alp, tlbar)
    wo = mple(te, leop, alp, th, tlbar)
    wc = mplu(1-te, 1-leam, alp, 1, tlbar)
    fig, ax = plt.subplots(figsize=(8,6))
    #ax.spines['top'].set_visible(False)
    mpe = mple(te, ll, alp, th, tlbar)
    apu = aplu(1-te, 1-ll, alp, 1, tlbar)
    mpu = mplu(1-te, 1-ll, alp, 1, tlbar)

    ax.plot(ll, mpe, linewidth=2, color='k')
    ax.plot(ll, apu, linewidth=2, color='k')
    ax.plot(ll, mpu, linewidth=2, color='k')   
    ax.fill_between(ll, mpe, mpu, 
                    where=(ll>=leam)&(ll<=leop), 
                    hatch= '//',
                    color='none',
                    edgecolor='k')

    #ax.set_xlabel(r'$l_e$ - share')
    ax.vlines(x=leam, ymin=0, ymax=we, linestyle=':') 
    ax.vlines(x=leop, ymin=0, ymax=wo, 
              linestyle=':') 
    ax.axhline(we, linestyle=':')
    ax.axhline(wc, linestyle=':')
    ax.set_xticklabels([])
    ax.set_yticklabels([])
    ax.set_title('Labor Allocations, given '+r'$t_e$'+' = '+f'{te:2.2f}')
    ax.set_ylim(0,1.5)
    ax.set_xlim(0,1)
    ax.text(1.01, we, r'$w_e$', fontsize=12)
    ax.text(1.01, wc, r'$w_c$', fontsize=12)
    ax.text(leam, -0.1, r'$l_e^*(t_e)$', fontsize=12,ha='center')
    ax.text(leop, -0.1, r'$l_e^o(t_e)$', fontsize=12,ha='center')

    ax.annotate(r'$MPL_c$',xy=(0.85, mplu(1-te, 0.15, alp, 1, tlbar)), 
                textcoords="offset points", 
                 xytext=(-30,20), fontsize=14)
    ax.annotate(r'$APL_c$',xy=(0.65, aplu(1-te, 0.35, alp, 1, tlbar)), 
                textcoords="offset points", 
                 xytext=(-24,15), fontsize=14)
    ax.annotate(r'$MPL_e$',xy=(0.8,  mple(te, 0.8, alp, th, tlbar)), 
                textcoords="offset points", 
                 xytext=(20,-20), fontsize=14)

    labels = ['A', 'B', 'C', 'F', '', '', '', '', '0']
    xx = [leam, leam,    leop, 1, 1, 1, leam, leop,0]
    yy = [wc, we, wo, 0, we, wc, 0, 0, 0]    
    for x, y, lab in zip(xx, yy, labels):
        ax.scatter(x, y, marker='o', s=20, c ='k',clip_on=False ) 
        plt.annotate(lab, (x,y), 
                textcoords="offset points", # how to position the text
                 xytext=(-5,7), # distance from text to points (x,y)
                 ha='center', fontsize=12)
    return fig, ax
   

def simplempl(te=1/2, alp=1/2, th=1, tlbar=Tbar/Lbar):
    ll = np.linspace(0.001, 0.999, 50)
    plt.figure(figsize=(10,6))
    plt.plot(ll, mple(te, ll, alp, 1, tlbar)) 
    plt.plot(ll, mplu(te, ll, 0.3, th, tlbar))
    plt.plot(ll, aple(te, ll, alp, 1, tlbar))
    plt.xlabel('l - labor')
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
    #plt.axvline(1-le(te, th, alp, mu=0), linestyle='-') 
    #plt.axvline(le(te, alp, th, mu=1), ymin=0, ymax=0.25, linestyle=':') 
    #plt.axhline(0.5,  linestyle=':') 
    plt.title('MPL and APL on enclosed and unenclosed lands')
    #plt.ylim(0,2)
    #plt.xlim(0,1)



## More plots 

def z(te, th, alp, lbar):
    '''output per unit land net of enclosure cost
       $z(t_e) = \bar l^\alpha \left(1+(\Lambda^0-1)t_e\right)^{1-\alpha}-c\bar t_e$
       To find optimal enclosure rate, given MPLs equalized '''
    lam = th**(1/(1-alp))
    return lbar**alp * (1+(lam-1)*te)**(1-alp) 

def zprime(te, th, alp, lbar):
    '''output per unit land net of enclosure cost
       $z(t_e) = \bar l^\alpha \left(1+(\Lambda^0-1)t_e\right)^{1-\alpha}-c\bar t_e$
       To find optimal enclosure rate, given MPLs equalized '''
    lam = th**(1/(1-alp))
    return  (1-alp)*(lam-1)*lbar**alp  * (1+(lam-1)*te)**(-alp) 


def teopt(th, alp, c, lbar):
    '''Social optimal enclosure
        zprime= derivative of z. Determines efficient enclosure. If 
        zprime(0)<c  : no enclosure 
        zprime(1)>c  : full enclosure
        zprime(0)>c and zprime(1)<c : partial enclosure
           then solve for teopt from foc
        '''
    lam = th**(1/(1-alp))
    zprime = lambda te : (1-alp)*(lam-1)*lbar**alp  * (1+(lam-1)*te)**(-alp) 
    if zprime(0)<c:
        teopt = 0
    elif zprime(1)>c:
        teopt = 1
    else:
        teopt = ( ( ((1-alp)*(lam-1)*lbar**alp)/c)**(1/alp)  -1  )/(lam-1)
    return teopt


def tepvt(th, alp, c, lbar, mu):
    '''Private enclosure rate
        req(te)= rental rate 
        r(0)<c  : no enclosure 
        r(1)>c  : full enclosure
        r(0)>c and r(1)<c : partial enclosure
           then solve for teopt from foc
        '''
    thresh = (1-mu+alp*mu)/alp    
    lam = Lambda(th, alp, mu)
    r0 = req(0, th, alp, lbar)
    r1 = req(1, th, alp, lbar)
    if th<thresh:
        if r0>=c:
            tep = 1
        elif r1<c:
            tep = 0
        else:
            tep = lbar * (lam/(lam-1)) * (th*(1-alp)/c )**(1/alp) - (1/(lam-1))
    
    elif th>= thresh:  
        if r1>=c:
            tep = 1
        elif r0<c:
            tep = 0
        else:
            tep = lbar * (lam/(lam-1)) * (th*(1-alp)/c )**(1/alp) - (1/(lam-1))

    return tep


def tepvt_g(th, alp, c, lbar, mu):
    '''Private enclosure rate (global game refinement)
        just like pvtpart() but adjuss for global game
        If theta < theta_hi then global game refinement says enclose fully if
        tep (from pvtpart) <= 0.5 otherwise no enclosre.
        '''
    thresh = (1-mu+alp*mu)/alp    
    tep = tepvt(th,alp,c, lbar, mu=0)
    
    tepg = tep
    if (tep==1) or (tep==0):
        tepg = tep
    elif (th < thresh):
        if (tep > 0.5):
            tepg = 0
        elif (tep <= 0.5):
            tepg = 1

    return tepg



def dwl(th, alp, c, lbar):
    '''
    Returns DWL at each paramter
    '''
    teo= teopt(th, alp, c, lbar)
    tep = tepvt(th,alp,c, lbar, mu=0)
    teg = tepvt_g(th,alp,c, lbar, mu=0)

    zo = z(teo, th, alp, lbar) - c*teo
    zg = z(teg, th, alp, lbar) - c*teg
    return  zo-zg

def dwlpct(th, alp, c, lbar):
    '''
    Returns actual/potential at each paramter
    '''
    teo= teopt(th, alp, c, lbar)
    tep = tepvt(th,alp,c, lbar, mu=0)
    teg = tepvt_g(th,alp,c, lbar, mu=0)

    zo = z(teo, th, alp, lbar) - c*teo
    zg = z(teg, th, alp, lbar) - c*teg
    return  zg/zo


def plotz(th=1, alp=1/2, c=1, lbar=Lbar, ax=None):
    '''Plot z(t_e).  input ax to allow use with subplots'''
    if ax is None:
        fig, ax =  plt.subplots(figsize=(5,5))
    teo = teopt(th, alp, c, lbar)
    tte = np.linspace(0,1,20)
    ax.scatter(teo, z(teo, th, alp, lbar) - c*teo, s=40, clip_on=False )
    ax.plot(tte, z(tte, th, alp, lbar) - c*tte)
    ax.set_xlim(0,1)
    ax.axvline(teo, ymin=0, ymax=z(teo, th, alp, lbar)-c*teo ,  linestyle='dashed')
    ax.set_xlabel(r'$t_e$'+' -- pct land enclosed')
    ax.set_ylabel(r'$z(t_e)$')
    ax.set_title(r'$z(t_e) - c\cdot t_e$')
    #return ax


def plotzprime(th, alp, c, lbar):
    teo= teopt(th, alp, c, lbar)
    tte = np.linspace(0,1,20)
    plt.scatter(teo, zprime(teo, th, alp, lbar) , s=40, clip_on=False )
    plt.axhline(c, xmin=0, xmax=1,  linestyle='dashed')
    plt.axvline(teo,  linestyle='dashed')
    plt.plot(tte, zprime(tte, th, alp, lbar))
    plt.xlabel(r'$t_e$'+' -- pct land enclosed')
    plt.ylabel(r'$z(t_e)$')
    plt.title(r'$z\prime(t_e) \; \mathrm{vs} \; c$')
    plt.xlim(0,1)



## Log linear MVPL plts


def plotdmg(te=1/2, alp=1/2, th=1, tlbar=Tbar/Lbar):
    '''like plotmpts but in logs to linearize'''
    ll = np.linspace(0.1, 99.9, 50)
    lnl = np.log(ll)
    plt.figure(figsize=(10,6))
    plt.plot(lnl, np.log(mple(te, ll, alp, th, tlbar)) ) 
    #plt.plot(lnl, np.log(mplu(te, ll, alp, 1, tlbar)))
    plt.plot(ll, aplu(te, ll, alp, 1, tlbar))
    plt.xlabel('l - labor')
    plt.title('MPL and APL on enclosed and unenclosed lands')


## Partition Diagrams from paper

def socpart(c = 1, alp= 2/3, mu =0, soc_opt= True, cond_opt=True, pv_opt=False, logpop=True):
    '''Plots loci determining parameter partitions corresponding to 
        Social (and Conditional Social) Optimum
        None, Full, or Partial Enclosure zones
        Option: to log plot or not
        '''
    start, finish  = 1.1, 2.1   # range that will be plotted
    the_1 = np.arange(start, finish, .01)
    cv = 1 / alp                          # high TFP gain threshold
    the_lo = np.arange(start, cv, .01)
    the_hi = np.arange(cv, finish, .01)
    
    ## Social Optima
    lamO = the_1**(1/(1-alp))

    lo0 = ( c / ( (lamO - 1)*(1-alp) )  ) **(1/alp)
    lo1 = lamO * lo0      

    ##### Conditional Optima:  we need separate plot ranges, each side of cv = theta_hat
    lam_hi =  Lambda(th = the_hi, alp= alp, mu = mu)

    lc  = ( c/(the_lo - 1))**(1/alp)
    lc0 = ( alp*c                  / (( lam_hi*(1+alp) - alp)*(1-alp))  ) **(1/alp)
    lc1 = ( c                      / (the_hi*(1-alp)  ) ) **(1/alp)

    ### Private Optima
    #lam = (the_1*alp)**(1/(1-alp))
    lam = Lambda(th = the_1, alp= alp, mu = mu)
    ld0 = ( alp*c/( (1-alp)*lam)  ) **(1/alp)
    ld1 = ( c / ( the_1*(1-alp) )  ) **(1/alp)

    
    if logpop:
        lc0, lc1, lc = np.log(lc0), np.log(lc1), np.log(lc)
        lo0, lo1 = np.log(lo0), np.log(lo1)
        ld0, ld1 = np.log(ld0), np.log(ld1)

    fig, ax = plt.subplots(figsize=(10, 8))

    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.spines['left'].set_linewidth(2)
    ax.spines['bottom'].set_linewidth(2)
    xlbl = ax.set_xlabel(r'$\theta$', fontsize=20)
    ylbl = ax.set_ylabel(r'$\overline{l}$', fontsize=18)

    # Shift the label on the x-axis a little bit
    xpos = list(xlbl.get_position())
    xpos[0] = xpos[0]+.41
    xpos[1] = xpos[1]-.02
    ax.xaxis.set_label_coords(xpos[0], xpos[1])

    ax.set_xticks([])
    ax.set_ylim(0, 5)
    if logpop:
        ax.set_yticks([])
        ax.autoscale()
        ylbl = ax.set_ylabel(r'$ln(\overline{l})$', fontsize=18)
   
    ep = np.max(the_1)+.021

    if soc_opt:
        oline1 = ax.plot(the_1, lo0, color= 'black')
        bline1 = ax.plot(the_1, lo1, color= 'black')
        t1 = ax.text(ep, np.min(lo0), r'$l^o_0$', fontsize=16)
        t2 = ax.text(ep, np.min(lo1)+.05, r'$l^o_1$', fontsize=16)

    if cond_opt:
        gline1 = ax.plot(the_hi, lc0, color= 'black', linestyle='dashed')
        pline1 = ax.plot(the_hi, lc1, color= 'black', linestyle='dashed')
        bkline = ax.plot(the_lo, lc,  color='black', linestyle='dashed')
        t3 = ax.text(ep, np.min(lc0), r'$l^*_0$', fontsize=16)
        t4 = ax.text(ep, np.min(lc1)-.05, r'$l^*_1$', fontsize=16)
        t5 = ax.text(cv-.1, np.min(lc)-.04, r'$l^*$', fontsize=16)

    if pv_opt:
        oline1 = ax.plot(the_1, ld0, color= 'red')
        bline1 = ax.plot(the_1, ld1, color= 'red')

    vline1 = ax.axvline((1-(1-alp)*mu)/alp, ymax=.95, linestyle=':', color='black')
    vline2 = ax.axvline(1, ymax=.95, linestyle=':', color='black')

    ax.text(cv, np.min(lo0)-.5, r'$\frac{1}{\alpha}$', fontsize=16)
    ax.text(1, np.min(lo0)-.5, r'$1$', fontsize=16)

    #if cond_opt == False:
    #    fig.savefig('social_optimum.png')
    #else:
    #    fig.savefig('social_opt_cond.png')


def prvpart(c = 1, alp= 2/3, full_diag = False, logpop=True, ax=None):

    if ax is None:
        fig, ax = plt.subplots(figsize=(10, 8))
    start = 1.1
    finish = 2.1
    cv = 1 / alp
    the_1 = np.arange(1.1, finish, .01)

    ### Truncated range for the other stuff

    the_d = np.arange(.8, finish, .01)

    #the_d = np.arange(1/alp, finish, .01)
    the_gg = np.arange(.8, cv, .01 )

    lo0 = ( c                      / ((the_1**(1/(1-alp)) - 1)*(1-alp))  ) **(1/alp)
    lo1 = ( c*the_1**(alp/(1-alp)) / ((the_1**(1/(1-alp)) - 1)*(1-alp))  ) **(1/alp)

    if logpop:
        lo0, lo1 = np.log(lo0), np.log(lo1)

    ##### For these lines, we need separate plot ranges, so which run to the critical value

    the_r1 = np.arange(start, cv, .01)
    the_r2 = np.arange(cv, finish, .01)

    ### Conditional optimum commented out
    lam = (the_r2*alp)**(1/(1-alp))
    lc0 = ( alp*c                  / ( (1-alp) * ( lam*(1+alp) - alp) )  ) **(1/alp)
    #lc0 = ( alp*c                  / (((the_r2*alp)**(1/(1-alp))*(1+alp) - alp)*(1-alp))  ) **(1/alp)
    lc1 = ( c                      / (the_r2*(1-alp)  ) ) **(1/alp)
    lc  = ( c/(the_r1 - 1))**(1/alp)

    if logpop:
        lc0, lc1, lc = np.log(lc0), np.log(lc1), np.log(lc)

    ln_pd1  =  ( c / (the_d*(1-alp))) **(1/alp)  
    Lamgg = (alp*the_gg)**(1/(1-alp))
    ln_pdgg =  ( alp*c / (1-alp*the_gg) *  (1-Lamgg)/Lamgg )**(1/alp)                
    ln_pd0  =  ( alp*c / ((1-alp)*(alp*the_d)**(1/(1-alp)))  ) **(1/alp) 

    if logpop:
        ln_pd0, ln_pd1, ln_pdgg = np.log(ln_pd0), np.log(ln_pd1), np.log(ln_pdgg)

    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.spines['left'].set_linewidth(2)
    ax.spines['bottom'].set_linewidth(2)

    xlbl = ax.set_xlabel(r'$\theta$', fontsize=26)
    ylbl = ax.set_ylabel(r'$\overline{l}$', fontsize=26)

    # Shift the label on the x-axis a little bit
    xpos = list(xlbl.get_position())
    xpos[0] = xpos[0]+.41
    xpos[1] = xpos[1]-.02
    ax.xaxis.set_label_coords(xpos[0], xpos[1])

    #ax.set_xticks([])
    ax.set_ylim(0,6)
    if logpop:
        #ax.set_yticks([])
        ax.set_ylim(-0.5,4)
        ax.autoscale()
        ylbl = ax.set_ylabel(r'$ln(\overline{l})$', fontsize=18)   

    ep = np.max(the_1)+.021
    # Conditional optimum stuff commented out...

    if full_diag:
        oline1 = ax.plot(the_1, lo0, color= 'black')
        bline1 = ax.plot(the_1, lo1, color= 'black')
    #    gline1 = ax.plot(the_r2, ln_ps0, color= 'black', linestyle='dashed')
    #    pline1 = ax.plot(the_r2, ln_ps1+.02, color= 'black', linestyle='dashed')
    #    bkline = ax.plot(the_r1, ln_ps,  color='black', linestyle='dashed')

        t1 = ax.text(ep, np.min(lo0), r'$l^o_0$', fontsize=16)
        t2 = ax.text(ep, np.min(lo1)+.05, r'$l^o_1$', fontsize=16)
    #    t3 = ax.text(ep, np.min(ln_ps0), r'$l^*_0$', fontsize=16)
    #    t4 = ax.text(ep, np.min(ln_ps1)-.05, r'$l^*_1$', fontsize=16)
    #    t5 = ax.text(cv-.1, np.min(ln_ps)+.34, r'$l^*$', fontsize=16)

    ## Comment out the global game stuff..

    bbline1 = ax.plot(the_d, ln_pd0, color='red')
    bbline2 = ax.plot(the_d, ln_pd1, color='red')
    bbline3 = ax.plot(the_gg, ln_pdgg, color='red', linestyle='dashed')

    vline1 = ax.axvline(1/alp, ymax=.95, linestyle=':', color='black')
    vline2 = ax.axvline(1, ymax=.95, linestyle=':', color='black')

    d1  = ax.text(ep, np.min(ln_pd0), r'$l^d_0$', fontsize=16)
    dgg = ax.text(np.max(the_gg)-.3, np.min(ln_pdgg)+.4, r'$l^d$', fontsize=16)

    if full_diag:
    #    d2  = ax.text(ep+.05, np.min(ln_pd1)-.07, r' $l^d_1$', fontsize=16)
        d2  = ax.text(ep, np.min(ln_pd1)-.07, r'$l^d_1$', fontsize=16)
    else:
        d2  = ax.text(ep, np.min(ln_pd1), r'$l^d_1$', fontsize=16)

    if full_diag:
        text1 = ax.text(cv, -1, r'$\frac{1}{\alpha}$', fontsize=16)
        text2 = ax.text(1, -1, r'$1$', fontsize=16)
    else:
        text1 = ax.text(cv, np.min(ln_pd0)-.5, r'$\frac{1}{\alpha}$', fontsize=16)
        text2 = ax.text(1, np.min(ln_pd0)-.5, r'$1$', fontsize=16)    

   # if full_diag:
   #     fig.savefig('nash_so_comp.png')
   # else:
   #     fig.savefig('nash_eq.png')

def threeplots(th, alp, c, lbar=2, logpop=False):
    '''
    axP  :  left subplot overlap social/private; mostly drawn by prvpart()
    axZ  :  top right subplot planner's  z(t_e) - c * t_e
    axZP :  bottom right subplot r vs z' vs c
    
    '''
    fig = plt.figure(figsize=(14, 8))
    axZ= fig.add_subplot(2,2,2)
    axZP= fig.add_subplot(2,2,4)
    axP= fig.add_subplot(1,2,1)
    
    # z() plot
    teo= teopt(th, alp, c, lbar)
    tte = np.linspace(0,1,20)
    tep = tepvt(th,alp,c, lbar, mu=0)
    teg = tepvt_g(th,alp,c, lbar, mu=0)

    dwlp = dwlpct(th, alp, c, lbar)


    # top right z(t_e) - c * t_e plot
    axZ.scatter(teo, z(teo, th, alp, lbar)-c*teo, s=40, clip_on=False )
    axZ.scatter(tep, z(tep, th, alp, lbar)-c*tep, s=40, clip_on=False,color='orange' )
    axZ.scatter(teg, z(teg, th, alp, lbar)-c*teg, s=40, clip_on=False, marker='X', color='red' )
    axZ.axvline(teo, ymin=0, ymax=z(teo, th, alp, lbar) -c*teo,  linestyle='dashed')
    axZ.axvline(tep, ymin=0, ymax=z(tep, th, alp, lbar)-c*tep ,  linestyle='dashed', color='orange')

    axZ.plot(tte, z(tte, th, alp, lbar) - c*tte )   
    axZ.set_xlim(0,1)
    #axZ.set_ylim(bottom=0, top=None)
    axZ.set_ylabel(r'$z(t_e)-c \cdot t_e $')
    #Ypct = (z(teg, th, alp, lbar)-c*teg)/(z(teo, th, alp, lbar)-c*teo)
    axZ.set_title(f'z-ct ({dwlp: .0%} potential)')


    # z prime, r and c plot
    axZP.scatter(teo, zprime(teo, th, alp, lbar), s=40, clip_on=False )
    axZP.scatter(tep, req(tep, th, alp, lbar), s=40, clip_on=False, color='orange' )
    axZP.scatter(teg, req(teg, th, alp, lbar), s=40, clip_on=False, marker='X', color='red' )


    axZP.axvline(teo, ymin=0, ymax=1 ,  linestyle='dashed')
    axZP.axvline(tep, ymin=0, ymax=1 ,  linestyle='dashed', color='orange')
    axZP.plot(tte, zprime(tte, th, alp, lbar), label=r'$z \prime$' )
    axZP.set_xlim(0,1)
    axZP.set_xlabel(r'$t_e$'+' -- pct land enclosed')
    axZP.set_ylabel(r'$c, r(t_e), z \prime (t_e) $')
    axZP.axhline(c, color='red', linestyle ='dashed', label='c')
    r0 = req(0, th, alp, lbar)
    r1 = req(1, th, alp, lbar)
    axZP.plot(tte, req(tte, th, alp, lbar),  label= '$r$')
    axZP.legend()
    
    axP.scatter(th, np.log(lbar), s=40)
    axP.set_xlim(0.9, 3)
    axP.set_ylim(0, 4)
    prvpart(c=c, alp=alp, full_diag=True, logpop=True, ax = axP)
    
    plt.show()
    