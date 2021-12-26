

# Appendix 
**(rough/incomplete)**

The socially optimal level of enclosure maximizes total output benefit  to not include the total costs of enclosure $ct_e\bar T$:

$$
Y-ct_e\bar T=\left[\theta\cdot F(t_e,l_e)+F(1-t_e,1-l_e)\right ]\cdot F(\bar T, \bar L)-ct_e\bar T
$$

and we then define

$$
z(t_e)=\frac{Y}{\bar T}
$$

This makes it easier to directly compare $z'(t_e)$ which is the total marginal benefit to enclosing to $r(t_e)$ which is the private marginal product of land.  As shown below, we can even demonstrate the relationship.

We then have:

$$
z(t_e) = \bar l^{\alpha} \cdot \left[ 1+\left(\Lambda_o-1\right)t_e\right]^{1-\alpha}
$$

Which leads to:

$$
z'(t_e)=(1-\alpha)(\Lambda_0-1) \cdot \bar l^\alpha\cdot \frac{1}{[1+(\Lambda_o-1)t_e]^\alpha}
$$

And the condition for enclosure is:

$$
z^\prime(t_e)>c
$$

which is directly comparable to the private decision:

$$
r(t_e)>c
$$

We'd have to rewrite just a bit, but the basic logic remains the same:

- $z$ concave as long as $\theta>1$  (easy to show, but need online appendix demo)
- $z'(0)<c$ so zero enclosure $t_e=0$
- $z'(1)>c$ so full enclosure $t_e=1$
- $z'(0)>c$ and $z'(1)<c$ so interior optimum $t_e$

All the loci expressions are derived same way (e.g. from $z'(0)<c$)

## Observation on Global games

I was playing around with some visualizations and it seems pretty clear 



## Move conditional optimality section down

My suggestion is to move this second-best/conditional optimality section until later.  It's present virtue is that several expressions (e.g. $l_e^*(t_e)$) are re-used in the private enclosure but I feel it's present location is a bit of a distraction:

- The primary comparison is between the first-best social and the private enclosure decisions.  Why not jump right into that comparison? 
- We don't really do much with the conditional optimal loci right now even though they are some of the more complicated expressions in the paper which complicate/distract right before we're about to deliver the punchlines of the paper.
- We might draw more interesting discussion moving this discussion later in the paper.  The most interesting aspect about it is that it seems to point to a more 'practical' policy - govt decides on frontier line but doesn't try to regulate. For that reason maybe leave it for later when we discuss policy and environment issues (lots of good econ history to tie it too).  



Relation $z$, $z^*$, $r$

From section on conditional optimality we have:
$$
z^*(t_e)= \bar l^\alpha \frac{1+(\frac{\Lambda}{\alpha}-1)t_e}{(1+(\Lambda -1)t_e)^{\alpha}}
$$
Let's try to get this to look a bit more like 



# 
$$
\theta F_T(t_e, l_e) \ge c +F_T(t_c,l_c)-\theta F_L(t_e,l_e)\frac{dl_e}{dt_e}+F_L(t_c,l_c)\frac{dl_e}{dt_e}
$$


## Appendix

All key equations are stated or derived here. 

$$
T_e+T_c=\bar T \\
L_e+L_c=\bar L
$$

We define shares of land and labor in the enclosed sector as: $t_e=\frac{T_e}{\bar T}$ and $l_e=\frac{L_e}{\bar L}$

**Production technology** $F(T_c, L_c)=T_c^{1-\alpha} \bar L_c ^{\alpha}$ in customary (unenclosed sector). Enclosed sector has potentially different TFP. 

$$
\begin{align}
   G(T_{e},L_{e}) &= \theta \cdot t_e^{1-\alpha} \bar l_e ^{\alpha} \cdot \bar T^{1-\alpha} \bar L ^{\alpha}\\
&=F(t_e,l_e)\cdot \theta F(\bar T, \bar L)\\
\end{align}
$$

Note also for later use that we can write:

$$
APT_e=\frac{F(T_e, L_e)}{T_e}= \bar l ^\alpha \cdot \left ( \frac{l_e}{t_e}  \right )^{\alpha}
$$

and

$$
MPT_e=(1-\alpha)\cdot \bar l ^\alpha \cdot \left ( \frac{l_e}{t_e}  \right )^{\alpha}
$$

because for Cobb-Douglas, $MPT_e=(1-\alpha)\cdot APT_e$​

### Socially Optimal

$$
Y(t_e,l_e)=\left[\theta\cdot F(t_e,l_e)+F(1-t_e,1-l_e)\right ]\cdot F(\bar T, \bar L)
$$

Planner wants to maximize social benefits net of enclosure costs

$$
\max_{t_e,l_e} Y(t_e,l_e)-ct_e\bar T
$$

We can divide each term above by $\bar T$ to express in per unit land terms.  Then purpose is to maximize:

$$
z(t_e,l_e)-ct_e = \bar l^\alpha [\theta t_e^{1-\alpha}l_e^\alpha 
+(1-t_e)^{1-\alpha} (1-l_e)^\alpha]-ct_e
$$

We break this into tow parts.  First find optimal labor-allocation $l_e^o(t_e)$​​​​ for any given $t_e$​​​​, then search over $t_e$​ to find the optimal enclosure rate.  This approach makes it easier to compare to equilibria in the decentralized cases.  The FOC for optimal labor allocation implies equalization of marginal products across sectors.

$$
\alpha\theta \left ( \frac{t_e}{l_e} \right ) ^{1-\alpha} = \alpha \left ( \frac{1-t_e}{1-l_e} \right ) ^{1-\alpha}
$$

Solving for $l_e$ as a function of $t_e$:

$$
l_e^o(t_e) = \frac{\Lambda_o t_e}{1+(\Lambda_o-1)t_e}, \quad \text{where }\Lambda_o=\theta^{\frac{1}{1-\alpha}}
$$

Substituting this back into $z(t_e)=z(t_e, l_e^o(t_e))$​ we have:

$$
\begin{aligned}
z(t_e) &= \bar l^\alpha \cdot (A + B)  \\
  &= \theta t_e^{1-\alpha}
\left (\frac{\Lambda_o t_e}{1+(\Lambda_o-1)t_e}  \right)^\alpha \\ 
&+ (1-t_e)^{1-\alpha} 
\left ( 1-\frac{\Lambda_o t_e}{1+(\Lambda_o-1)t_e}   \right)^\alpha]     
\end{aligned}
$$

