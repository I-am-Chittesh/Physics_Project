import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider
from qutip import coherent, wigner

def interactive_coherent():
    dim = 20
    x = np.linspace(-5, 5, 200)       # phase space axis

    fig, ax = plt.subplots()
    plt.subplots_adjust(bottom=0.25)

    alpha_init = 1.0
    psi = coherent(dim, alpha_init)   # initial coherent state
    W = wigner(psi, x, x)

    contour = ax.contourf(x, x, W, 100, cmap="viridis")
    plt.colorbar(contour)

    ax.set_title("Interactive Coherent State")

    # slider setup
    ax_slider = plt.axes([0.2, 0.1, 0.6, 0.03])
    slider = Slider(ax_slider, 'Alpha', 0.1, 5.0, valinit=alpha_init)

    def update(val):
        ax.clear()                               # clear old plot
        psi = coherent(dim, slider.val)          # new state
        W = wigner(psi, x, x)
        ax.contourf(x, x, W, 100, cmap="viridis")
        ax.set_title(f"Alpha = {slider.val:.2f}")
        fig.canvas.draw_idle()                   # refresh plot

    slider.on_changed(update)

    plt.show()


if __name__ == "__main__":
    interactive_coherent()