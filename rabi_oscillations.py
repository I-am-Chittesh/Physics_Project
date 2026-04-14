import numpy as np
import matplotlib.pyplot as plt
from qutip import *

# Parameters
wc = 1.0 * 2 * np.pi
wa = 1.0 * 2 * np.pi
g  = 0.05 * 2 * np.pi
N = 5  # fewer states = cleaner, faster

tlist = np.linspace(0, 25, 100)

# Initial state |0, e>
psi0 = tensor(basis(N, 0), basis(2, 1))

# Operators
a  = tensor(destroy(N), qeye(2))
sm = tensor(qeye(N), destroy(2))

# Hamiltonian (RWA)
H = wc * a.dag() * a + wa * sm.dag() * sm + g * (a.dag() * sm + a * sm.dag())

# Time evolution (NO dissipation)
result = sesolve(H, psi0, tlist, [a.dag()*a, sm.dag()*sm])

# Extract expectation values
n_c = result.expect[0]  # photons
n_a = result.expect[1]  # atom excitation

# Plot Rabi oscillations
plt.figure(figsize=(8,5))
plt.plot(tlist, n_c, label="Photon number")
plt.plot(tlist, n_a, label="Atom excited state")
plt.xlabel("Time")
plt.ylabel("Probability")
plt.title("Rabi Oscillations (Jaynes-Cummings Model)")
plt.legend()
plt.grid()
plt.show()
