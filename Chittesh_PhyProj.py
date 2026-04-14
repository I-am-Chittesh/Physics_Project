import numpy as np
import matplotlib.pyplot as plt
from qutip import destroy, tensor, qeye, basis, mesolve

N = 10                 
wc = 1.0 * 2 * np.pi   
wa = 1.0 * 2 * np.pi   
g  = 0.05 * 2 * np.pi  
kappa = 0.05           
gamma = 0.05           
a  = tensor(destroy(N), qeye(2)) 
sm = tensor(qeye(N), destroy(2))
H = wc * a.dag() * a + wa * sm.dag() * sm + g * (a.dag() * sm + a * sm.dag())
psi0 = tensor(basis(N, 0), basis(2, 1))
c_ops = []
c_ops.append(np.sqrt(kappa) * a)  
c_ops.append(np.sqrt(gamma) * sm) 
tlist = np.linspace(0, 25, 250)
track_op = [sm.dag() * sm]
ideal_result = mesolve(H, psi0, tlist, [], track_op)
noisy_result = mesolve(H, psi0, tlist, c_ops, track_op)
fig, ax = plt.subplots(figsize=(10, 6))

ax.plot(tlist, ideal_result.expect[0], 'b--', linewidth=2, label='Ideal System (Perfect Rabi Oscillations)')
ax.plot(tlist, noisy_result.expect[0], 'r-', linewidth=2, label='Noisy System (Decoherence via Lindblad)')

ax.set_xlabel('Time')
ax.set_ylabel('Probability of Atom in Excited State')
ax.set_title('Module 4: The Inevitable Corruption (Decoherence)')
ax.legend()
ax.grid(True, linestyle=':', alpha=0.7)

plt.show()