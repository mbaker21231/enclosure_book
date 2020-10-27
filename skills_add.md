## Differentiated Skills

In the model analyzed thus far all producers within the agricultural sector have similar skill and access to production technologies.  That model highlighted misallocation that could arise within the agricultural sector, but that was due fundamentally to a misallocation between enclosed and unenclosed subsectors.  There was equalization of MPLs within these subsectors, but non-equalization between subsectors.   

What follows are some notes on how to extend the model in the direction of realism by allowing for differentiation among producers within the agricultural sector and the possibility of misallocations arising within subsectors due to the imperfect operation of land and or labor markets there. 

A substantial literature emphasizes the role of non-traded skills in production and the considerable differentiation observed in practice.  The more differences there are between producers within a community, the more important it will be to have mechanisms such as active land rental and labor wage markets to allow access to resources to more productive farm managers, regardless of who holds claim to the resources.  Several studies have suggested that insecurity of property rights within communities may contribute to repress the operation of land lease markets, leading to possibly serious misallocation of resources.  

Here are some notes on extending the model to incorporate such considerations. 

We add a non-traded farm management skill $S$ to now use a linear homogenous production as follows: 

$$
F(S_i,T_i,L_i)=S_i^{1-\gamma} \left [T_i^{1-\alpha}L_i^\alpha     \right]^\gamma
$$
and we will assume that non-traded farming skill $S_i$ varies by household.  This will give us a Lucas {cite}`lucas1978` span-of-control type model with efficient farm size determined by the household's managerial skill, and 'profits' in this model are interpreted as a rent to this non-traded skill.   

In our simpler model, without skill we were able to write $APL=\left (\frac{T_i}{L_i} \right)^{1-\alpha}$ and $MPL=\alpha APL$. With skill in the production we can now write: 


$$
APL=\frac{F(S_i,T_i,L_i)}{L_i}=
\left ( \frac{S_i}{L_i} \right )^{1-\gamma}
\cdot
\left ( \frac{T_i}{L_i} \right )^{(1-\alpha)\gamma}
$$


And $MPL=\gamma\alpha \cdot APL$.  The $\gamma=1$ corresponds to the earlier model without any  role for skill.

It's easy to show than an efficient allocation will require the mobile factors of production (land, labor) allocated to farms in proportion to the skill level of the farm managers:

$$
T_i=\frac{S_i}{\mathbf S}\cdot \bar T \\  L_i=\frac{S_i}{\mathbf S} \cdot \bar L
$$
where $\mathbf S = \sum S_i$

This can be verified by substituting this into the formulas for $MPL_i$ and verifying that this equalizes the $MPL_i$ (and the $MPT_i$) across farms to a common value of:
$$
MPL^e=\gamma\alpha
\left ( \frac{\bar S}{\bar L} \right )^{1-\gamma}
\cdot
\left ( \frac{\bar T}{\bar L} \right )^{(1-\alpha)\gamma}
$$
In other words, an efficient allocation will require that the mobile factors land and labor be allocated to households in proportion to non-traded farming skill held by that household.  This model thus gives us a determinate efficient size distribution of farms and points to the need for land and labor factor markets (or other reallocation mechanisms) .  

Note also that with this Cobb-Douglas, $MPT = \gamma \cdot (1-\alpha) APT$:


$$
F_T = \gamma (1-\alpha) \cdot \frac{F}{T}
$$

### What changes?


Speculation: the more skilled would want to enclose earlier, generating interesting situations.  

This extension would be nice because it then allows us to talk to the 'misallocation' literatures that start from here and say the land rental market is malfunctioning and leading to misallocation.  We'd be potentially positioned to say that and more interesting things as well (e.g. political economy might be interesting...less productive farmers would stand to gain if they can now gain title to use-rights and then lease out land without fear to the more skilled... but maybe other considerations -- fallback subsistence land -- might play ar role.)


