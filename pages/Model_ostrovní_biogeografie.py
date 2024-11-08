import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp
import pandas as pd
pd.options.plotting.backend = "plotly"


"""
# Model ostrovní biogeografie
"""

text = r"""

Životní prostředí podléhá neustálým změnám, ať už vlivem činnosti člověka či
vlivem jiných aspektů. V důsledku toho jsou některé živočišné či rostlinné druhy
ohroženy, jiné vymírají a jiné se naopak začínají více a více prosazovat. K
pochopení tohoto procesu může pomoci i *ostrovní ekologie*. 
Z hlediska pevniny jsou totiž ostrovy relativně nestálá a
neustále se vyvíjející společenstva, vysoce citlivá na vnější zásahy, na kterých
je možno sledovat vývoj jednotlivých druhů, jejich stability, rozmanitosti a
pod. Principy ostrovní ekologie se nevztahují pouze na ostrovy v zeměpisném
slova smyslu. Jde o jakýkoliv habitat oddělený od okolí. Například vrcholky hor
jsou ostrovy v moři stanovišť s menší nadmořskou výškou, parky jsou ostrovy
zeleně v moři městské zástavby, lesy jsou ostrovy v zemědělsky využívané
krajině, živočichové jsou ostrovy pro parazity na nich žijící a podobně.
Ostrovní ekologie je tedy nedílnou součástí ekologie jako celku i u
vnitrozemských států.

R. H. Mac Arthur a E. O. Wilson představili v 60. letech 20. stol. 
teorii dynamické rovnováhy počtu druhů na ostrově. Tato teorie získala veliký
ohlas a oba vědce proslavila mezi ekology, protože vysvětlovala fenomény spojené
s dynamikou populací na ostrovech, jako souvislost druhové rozmanitosti se
vzdáleností a rozlohou ostrova.  Vzhledem k možnostem aplikací teorie i na
"ostrovy" v přeneseném smyslu tohoto slova se teorie Mac Arthura a Wilsona stala
základním stavebním kamenem moderní krajinné ekologie.

Uvažujme ostrov, nacházející se relativně nedaleko pevniny -- takový,
že na něj mohou z pevniny migrovat nové druhy (větrem, přes moře,
v trusu ptáků a pod.), které na ostrově dosud nežijí. Tyto druhy se na
ostrově buď uchytí nebo neuchytí. V případě, že se druh úspěšně uchytí
a kolonizuje ostrov, může tato kolonizace být na úkor druhů jiných,
které následkem tohoto vymřou. Protože pevnina má mnohem větší nosnou
kapacitu než ostrov, slouží jako jistá zásobárna nových druhů pro
uvažovaný ostrov a ostrov je tedy neustále pod vlivem imigrace.
Protože ostrov má menší nosnou kapacitu, než mnohem rozlehlejší a
bohatší pevnina, může na něm trvale žít méně druhů než na pevnině.
"""

