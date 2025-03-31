from itertools import count
import matplotlib.pyplot as plt

h = 1
m = 1

a = 1
V = 0

x = 0
psi = 1
dx = a * 0.01

E = 0
dE = 0.01

nmax = 4
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

print('Eigenfunctions: ', eigenfunctions)

# Plotting the eigenfunctions
counter = 0  # Reset counter to align with zero-based indexing of eigenfunctions
while counter < len(eigenfunctions):
    plt.plot(eigenfunctionsxList[counter], eigenfunctions[counter], label=f"Eigenfunction {counter+1}")
    counter += 1

plt.xlabel("x")
plt.ylabel("psi")
plt.title("Eigenfunctions of Particle in a Box")
plt.legend()  # Show legend to distinguish the curves
plt.grid(True)  # Add gridlines for better readability
plt.show()
