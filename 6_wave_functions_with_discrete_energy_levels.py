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

nmax = 5
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



# Normalize all eigenfunctions
for i in range(len(eigenfunctions)):
    # Compute normalization constant for the i-th eigenfunction
    normConstant = np.dot(eigenfunctions[i], eigenfunctions[i]) * dx
    # Normalize the eigenfunction by dividing each value
    for j in range(len(eigenfunctions[i])):
        eigenfunctions[i][j] = eigenfunctions[i][j] / np.sqrt(normConstant)

# Verify normalization of the first eigenfunction
normConstantNew = np.dot(eigenfunctions[0], eigenfunctions[0]) * dx
print(normConstantNew)  # Should be 1
print('Eigenfunctions NEW: ', eigenfunctions)

# # Plotting the eigenfunctions
# counter = 0  # Reset counter to align with zero-based indexing of eigenfunctions
# while counter < len(eigenfunctions):
#     plt.plot(eigenfunctionsxList[counter], eigenfunctions[counter], label=f"Eigenfunction {counter + 1}")
#     counter += 1


# todo Scaling up
for i in range(len(eigenfunctions)):
    shifted_psi = eigenEnergies[i] + np.array(eigenfunctions[i])
    plt.plot(eigenfunctionsxList[i], shifted_psi, label=f"Eigenfunction {i + 1} at E={eigenEnergies[i]:.2f}")

plt.xlabel("x")
plt.ylabel("psi")
plt.title("Eigenfunctions of Particle in a Box")
plt.legend()  # Show legend to distinguish the curves
plt.grid(True)  # Add gridlines for better readability
plt.show()