matematicky_model = r"""
Předpokládejme, že rychlost kolonizace, tj. počet druhů, které v čase
$t$ proniknou na ostrov a úspěšně se zde zabydlí, roste s počtem
imigrantů a klesá s počtem druhů, které na ostrově  již žijí. První
předpoklad je zcela přirozený, druhý vyjadřuje v ekologii obvyklé
tvrzení, že komplexnější společenstva organismů jsou stabilnější a lépe
odolávají invazi nových druhů. Počet imigrantů klesá s rostoucí
vzdáleností ostrova od pevniny, což je opět přirozený  předpoklad.
Uvedené předpoklady splňuje funkce
$$
 \frac b{D(N+\beta)},
$$
kde $N$ je počet druhů na ostrově v čase $t$, $D$ je vzdálenost ostrova od
pevniny, $\beta$ je nezáporná a  $b$ kladná konstanta. Rychlost kolonizace souvisí i s rozlohou ostrova. Tato veličina by
se dala včlenit například do parametru $D$, který by potom nevyjadřoval
vzdálenost, ale vhodným způsobem by zohledňoval společný vliv vzdálenosti a
velikosti ostrova.

Předpokládejme, že rychlost vymírání  druhů, které v minulosti již úspěšně
kolonizovaly ostrov, ale neobstály v konkurenci pozdějších kolonizátorů,
roste s klesající rozlohou ostrova a s rostoucím počtem druhů na
ostrově. Tento předpoklad
je opět přirozený, vzhledem k tomu, že ostrov menší rozlohy má menší nosnou
kapacitu. Kromě toho, byl tento předpoklad prověřen i pokusy. Rychlost vymírání druhů je možné modelovat funkcí
$$
 a\frac {N^k}S,
$$
kde $S$ je rozloha ostrova a $a$ a $k$ jsou kladné konstanty.


Nyní budeme pohlížet na rychlost s jakou se mění počet druhů na ostrově ze dvou
hledisek a tato hlediska nám pomůžou sestavit matematický model pro popis
dynamiky ostrova. 

* Rychlost s jakou se mění počet druhů na ostrově je derivace počtu druhů podle
  času. To je přímo význam derivace podle času.
  $$
  \frac{\mathrm dN}{\mathrm dt}
  $$
* Rychlost s jakou se mění počet druhů na ostrově je také změna počtu druhů za
  jednotku času. Tato změna se vypočítá jako rozdíl počtu druhů, které ostrov za
  jednotku času kolonizovaly a počtu druhů, které na ostrově za tuto dobu
  vymřely. Tedy půjde o rozdíl rychlosti kolonizace a rychlosti vymírání.
  $$
    \frac b{D(N+\beta)}-a\frac {N^k}S.
  $$

V předchozích bodech jsme dvakrát z různých pohledů představili stejnou veličinu
a proto se oba výrazy musí rovnat. Počet druhů na ostrově rozlohy $S$ ve
vzdálenosti $D$ od pevniny tedy vyhovuje diferenciální rovnici
$$
  \frac{\mathrm dN}{\mathrm dt}= \frac b{D(N+\beta)}-a\frac {N^k}S.
$$
Předpokládáme-li, že na počátku byl ostrov neosídlený, připojíme
podmínku $N(0)=0$.
"""


c1 ,c2 = st.columns(2)

with c1:
    text
with c2:
    "![Mangorovové ostrůvky na Okinavě](https://upload.wikimedia.org/wikipedia/commons/thumb/7/75/Mangrove_swamp%2C_Iriomote_Island%2C_Okinawa%2C_Japan.jpg/800px-Mangrove_swamp%2C_Iriomote_Island%2C_Okinawa%2C_Japan.jpg?20150819055702)"

c1 ,c2 = st.columns(2)

with c1:
    tmax = st.number_input("Konec času", value=20)
    D = st.slider("Vzdálenost ostrova od pevniny", min_value=0.01, value=1., max_value=2., step=0.01)
    S = st.slider("Rozloha ostrova", min_value=1., step=0.1, max_value=50., value=20.)

pocatecni_podminka = [0]
meze = [0,tmax]

t = np.linspace(*meze, 500) # časy ve kterých určíme hodnotu řešení
def rovnice(t, N, a=1, b=8, beta=0.2, D=0.5, k=1.3, S=20):
    return b/(D*(N+beta)) - a*N**k/S

reseni = solve_ivp(lambda t,N: rovnice(t,N, D=D, S=S),
                   meze,
                   pocatecni_podminka,
                   t_eval=t,
                   )
df = pd.DataFrame(reseni.y.T, index=reseni.t, columns=["Počet druhů"])
df.index.name = "Čas"

fig = df.plot()

with c2:
    st.plotly_chart(fig)

# plt.plot(reseni.t, reseni.y.T)
# ax = plt.gca()
# ax.set(
#     xlabel="čas",
#     ylabel="počet druhů",
#     title="Dynamika počtu druhů na ostrově"
# )
# ax.grid();

matematicky_model
