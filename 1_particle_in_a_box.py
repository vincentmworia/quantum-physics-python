import matplotlib.pyplot as plt

# todo We are just initializing everything to one and zero for simplicity but in real
#  sense, the true values will just scale it up or down.

h = 1  # hbar
m = 1  # mass of an electron

a = 1  # The final value x goes to
V = 0  # The potential inside our box

psi = 0  # <Our wave function>
dpsi = 1  # 1 <dphi should be different from 0>

# Starting conditions:
x = 0

dx = a * 0.001  # We want small increments from one end to the other end of the box. In our case, 1000 steps


# todo Guess the value of the energy until you get it right.
#  The higher the energy, the higher the vibration, complexity and the oscillations of our waves
#
# todo. This method is called the shooting method
# E = 500  # Energy
# Energy
E = 4.933999999999982 *10**2

# todo... We used the shooting method but in the next one, we just nest while loops to get this energy
# List to store our data
xlist = []
psilist = []

while x <= a:
    ddpsi = 2 * (m / h ** 2) * (V - E) * psi
    dpsi = dpsi + ddpsi * dx
    psi = psi + dpsi * dx
    x = x + dx
    xlist.append(x)
    psilist.append(psi)

print(xlist)
print(psilist)

# Plotting outside the loop, after all data is collected
plt.plot(xlist, psilist)
plt.xlabel("x")  # Add labels for clarity
plt.ylabel("psi")
plt.title("Wavefunction")  # Add a title
plt.show()
