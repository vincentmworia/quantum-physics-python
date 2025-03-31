import matplotlib.pyplot as plt
from time import sleep

# todo We are just initializing everything to one and zero for simplicity but in real
#  sense, the true values will just scale it up or down.

h = 1  # hbar
m = 1  # mass of an electron

a = 1  # The final value x goes to
V = 0  # The potential inside our box

# Starting conditions:
x = 0
psi = 1  # <Our wave function>
dx = a * 0.001  # We want small increments from one end to the other end of the box. In our case, 1000 steps

# todo Energy initialized, then we scan until we get a zero at x=0 and x=a as required
E = 0
dE = 0.001


while abs(psi) > 0.0001:
    psi = 0  # <Our wave function>
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
        # sleep(0.001)
    # sleep(0.001)
# todo we add some sleep because if we don't we are running with the
#  full computation speed of the computer, that may make it to crash?
# print(xlist)
# print(psilist)

# Plotting outside the loop, after all data is collected
plt.plot(xlist, psilist)
plt.xlabel("x")  # Add labels for clarity
plt.ylabel("psi")
plt.title("Wavefunction")  # Add a title
plt.show()

print(E)