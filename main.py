from math import comb
from scipy.stats import poisson, binom
import matplotlib.pyplot as plt
import matplotlib
import numpy as np
matplotlib.use('TkAgg') 

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

if mt < 1000 and et < 500: #if the numbers are small enough, the choice function works fine

    tempincreasestates = sum(comb(m1,min(m1-i,i)) * comb(m2,min(m2-et+i,et-i)) for i in range(E1+1,min(et+1,m1))) #the min function makes it less computationally intensive
    totalstates = comb(mt,et)
    p = tempincreasestates / totalstates
    
    label = 'Binomial Modelling'

    print(f'There are {tempincreasestates:g} total states where heat increases')
    print(f'There are {totalstates:g} states in total')
    print(f'There is a {p:g} chance of the temperature increasing')

else: #if they are too big, it defaults to poisson distribution
    lamd = et * Pop #lambda is total energy * percent of slots taken up by hot bar
    p = poisson.sf(E1,lamd) #calculates poisson distribution
    label = 'Poisson Modelling'

    print('Numbers too large to provide total states')
    print(f'Probability of heat increasing is {p:g}') 

x = np.arange(0, mt+1)
pmf = binom.pmf(x, mt, Pop)

plt.figure(figsize=(10,6))
plt.bar(x, p, alpha=0.7, label=label, color='blue')

# Shade area where A > E
shade_x = x[x > E1]
shade_pmf = pmf[x > E1]
plt.bar(shade_x, shade_pmf, alpha=0.7, color='red', label=f'{label}, A>{E1}')

# Labels and legend
plt.xlabel("Number of packets in Bar A")
plt.ylabel("Probability")
plt.title(f"{label} distribution (shaded: A>{E1})")
plt.legend()
plt.show()