To simplify, note that $A$​​ can be simplified to

$$
\frac{\theta t_e\cdot \Lambda_0^\alpha}{(1+(\Lambda_o-1)t_e)^\alpha}
$$


Now note that  $\theta \cdot \Lambda_0^\alpha=\theta \cdot \theta^\frac{\alpha}{1-\alpha}=\theta^\frac{1}{1-\alpha}=\Lambda_o$ ​​​ so we can further simplify $A$​​​ to:

$$
\frac{t_e\cdot \Lambda_0}{(1+(\Lambda_o-1)t_e)^\alpha}
$$

Meanwhile $B$​ can be written

$$
\frac{1-t_e}{(1+(\Lambda_o-1)t_e)^\alpha}
$$

And hence 

$$
A+B=\frac{1+(\Lambda_o-1)t_e}{(1+(\Lambda_o-1)t_e)^\alpha}=(1+(\Lambda_o-1)t_e)^{1-\alpha}
$$

And $z(t_e)$  becomes:

$$
z(t_e) = \bar l^\alpha \cdot (1+(\Lambda_o-1)t_e)^{1-\alpha}
$$

The marginal benefit of increasing enclosure is then:

$$
z'(t_e)=(1-\alpha)\bar l^\alpha \frac{(\Lambda_o - 1)}{(1+(\Lambda_o-1)t_e)^\alpha}
$$

###  Social Enclosure decisions

When $\theta \ge 1$​ (so $\Lambda^o \geq 1$​) then $z(t_e)$​ is concave in $t_e$​ and we can use the derivative of $z(t_e)$​ assessed at each endpoint to see whether land enclosure should be zero, partial, or full.

|              Regime               |  Condition  |                           Boundary                           |
| :-------------------------------: | :---------: | :----------------------------------------------------------: |
| **No Enclosure** <br />$t_e^o=0$​  |   z'(0)<0   | $\bar l \le \left[\frac{c}{(1-\alpha)\left(\Lambda^o-1\right)}\right]^{\frac{1}{\alpha}}=l_0^o(c,\theta)$ |
| **Full Enclosure**<br />$t_e^o=1$​ |   z'(1)>c   | $\bar l \geq \left[\frac{c \Lambda^o}{(1-\alpha)\left( \Lambda^o-1\right)}\right]^{\frac{1}{\alpha}}=l^o_1(c,\theta)$ |
|    **Partial Enclosure**<br />    | $z'(t_e)=c$ |                                                              |

## Interior social enclosure

Solve $z'(t_e)=c$ for $t_e$:

