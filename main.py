from states import generate_coherent_state, generate_fock_state
from wigner_plot import plot_wigner_3d, plot_wigner_with_negativity

def main():
    print("Generating Coherent State...")
    psi_c, rho_c = generate_coherent_state(alpha=2)

    print("Generating Fock State...")
    psi_f, rho_f = generate_fock_state(n=1)

    print("\nDensity Matrix (Coherent):")
    print(rho_c)

    print("\nDensity Matrix (Fock):")
    print(rho_f)

    # explanation for project/viva
    print("\n--- PHASE SPACE INFO ---")
    print("Phase space = position (X) + momentum (P)")
    print("Wigner function represents quantum state in phase space")
    print("Negative values indicate NON-CLASSICAL light\n")

    plot_wigner_3d(psi_c, "Coherent State")
    plot_wigner_with_negativity(psi_f, "Fock State")

if __name__ == "__main__":
    main()