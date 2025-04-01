import matplotlib.pyplot as plt
import numpy as np

# Constants
h = 1
m = 1
a = 1
V = 0

dx = a * 0.01
dE = 0.01
nmax = 5

# Variables
eigenfunctions = []
eigenfunctionsxList = []
eigenEnergies = []

# Compute eigenfunctions and eigenvalues
E = 0
counter = 1
while counter <= nmax:
    psi = 1
    while abs(psi) > 0.001:
        psi = 0
        x = 0
        dpsi = 1
        E += dE
        xlist = []
        psilist = []
        while x <= a:
            ddpsi = 2 * (m / h ** 2) * (V - E) * psi
            dpsi += ddpsi * dx
            psi += dpsi * dx
            x += dx
            xlist.append(x)
            psilist.append(psi)

    # Store eigenfunction and eigenenergy
    eigenfunctions.append(psilist)
    eigenfunctionsxList.append(xlist)
    eigenEnergies.append(E)
    counter += 1
    E *= 1.1  # Increase E to prevent finding the same eigenvalue repeatedly

# Normalize eigenfunctions
for i in range(len(eigenfunctions)):
    normConstant = np.dot(eigenfunctions[i], eigenfunctions[i]) * dx
    eigenfunctions[i] = [psi / np.sqrt(normConstant) for psi in eigenfunctions[i]]

# Plot eigenfunctions at their respective energy levels
scale_factor = 2  # Scale to make wavefunctions more visually distinct
for i in range(len(eigenfunctions)):
    shifted_psi = [eigenEnergies[i] + scale_factor * psi for psi in eigenfunctions[i]]
    plt.plot(eigenfunctionsxList[i], shifted_psi, label=f"Eigenfunction {i + 1} (E={eigenEnergies[i]:.2f})")

# Customize and display the plot
plt.xlabel("x")
plt.ylabel("Energy + ψ (scaled)")
plt.title("Eigenfunctions Plotted at Their Energy Levels")
plt.legend()
plt.grid(True)
plt.show()
