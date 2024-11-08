import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from scipy.integrate import solve_ivp
from matplotlib.offsetbox import (OffsetImage, AnnotationBbox)
from matplotlib import colors

st.set_page_config(layout="wide")

import modules.nav
modules.nav.Navbar()


""" 
# Model lišky ostrovní
"""

c1,c2 = st.columns(2)

with c1:
    """
    ![](https://upload.wikimedia.org/wikipedia/commons/thumb/3/31/Island_Fox_%2839100105000%29.jpg/800px-Island_Fox_%2839100105000%29.jpg)
    """

with c2:
    r"""
   

Liška ostrovní (*Urocyon littoralis*) je jedinečný živočišný druh, endemit žijící jenom na ostrůvcích okolo Kalifornie. Vlivem činnosti člověka se její populace dostala do velkých potíží. Na ostrově San Miguel klesla populace z 450 dospělých jedinců v roce 1994 na 15 v roce 1999. Podobná situace byla i na ostatních ostrovech, z nichž každý je osídlen samostatným poddruhem lišky ostrovní. Dříve vrcholný predátor na ostrově se stal najednou kořistí a byl těsně před vyhubením. Naštěstí se podařilo situaci pro lišku zachránit, zajistit podmínky ve kterých je populace stabilní a populaci lišek opětovně rozmnožit. Nyní je liška ostrovní „pouze“ téměř ohrožená. Jedná se o jeden z nejúspěšnějších záchranných programů pro savce. Komplexní program zahrnoval vybití divokých prasat, přesídlení orlů skalních, návrat orlů bělohlavých, umělé rozmnožení lišek, jejich návrat do přírody a jejich vakcinaci proti zavlečeným chorobám. To vše za jednu dekádu.

Následující model se snažil vysvětlit, jak zdivočelá prasata a orli příspívají k tomu, že liška ostrovní se z predátora stane kořistí stojící na pokraji vyhubení. *(Obrázek <https://commons.wikimedia.org/wiki/File:Island_Fox_%2839100105000%29.jpg>, autor Caleb Putnam)*

Model populace lišky, orla, prasete a skunka je převzat z publikace [Golden eagles, feral pigs, and insular carnivores: How exotic species turn native predators into prey](https://www.pnas.org/doi/10.1073/pnas.012422499#F3) a má tvar soustavy diferenciálních rovnic
$$
\begin{aligned}
\frac{\mathrm dF}{\mathrm dt} & =
r_f F \left(1-\frac{F+\beta_{fs}S}{K_f}\right) - \mu_f \frac{\phi F}{\phi F+\sigma S+P} EF,\\
\frac{\mathrm dS}{\mathrm dt} & =
r_s S \left(1-\frac{S+\beta_{sf}F}{K_s}\right) - \mu_s\frac{\sigma S}{\phi F+\sigma S+P}ES,\\
\frac{\mathrm dP}{\mathrm dt} & =
r_p P \left(1-\frac P{K_p}\right) - \mu_p \frac P{\phi F+\sigma S+P} EP,
\\
\frac{\mathrm dE}{\mathrm dt} & =
\frac{(\lambda_f \mu_f\phi F^2+\lambda_s\mu_s\sigma S^2+\lambda_p \mu_p P^2) E}{\phi F+\sigma S+P} - \nu E,
\end{aligned}
$$
kde $F$, $S$, $P$, a $E$ jsou velikosti populací lišek, skunků, prasat a orlů skalních.

"""

cc1,cc2 = st.columns(2)

with cc1:
    "Parametry"

def rovnice(t, X):
    # Podle Roemer, Donlan, Courchamp, Golden eagles, feral pigs and insular carnivores: How exotoc species turn native pre
    F,S,P,E = X
    r_f = 0.32
    r_s = r_f
    r_p = 0.78
    beta_fs = 181.58/500.48
    beta_sf = 500.48/181.58
    mu_f = 0.086
    mu_s = 0.159
    mu_p = 0.019
    phi = 8.1
    sigma = 3.1
    K_f = 1544
    K_s = 2490
    K_p = 15189
    lambda_f = 7.7e-4
    lambda_s = 2.5e-4
    lambda_p = 7.7e-4
    nu = 0.09
    dF = r_f*F*(1-(F+beta_fs*S)/K_f) - mu_f*phi*F/(phi*F+sigma*S+P)*E*F
    dS = r_s*S*(1-(S+beta_sf*F)/K_s) - mu_s*sigma*S/(phi*F+sigma*S+P)*E*S
    dP = r_p*P*(1-P/K_p) - mu_p*P/(phi*F+sigma*S+P)*E*P
    dE = (lambda_f*mu_f*phi*F**2+lambda_s*mu_s*sigma*S**2+lambda_p*mu_p*P**2)*E/(phi*F+sigma*S+P) - nu*E
    return [dF,dS,dP,dE]

pocatecni_podminky = [
    [500,250,50,10],
    [500,400,0,10]
    ]
meze = [0,100]
labels = ["liška","skunk","prase","orel"]
t=np.linspace(*meze, 500)  # graf reseni

reseni = [solve_ivp(
                   rovnice,
                   meze,
                   pocatecni_podminka,
                   t_eval=t,
                   ).y
          for pocatecni_podminka in pocatecni_podminky ]
reseni = np.array(reseni)  # převod na array knihovny numpy
a,b,c = reseni.shape       # zjištění rozměrů
reseni = reseni.reshape(a*b,c)
df = pd.DataFrame(
        reseni.T,
        columns=pd.MultiIndex.from_product([["s prasaty","bez prasat"],labels],names=["scenar","populace"])
)
df.index = t
df.index.name = "čas"

with cc2:
    st.dataframe(df)
