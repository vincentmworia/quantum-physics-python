from itertools import count
import matplotlib.pyplot as plt
import numpy as np

h = 1
m = 1

a = 1
V = 0

x = 0
psi = 1
dx = a * 0.01

E = 0
dE = 0.01

nmax = 3
counter = 1  # Used to count eigenfunctions during computation

xlist = []
psilist = []
eigenfunctions = []
eigenfunctionsxList = []
eigenEnergies = []

# Compute eigenfunctions
while counter <= nmax:
    psi = 1

    while abs(psi) > 0.001:
        psi = 0
        x = 0
        dpsi = 1
        E = E + dE
        xlist = []
        psilist = []
        # if abs(psi) <= 0.001:
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
    # Ensure that the eigenvalue step increases appropriately
    E = E * 1.1

# print('EigenEnergies: ', eigenEnergies)
print('Eigenfunctions OLD: ', eigenfunctions)
# print('EigenfunctionsxList: ', eigenfunctionsxList)

# todo NORMALIZATION OF INDIVIDUAL WAVES
# normalization condition is integrate the eqn
# Integration is the small values multiplied by the increments


# Normalize all eigenfunctions
for i in range(len(eigenfunctions)):
    # Compute normalization constant for the i-th eigenfunction
    normConstant = np.dot(eigenfunctions[i], eigenfunctions[i]) * dx
    # Normalize the eigenfunction by dividing each value
    for j in range(len(eigenfunctions[i])):
        eigenfunctions[i][j] = eigenfunctions[i][j] / np.sqrt(normConstant)

# Verify normalization of the third eigenfunction
normConstantNew = np.dot(eigenfunctions[0][0], eigenfunctions[0][0]) * dx
print(normConstantNew) # Should be 1
print('Eigenfunctions NEW: ', eigenfunctions)

# Plotting the eigenfunctions
counter = 0  # Reset counter to align with zero-based inde
# xing of eigenfunctions
while counter < len(eigenfunctions):
    plt.plot(eigenfunctionsxList[counter], eigenfunctions[counter], label=f"Eigenfunction {counter + 1}")
    counter += 1

plt.xlabel("x")
plt.ylabel("psi")
plt.title("Eigenfunctions of Particle in a Box")
plt.legend()  # Show legend to distinguish the curves
plt.grid(True)  # Add gridlines for better readability
plt.show()
