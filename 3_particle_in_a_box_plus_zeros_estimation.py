from itertools import count

import matplotlib.pyplot as plt
from time import sleep

h = 1
m = 1

a = 1
V = 0

x = 0
psi = 1
dx = a * 0.01

E = 0
dE = 0.01

nmax = 2
counter = 0

xlist = []
psilist = []
eigenfunctions = []
eigenfunctionsxList = []
eigenEnergies = []

while counter < nmax:
    psi = 1

    while abs(psi) > 0.001:
        psi = 0
        x = 0
        dpsi = 1
        E = E + dE
        xlist = []
        psilist = []

        while x <= a:
            ddpsi = 2 * (m / h ** 2) * (V - E) * psi
            dpsi = dpsi + ddpsi * dx
            psi = psi + dpsi * dx
            x = x + dx
            xlist.append(x)
            psilist.append(psi)
    eigenfunctions.append(psilist)
    eigenfunctionsxList.append(xlist)
    eigenEnergies.append(E)
    counter += 1
    # todo the code below ensures that we increase our eigen value enough such that
    #  in case we get an eigenvalue, it is not repeated but rather we get the next value
    E=E*1.1


plt.plot(xlist, psilist)
plt.xlabel("x")  # Add labels for clarity
plt.ylabel("psi")
plt.title("Wavefunction")  # Add a title
plt.show()

print('EigenEnergies: ', eigenEnergies)
print('Eigenfunctions: ', eigenfunctions)
print('EigenfunctionsxList: ', eigenfunctionsxList)
