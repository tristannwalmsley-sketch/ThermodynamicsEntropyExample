from math import comb
from scipy.stats import poisson

def askparam():
    m1 = int(input('Enter the number of particles in the hot bar ->'))
    m2 = int(input('Enter the number of particles in the cold bar ->'))
    E1 = int(input('Enter the number of energy packets in hot bar ->'))
    E2 = int(input('Enter the number of energy packets in cold bar ->'))
    return m1,m2,E1,E2

m1,m2,E1,E2 = askparam()
while E2 > E1:
    print('The cold bar MUST have less energy packets than the hot bar')
    E2 = int(input('Enter the number of energy packets in cold bar'))

while E1>m1 or E2>m2:
    print('There must be less energy packets than number of atoms')
    m1,m2,E1,E2 = askparam()

mt = m1+m2
et = E1+E2
Pop = m1 / mt

if mt < 1000 and et < 500:
    tempincreasestates = sum(comb(m1,min(m1-i,i)) * comb(m2,min(m2-et+i,et-i)) for i in range(E1+1,et+1))
    totalstates = comb(mt,et)
    p = tempincreasestates / totalstates
    print(f'There are{tempincreasestates:g} total states where heat increases')
    print(f'There are{totalstates:g} states in total')
    print(f'There is a {p:g}chance of the temperature increasing')
else:
    lamd = et * Pop
    p = poisson.sf(E1,lamd)
    print('Numbers too large to provide total states')
    print(f'Probability of heat increasing is {p:g}')