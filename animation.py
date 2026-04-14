import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from qutip import coherent, wigner

dim = 20
x = np.linspace(-5, 5, 200)

fig, ax = plt.subplots()

def update(frame):
    ax.clear()                         # clear previous frame
    alpha = frame / 5                  # change alpha over time
    psi = coherent(dim, alpha)
    W = wigner(psi, x, x)

    ax.contourf(x, x, W, 100, cmap="viridis")
    ax.set_title(f"Alpha = {alpha:.2f}")

ani = FuncAnimation(fig, update, frames=30, interval=200)

plt.show()