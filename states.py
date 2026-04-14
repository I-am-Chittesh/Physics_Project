from qutip import coherent, fock, ket2dm

def generate_coherent_state(alpha=2.0, dim=20):
    psi = coherent(dim, alpha)        # create coherent state |α>
    rho = ket2dm(psi)                 # convert state vector to density matrix
    return psi, rho

def generate_fock_state(n=1, dim=20):
    psi = fock(dim, n)                # create Fock state |n>
    rho = ket2dm(psi)                 # density matrix representation
    return psi, rho