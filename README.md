# ThermodynamicsEntropyExample

This was made in conjunction with my essay for the Tottenham Phoenix, please read it to understand.

The program asks you for 4 variables, atoms in Bar A, atoms in Bar B, energy packets in Bar A, energy packets in Bar B

Make sure that all of these are not 0, the number of energy packets are less than the number of atoms and Bar A has more packets than Bar B.

Once you have entered all of the data, there will be a file called distribution.png. Make sure to click on it. It shows you a much more digestible form of the data, through the use of a distribution graph.

The maths for those interested (Not Essential):

m1 and m2 are atoms in Bars A and B respectfully, e1 and e2 are the energy packets in Bars A and B. mt and et are the sum of the two quantities

When the numbers is small (binomial approximation):
states where e1 has increased = sum(m1Cn x m2C(et - n)) for n = e1 + 1 to et (or mt, which ever is smaller)
total states = mtCet
probability = states where e1 has increased / total states

When the numbers is large (Poisson Approximation in conjunction with the Sterling)

Poisson: Models it as a Poisson with lambda = et * m1 / mt 
Finds probability using scipy to find P(A>e1)

Sterlings formula = log10(et!) ≈ et(ln *et) - n + 0.5 * et * ln(2 * et * pi)
Using logs to find order of magnitude: log10(et!) ≈ et * log10(et) - et / log(10) + 0.5 * log10(2 * et * pi)
Order of Magnitude for total states: et * log10(mt)) - log10(et!)

Order of magnitude of states where e1 increases = Order of Magnitude for total states + Order of Magnitude of the probability
