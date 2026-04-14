import numpy as np
import matplotlib.pyplot as plt
from qutip import wigner
from matplotlib.colors import LinearSegmentedColormap

# custom colormap: dark green → green → yellow
green_yellow_cmap = LinearSegmentedColormap.from_list(
    "green_yellow",
    ["darkgreen", "green", "yellow"]
)

def create_phase_space_grid(x_min=-5, x_max=5, points=200):
    x = np.linspace(x_min, x_max, points)   # position axis
    p = np.linspace(x_min, x_max, points)   # momentum axis
    return x, p


def plot_wigner_3d(state, title="Wigner Function"):
    x, p = create_phase_space_grid()
    W = wigner(state, x, p)                 # compute Wigner function

    X, P = np.meshgrid(x, p)                # create 2D grid

    fig = plt.figure(figsize=(10, 7))
    ax = fig.add_subplot(111, projection='3d')

    ax.plot_surface(X, P, W, cmap=green_yellow_cmap)  # 3D surface plot

    ax.set_title(title)
    ax.set_xlabel("Position (X)")
    ax.set_ylabel("Momentum (P)")
    ax.set_zlabel("Wigner")

    plt.savefig(title.replace(" ", "_") + "_3D.png")  # save image
    plt.show()


def plot_wigner_with_negativity(state, title="Wigner Function"):
    x, p = create_phase_space_grid()
    W = wigner(state, x, p)                 # compute Wigner values

    plt.figure(figsize=(8, 6))

    contour = plt.contourf(x, p, W, 100, cmap=green_yellow_cmap)  # filled contour

    plt.contour(x, p, W, levels=[0], colors='black', linewidths=1.5)  # boundary at W=0

    plt.colorbar(contour, label="Wigner Value")

    plt.title(title + "\nNegative regions → Non-classical behavior")
    plt.xlabel("Position (X)")
    plt.ylabel("Momentum (P)")

    plt.savefig(title.replace(" ", "_") + ".png")  # save plot
    plt.show()