import numpy as np
import matplotlib.pyplot as plt
from functools import reduce

# =============================================================
# MODULE 6: SYSTEM INTEGRATION & FIDELITY VERIFICATION
# 3-Qubit Bit-Flip Code — Full Error Correction Pipeline
# 5 qubits: data[0], data[1], data[2], ancilla[3], ancilla[4]
# Hilbert space: 2^5 = 32 dimensions
# =============================================================

N = 5
DIM = 2 ** N
I2  = np.eye(2, dtype=complex)
X_g = np.array([[0, 1], [1, 0]], dtype=complex)
H_g = (1 / np.sqrt(2)) * np.array([[1, 1], [1, -1]], dtype=complex)

def gate(g, q):
    """Embed a single-qubit gate g at position q into the full 5-qubit space."""
    return reduce(np.kron, [g if i == q else I2 for i in range(N)])

def cnot(c, t):
    """Construct a CNOT gate (control=c, target=t) in the full 5-qubit space."""
    M = np.zeros((DIM, DIM), dtype=complex)
    for col in range(DIM):
        b = list(format(col, f'0{N}b'))
        if b[c] == '1':
            b[t] = str(1 - int(b[t]))
        M[int(''.join(b), 2), col] = 1.0
    return M

# ---- STEP 1: ENCODE logical |+> into (|000> + |111>)/sqrt(2) ⊗ |00>_anc ----
psi = np.zeros(DIM, dtype=complex)
psi[0] = 1.0
psi = gate(H_g, 0) @ psi        # Superposition on data[0]
psi = cnot(0, 1)   @ psi        # Encode: spread to data[1]
psi = cnot(0, 2)   @ psi        # Encode: spread to data[2]
psi_encoded = psi.copy()

# ---- STEP 2: INJECT BIT-FLIP ERROR on data qubit 0 ----
psi = gate(X_g, 0) @ psi        # Simulated noise event (X gate = bit flip)
psi_corrupted = psi.copy()

# ---- STEP 3: SYNDROME DETECTION CIRCUIT----
# Measures stabilizers: a0 = d0 XOR d1 (Z1Z2), a1 = d1 XOR d2 (Z2Z3)
psi = cnot(0, 3) @ psi          # a0 ^= d0
psi = cnot(1, 3) @ psi          # a0 ^= d1  →  a0 = d0 XOR d1
psi = cnot(1, 4) @ psi          # a1 ^= d1
psi = cnot(2, 4) @ psi          # a1 ^= d2  →  a1 = d1 XOR d2

# ---- STEP 4: MEASURE ANCILLA QUBITS → READ SYNDROME ----
anc_probs = np.zeros(4)
for i in range(DIM):
    anc_probs[i % 4] += abs(psi[i]) ** 2      # last 2 bits = ancilla state
syndrome_int = int(np.argmax(anc_probs))
syndrome = format(syndrome_int, '02b')

# Collapse state vector to the measured ancilla outcome and renormalize
psi_post = np.where(np.arange(DIM) % 4 == syndrome_int, psi, 0).astype(complex)
psi_post /= np.linalg.norm(psi_post)

# ---- STEP 5: CLASSICAL SYNDROME DECODING → APPLY CORRECTION GATE ----
# Syndrome lookup table derived from stabilizer algebra
syndrome_table = {'00': None, '10': 0, '11': 1, '01': 2}
err_q = syndrome_table[syndrome]
psi_corrected = (gate(X_g, err_q) @ psi_post) if err_q is not None else psi_post.copy()

# ---- STEP 6: FIDELITY CALCULATION ----
# Build target: encoded data amplitudes with ancilla now in |syndrome> state
target = np.zeros(DIM, dtype=complex)
for i in range(8):
    target[i * 4 + syndrome_int] = psi_encoded[i * 4]
fidelity = abs(np.dot(target.conj(), psi_corrected)) ** 2

print("--- MODULE 6: SYSTEM INTEGRATION & FIDELITY VERIFICATION ---")
print(f"  Syndrome Measured : '{syndrome}'")
print(f"  Error Detected    : bit-flip on data qubit {err_q}")
print(f"  Correction Applied: X gate on qubit {err_q}")
print(f"  Final Fidelity F  = |<psi_target|psi_corrected>|^2 = {fidelity:.6f}")
print(f"  Result            : {'PERFECT CORRECTION VERIFIED' if fidelity > 0.9999 else 'CORRECTION INCOMPLETE'}")

# ---- STEP 7: VISUALIZATION — Probability bar chart at each stage ----
def data_marginal(sv):
    """Trace out ancilla qubits; return marginal probs over 8 data states."""
    p, dp = np.abs(sv) ** 2, np.zeros(8)
    for i in range(DIM):
        dp[i >> 2] += p[i]      # top 3 bits = data qubit index
    return dp

labels = [f'|{format(i, "03b")}>' for i in range(8)]
stages = [
    (psi_encoded,   "Stage 1: Encoded State\n(|000> + |111>)/sqrt(2)",    'steelblue'),
    (psi_corrupted, "Stage 2: After Error\n(|100> + |011>)/sqrt(2)",       'tomato'),
    (psi_corrected, f"Stage 3: After Correction\nFidelity = {fidelity:.4f}", 'mediumseagreen'),
]
fig, axes = plt.subplots(1, 3, figsize=(15, 5), sharey=True)
fig.suptitle("Module 6: System Integration & Fidelity Verification\n"
             "3-Qubit Bit-Flip Code — Encode → Error → Detect → Correct", fontsize=12)
for ax, (sv, title, color) in zip(axes, stages):
    dp = data_marginal(sv)
    bars = ax.bar(labels, dp, color=color, edgecolor='black', linewidth=0.7)
    ax.set_title(title, fontsize=10)
    ax.set_xlabel('Data Qubit State')
    ax.set_ylim(0, 1.1)
    ax.grid(axis='y', linestyle=':', alpha=0.5)
    for bar, p in zip(bars, dp):
        if p > 0.01:
            ax.text(bar.get_x() + bar.get_width() / 2, p + 0.03,
                    f'{p:.2f}', ha='center', fontsize=9)
axes[0].set_ylabel('Probability')
plt.tight_layout()
plt.show()