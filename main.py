import math
from scipy.stats import poisson, binom
import matplotlib.pyplot as plt
import matplotlib
import numpy as np
matplotlib.use('Agg') 

def askparam(): #asks for the parameters
    while True:
        try:
            m1 = int(input('Enter the number of particles in the hot bar ->'))
            m2 = int(input('Enter the number of particles in the cold bar ->'))
            E1 = int(input('Enter the number of energy packets in hot bar ->'))
            E2 = int(input('Enter the number of energy packets in cold bar ->'))
            return m1,m2,E1,E2
        except:
            print('Must be a whole, non zero number')

m1,m2,E1,E2 = askparam()
while E2 > E1:
    print('The cold bar MUST have less energy packets than the hot bar')
    E2 = int(input('Enter the number of energy packets in cold bar'))

while E1>m1 or E2>m2:
    print('There must be less energy packets than number of atoms')
    m1,m2,E1,E2 = askparam()

mt = m1+m2 #total number of atoms
et = E1+E2 #total number of energy packets
Pop = m1 / mt #percent of decimals taken up by bar 1

x = np.arange(0, et+1)
plt.xlim(0, min(m1+mt//10,et))


try: #normally does binomial
    #the min function makes it less computationally intensive
    tempincreasestates = sum(comb(m1,min(m1-i,i)) * comb(m2,min(m2-et+i,et-i)) for i in range(E1+1,min(et+1,m1))) 
    totalstates = comb(mt,et) 
    p = tempincreasestates / totalstates
    
    label = 'Binomial Modelling'

    pmf = binom.pmf(x, et, Pop)

    print(f'There are {tempincreasestates:g} total states where heat increases')
    print(f'There are {totalstates:g} states in total')
    print(f'There is a {p:g} chance of the temperature increasing')

    stats_text = (
        f"Useful States = {tempincreasestates:g}\n"
        f"Total States = {totalstates:g}\n"
        f"P(A > {E1}) = {p:g}"
    )

except: #if they are too big, it defaults to poisson distribution
    lamd = et * Pop #lambda is total energy * percent of slots taken up by hot bar
    p = poisson.sf(E1,lamd) #calculates poisson distribution
    label = 'Poisson Modelling'
    pmf = poisson.pmf(x,lamd)

    # symmetry: C(mt, et) = C(mt, mt-et)
    et = min(et, mt - et)

    # Stirling-based approximation
    totalstatesapprox = int(round(
        et * math.log10(mt)
        - (et * math.log10(et) - et / math.log(10) + 0.5 * math.log10(2 * math.pi * et)),0
    ))

    tempincreasestatesapprox = int(round(totalstatesapprox + math.log(p),0))
    approx = "\u2248"

    print('Numbers too large to provide total states')
    print(f'Probability of heat increasing is {p:g}') 

    stats_text = (
        f"Useful States {approx} 1e{tempincreasestatesapprox}\n"
        f"Total States {approx} 1e{totalstatesapprox}\n"
        f"P(A > {E1}) = {p:g}\n"
    )




plt.figure(figsize=(10,6))

# Shade area where A > E
shade_x = x[x > E1]
shade_pmf = pmf[x > E1]
plt.bar(x,pmf, alpha=0.7, color = 'grey')
plt.bar(shade_x, shade_pmf, alpha=0.7, color='red', label=f'Values where Bar A energy>{E1}')


# Add box (axes coords: 0–1)
plt.text(
    0.98, 0.95, stats_text,
    transform=plt.gca().transAxes,
    fontsize=10,
    verticalalignment='top',
    horizontalalignment='right',
    bbox=dict(boxstyle="round", facecolor="white", alpha=0.85))

# Labels and legend
plt.xlabel("Number of packets in Bar A")
plt.ylabel("Probability")
plt.title(f"{label}")
plt.legend()
plt.savefig("distribution.png", dpi=150, bbox_inches="tight")
plt.close()