$$
\bar l^\alpha (1-\alpha)(\Lambda_o - 1)=c{(1+(\Lambda_o-1)t_e)^\alpha}
$$

$$
\bar l [(1-\alpha)(\Lambda_o - 1)]^{1/\alpha}=c^{1/\alpha}(1+(\Lambda_o-1)t_e)
$$

$$
(\Lambda_o-1)t_e= \bar l \left ( \frac{(1-\alpha)(\Lambda_o - 1)}{c} \right )^{1/\alpha}-1
$$

$$
t_e= 
\frac{\bar l \cdot\left ( 
 {\frac{(1-\alpha)(\Lambda_o-1)}{c}} \right)^{1/\alpha}-1}
 {(\Lambda_o-1)}
$$


$$
t_e= 
\bar l \cdot (\Lambda_o-1)^\frac{1-\alpha}{\alpha} 
\cdot \left ( 
\frac{(1-\alpha)}{c} \right)^{1/\alpha}
-\frac{1}{\Lambda_o-1}
$$


This could be further simplified perhaps but we'll leave it at this.

|           Regime            |  Condition  |                           Boundary                           |
| :-------------------------: | :---------: | :----------------------------------------------------------: |
| No Enclosure <br />$t_e=0$  |   z'(0)<0   | $\bar l \le \left[\frac{c}{(1-\alpha)\left(\Lambda^o-1\right)}\right]^{\frac{1}{\alpha}}=l_0^o(c,\theta)$ |
| Full Enclosure<br />$t_e=1$ |   z'(1)>c   | $\bar l \geq \left[\frac{c \Lambda^o}{(1-\alpha)\left( \Lambda^o-1\right)}\right]^{\frac{1}{\alpha}}=l^o_1(c,\theta)$ |
|      Partial Enclosure      | $z'(t_e)=c$ |                             n.a.                             |
|                             |             |                                                              |

## Interior enclosure

From the condition 

$$
\alpha\theta\left(\frac{t_e}{l_e}\right)^{1-\alpha}
    =\left(\frac{1-t_e}{1-l_e}\right)^{1-\alpha}
$$

From which we can solve for

$$
l_e^*(t_e) = \frac{\Lambda t_e}{1+(\Lambda-1) t_e } , \quad \Lambda(\theta)=(\alpha\theta)^\frac{1}{1-\alpha}
$$

Private actors enclose when $r(t_e)>c$

$$
(1-\alpha)\cdot \theta \cdot \bar l ^\alpha \cdot \left ( \frac{l_e^*(t_e)}{t_e}  \right )^{\alpha}>c
$$

Substitute in 

$$
r(t_e)={\theta}\cdot(1-\alpha)\cdot \bar l^{\alpha}
\cdot \left ( \frac{\Lambda}{(1+(\Lambda -1)t_e)} \right)^\alpha >c
$$

**Interior**

$$
{\theta}\cdot(1-\alpha)\cdot \bar l^{\alpha}
\cdot  \frac{\Lambda^\alpha}{(1+(\Lambda -1)t_e)}  =c
$$

$$
c(1+(\Lambda -1)t_e)^\alpha={\theta}\cdot(1-\alpha)\cdot \bar l^{\alpha} \cdot  {\Lambda^\alpha}  
$$

$$
c^{1/\alpha}(1+(\Lambda -1)t_e)=[{\theta}\cdot(1-\alpha)]^{1/\alpha}\cdot \bar l \cdot  {\Lambda}  
$$


$$
t_e=  \bar l \cdot  \frac{\Lambda}{\Lambda-1} \cdot \left [\frac{{\theta}\cdot(1-\alpha)}{c} \right]^{1/\alpha} 
- \frac{1}{\Lambda-1}
$$


## When is there too much or too little enclosure

Too much enclosure $z'(t_e)<r(t_e)$

$$
\frac{(\Lambda_o - 1)}{(1+(\Lambda_o-1)t_e)^\alpha}
<{\theta}
\cdot \left ( \frac{\Lambda}{(1+(\Lambda -1)t_e)} \right)^\alpha
$$

$$
\frac{(\Lambda_o - 1)^{1/\alpha}}{(1+(\Lambda_o-1)t_e)}
<{\theta^{1/\alpha}}
\cdot  \frac{\Lambda}{(1+(\Lambda -1)t_e)} 
$$


Let's solve for the boundary:

$$
\frac{ \left [ (1-\alpha)\theta \right]^{1/\alpha}\Lambda\bar l-c^{1/\alpha}}{c^{1/\alpha}(\Lambda-1)}
$$

