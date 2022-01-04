# Partial Exclusivity

We've given two different (complementary) interpretations of the mis-allocation:
- **unregulated-access:** laborers continue to enter the unenclosed sector to capture rents, but this creates a negative externality in that it reduces the rents of others in the sector. 
- **insecure property rights**: land rights are established via possession and membership hence laborers migrate less for fear of losing land and rents.

The latter interpretation means that laborers migrate until they are indifferent between the higher wage in the enclosed sector and the lower wage but land perks in the customary sector:

$$
w_c + r_c \cdot \bar T_i = w_e
$$

Implicitly, land rights are not alienable -- the laborer cannot sell and cash out.

But suppose that when they move to the city or other opportunity they have probability $\mu > 0$ of retaining their use-rights. Or they can, in effect, lease out those rights and get paid some fraction of the rents they'd capture had they stayed.  Then the relation becomes:

$$
w_c + r_c \cdot \bar T_i = w_e + \mu r_c \cdot T_i
$$

If $\mu=0$​ we have the model described in the paper. If $\mu=1$ then land becomes exclusive/alienable, and the villager can move to the city without losing land rental income streams (i.e. they can sell or lease out their land).  In this latter case efficiency would be restored.

Rearranging: 

$$
w_c + (1-\mu) \cdot r_c \cdot \frac{T_c}{L_c}=w_e
$$

This way of writing things might line up with a **regulated commons** view.  Instead of unregulated access, those who live and use land in the community are subject to a user-tax (like a Pigouvian tax) $\mu$  (where do the revenues go?)

Under either interpretation, note from Euler's theorem that $F(L_c, T_c) = F_L \cdot L_c + F_T \cdot T_c$ and so we can write: 

$$
APL = \frac{F}{L_c}=F_L + F_T \cdot \frac{T_c}{L_c}
$$

Note we can write $F_T=(1-\alpha)\frac{F}{T}$ and therefore 

$$
(1-\mu) \cdot F_T \cdot \frac{T}{L}= (1-\mu)(1-\alpha)\frac{F}{L}
$$

Hence a laborer's earnings in the commons is:

$$
F_L+(1-\mu) \cdot F_T \cdot \frac{T}{L}=\alpha \frac{F}{L}
+(1-\mu)(1-\alpha)\frac{F}{L}
$$

Gathering terms and rearranging the relevant FOC is now

$$
[\alpha +(1-\mu)(1-\alpha)]APL_c=MPL_e
$$

Or

$$
[1-\mu\cdot(1-\alpha)]APL_c=MPL_e
$$

Note that when $\mu=1$ we get the efficient $MPL_c=MPL_e$ and when $\mu=0$ we get the case analyzed in the paper where $APL_c=MPL_e$.

For any $\mu\in(0,1)$ we instead have this FOC:

$$
\alpha  \theta \left ( \frac{t_e}{l_e} \right ) ^{1-\alpha} = (1-\mu(1-\alpha)) \cdot\left ( \frac{1-t_e}{1-l_e} \right ) ^{1-\alpha}
$$


This will look very similar to everything from before


$$
l_e^p(t_e) = \frac{\Lambda^p t_e}{1+(\Lambda^p-1) t_e }
$$

But with 

$$
\Lambda^p=\left ( \frac{\alpha\theta}{1+\mu \cdot (1-\alpha)}  \right)^\frac{1}{1-\alpha}
$$
