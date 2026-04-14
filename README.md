# Quantum Computing & Quantum Optics: A Comprehensive Physics Project

## 📋 Project Overview

This is a collaborative quantum physics project exploring **Lifecycle of Single Qubit** through practical implementations of quantum computing concepts, quantum optics, and quantum information theory. The project covers fundamental quantum phenomena including quantum states, light-matter interactions, quantum error correction, and quantum search algorithms.

**Key Technologies**: Python 3, QuTiP (Quantum Toolbox in Python), Qiskit (IBM's Quantum Framework), NumPy, Matplotlib

---

## 🎓 Theoretical Foundation

### 1. **Quantum States in Phase Space**

#### **Coherent States** 
A coherent state $|\alpha\rangle$ is a quantum state of light that most closely resembles classical electromagnetic waves. It's an eigenstate of the annihilation operator:

$$\hat{a}|\alpha\rangle = \alpha|\alpha\rangle$$

where $\alpha = |\alpha|e^{i\phi}$ is a complex displacement parameter.

**Key Properties**:
- **Minimum uncertainty**: Saturates Heisenberg's uncertainty principle ($\Delta x \cdot \Delta p = \hbar/2$)
- **Classical-like behavior**: Exhibits particle-like statistics
- **Phase space representation**: Maps to a Gaussian distribution in phase space

#### **Fock States** 
Fock states (or number states) $|n\rangle$ are eigenstates of the photon number operator:

$$\hat{a}^\dagger \hat{a}|n\rangle = n|n\rangle$$

**Key Properties**:
- **Quantum origin**: Show purely quantum behavior, no classical analog
- **Regular intervals**: Equally spaced energy levels
- **Negative Wigner values**: Exhibit non-classical light properties (indicating quantum advantage over classical light)

### 2. **Wigner Function: Quantum Phase Space Distribution**

The Wigner function $W(x,p)$ is a quasi-probability distribution representing quantum states in phase space:

$$W(x,p) = \frac{1}{\pi\hbar}\int_{-\infty}^{\infty} e^{i2py/\hbar}\langle x-y|\rho|x+y\rangle dy$$

**Physical Interpretation**:
- **Positive values** → Classical-like correlations between position and momentum
- **Negative values** → Non-classical (quantum) behavior, demonstrating "quantum advantage"
- **Shape** → Distribution of probability amplitude in phase space (analogous to position space)

**For Coherent States**: Gaussian Wigner function centered at $(\alpha_R, \alpha_I)$

**For Fock States**: Ring-like structure with negative central regions (hallmark of quantum non-classicality)

### 3. **Rabi Oscillations & Jaynes-Cummings Model**

The interaction between a two-level system (atom) and quantized electromagnetic field is described by the Jaynes-Cummings Hamiltonian:

$$H = \hbar\omega_c \hat{a}^\dagger\hat{a} + \hbar\omega_a \sigma^{\dagger}_z + \hbar g(\hat{a}^\dagger\sigma^- + \hat{a}\sigma^+)$$

**Components**:
- $\omega_c$: Cavity frequency
- $\omega_a$: Atomic transition frequency  
- $g$: Coupling strength
- $\sigma^{\pm}$: Atomic raising/lowering operators

**Rabi Oscillations**: Under resonance ($\omega_c = \omega_a$), the system undergoes periodic energy exchange:
$$P_{\text{excited}}(t) = \sin^2\left(\frac{gt}{\sqrt{2}}\right)$$

This represents reversible oscillations between excited and ground states—the fundamental mechanism in quantum computing gate operations!

### 4. **Decoherence: The Inevitable Quantum-Classical Transition**

Real quantum systems interact with their environment, causing coherence loss. The Lindblad master equation governs dissipative evolution:

$$\frac{d\rho}{dt} = -\frac{i}{\hbar}[H, \rho] + \sum_k \left(L_k\rho L_k^\dagger - \frac{1}{2}\{L_k^\dagger L_k, \rho\}\right)$$

**Decoherence Channels**:
- **Cavity decay** (rate $\kappa$): Energy loss to environment
- **Atomic decay** (rate $\gamma$): Spontaneous emission

**Impact**: Damps Rabi oscillations, destroying quantum coherence and leading to classical behavior.

### 5. **Quantum Error Correction: Bit-Flip Code**

Quantum information is fragile. The 3-qubit bit-flip code protects a logical qubit:

$$|\psi\rangle_{\text{logical}} = \alpha|000\rangle + \beta|111\rangle$$

**Encoding**: Map $|0\rangle \to |000\rangle$ and $|1\rangle \to |111\rangle$ using CNOT gates

**Error Detection**: Use two ancilla qubits to measure stabilizers without destroying data:
- $S_1 = Z_1Z_2$: Syndrome bit 0 = qubit 0 XOR qubit 1
- $S_2 = Z_2Z_3$: Syndrome bit 1 = qubit 1 XOR qubit 2

**Correction**: Syndrome table maps measured error syndrome to correction operation:
| Syndrome | Error | Correction |
|----------|-------|-----------|
| 00 | None | Identity |
| 10 | Q₀ flip | X₀ |
| 11 | Q₁ flip | X₁ |
| 01 | Q₂ flip | X₂ |

### 6. **Grover's Algorithm: Quantum Search**

Grover's algorithm searches an unsorted database of N elements in $O(\sqrt{N})$ time (vs. classical $O(N)$).

**Circuit Components**:

1. **Superposition**: Apply Hadamard gates to all qubits
$$|\psi\rangle = \frac{1}{\sqrt{N}}\sum_{x=0}^{N-1}|x\rangle$$

2. **Oracle** ($U_w$): Flip phase of target state
$$U_w|x\rangle = (-1)^{f(x)}|x\rangle$$

3. **Diffuser** ($U_s$): Amplitude amplification operator
$$U_s = 2|\psi\rangle\langle\psi| - I$$

**Iteration**: Repeat oracle + diffuser $\approx \frac{\pi\sqrt{N}}{4}$ times

**Result**: Probability of measuring target amplified from $1/N$ to $\approx 1$

---

## 📁 Project Structure

### Core Modules

| File | Purpose |
|------|---------|
| `main.py` | Entry point: demonstrates coherent and Fock states |
| `states.py` | Quantum state generation (coherent, Fock) |
| `wigner_plot.py` | Wigner function visualization (3D surfaces, contour plots) |
| `rabi_oscillations.py` | Jaynes-Cummings model simulation |
| `animation.py` | Animated Wigner function evolution |
| `interactive.py` | Interactive coherent state explorer with sliders |

### Student Projects

| File | Author | Topic |
|------|--------|-------|
| `Ana_project.py` | Ana | Quantum Error Correction (Bit-flip detection) using Qiskit |
| `Chittesh_PhyProj.py` | Chittesh | Decoherence effects (Lindblad master equation) |
| `Phy_Ramya.py` | Ramya | Grover's Algorithm (quantum search) |
| `Yesh_Phy_Project.py` | Yesh | Full error correction pipeline (encoding → detection → correction) |

### Visualization Outputs

- `Coherent_State_3D.png`: 3D Wigner function of coherent state
- `Fock_State.png`: Contour plot showing non-classical Fock state

---

## 🚀 Installation & Setup

### Prerequisites
- Python 3.8+
- pip package manager

### Installation Steps

```bash
# Clone the repository
git clone <repository-url>
cd Physics_Project

# Install required packages
pip install -r requirements.txt
```

### Required Libraries

```
qutip              # Quantum Toolbox in Python
qiskit             # IBM's Quantum Computing Framework
qiskit-aer         # Quantum simulators
numpy              # Numerical computing
matplotlib         # Visualization & plotting
```

---

## 💻 Usage Examples

### 1. **Visualize Quantum States**

```bash
python main.py
```

**Output**: 
- 3D surface plot of coherent state Wigner function
- Contour plot of Fock state showing negative regions (quantum advantage)
- Density matrices for both states

### 2. **Simulate Rabi Oscillations**

```bash
python rabi_oscillations.py
```

**Shows**: Periodic energy exchange between atom and cavity field over time

### 3. **Animate Wigner Function Evolution**

```bash
python animation.py
```

**Shows**: How coherent state Wigner function moves in phase space as $\alpha$ parameter changes

### 4. **Interactive State Explorer**

```bash
python interactive.py
```

**Features**: 
- Slider control for $\alpha$ parameter
- Real-time Wigner function updates
- Phase space visualization

### 5. **Quantum Error Correction (Ana's Module)**

```bash
python Ana_project.py
```

**Demonstrates**: 
- 3-qubit bit-flip encoding
- Error injection
- Syndrome measurement without state collapse
- Mathematical fidelity verification

### 6. **Study Decoherence (Chittesh's Module)**

```bash
python Chittesh_PhyProj.py
```

**Compares**:
- Ideal Rabi oscillations (no dissipation)
- Noisy system (with cavity decay & spontaneous emission)
- Effect of decoherence on quantum coherence

### 7. **Explore Grover's Algorithm (Ramya's Module)**

```bash
python Phy_Ramya.py
```

**Visualizes**: 
- Initial equal superposition (1/8 probability each)
- Amplitude amplification after each iteration
- Target state probability rising toward 1.0

### 8. **Full Error Correction Pipeline (Yesh's Module)**

```bash
python Yesh_Phy_Project.py
```

**Demonstrates**:
- Complete quantum error correction workflow
- Encoding logical state
- Error injection and detection
- Correction and fidelity verification

---

## 📊 Key Results & Observations

### Quantum Non-Classicality

**Fock States exhibit non-classical properties**:
- Negative values in Wigner function (impossible for classical probability)
- Indicate quantum advantage over classical light
- Used as resource for quantum technologies

### Rabi Oscillations

**Without noise**: Perfect periodic oscillations between system states
- Frequency: $\Omega_R = g/\sqrt{2}$ (Rabi frequency)
- Amplitude: Reaches perfect population inversion

**With decoherence**: 
- Oscillations decay exponentially
- Decoherence time $T_2 \approx 1/\gamma$ limits quantum coherence
- Motivates quantum error correction need

### Error Correction Fidelity

- **Perfect simulation**: >99.99% fidelity in error correction
- **Syndrome decoding**: 100% accuracy in error identification
- **Scalability**: 3-qubit code corrects single bit-flip errors

### Grover's Algorithm Speedup

- **2 iterations** on 3-qubit system amplifies target from 12.5% → 90%+
- **Quadratic speedup**: $O(\sqrt{N})$ vs classical $O(N)$

---

## 🔬 Physical Insights

### Why Quantum Computing is Hard (IRL)

1. **Decoherence**: Environmental noise destroys quantum information
   - Typical coherence time: microseconds to milliseconds
   - Error rates: 0.1% - 1% per gate operation

2. **Error Mitigation**: Multi-level approach needed
   - Material engineering (better isolation)
   - Quantum error correction codes
   - Noise-resilient algorithms

3. **Scalability Challenge**: 
   - Each added qubit doubles Hilbert space (exponential growth)
   - Error correction requires many physical qubits per logical qubit
   - Current systems: 10-1000 qubits; practical QC needs millions

### Quantum Advantage Windows

**Where quantum excels**:
- Simulation of quantum systems
- Database search (Grover)
- Factoring large numbers (Shor)
- Quantum chemistry & optimization

**Current limitations**: Hundreds to thousands of qubits needed for practical problems

---

## 📚 Learning Outcomes

By working through this project, you'll understand:

✅ **Quantum Mechanics**: Superposition, entanglement, measurement postulate  
✅ **Phase Space Methods**: Wigner functions, characteristic functions  
✅ **Quantum Optics**: Light-matter interaction, coherent/Fock states  
✅ **Quantum Information**: Qubits, quantum gates, quantum circuits  
✅ **Quantum Error Correction**: Stabilizer codes, syndrome decoding  
✅ **Quantum Algorithms**: Oracle-based search, amplitude amplification  
✅ **Computational Methods**: Lindblad master equation, time evolution  

---

## 🔗 References & Further Reading

### Foundational Texts
- **"Quantum Mechanics: The Theoretical Minimum"** - Leonard Susskind
- **"Quantum Computation and Quantum Information"** - Nielsen & Chuang
- **"Introduction to Quantum Optics"** - Grynberg, Aspect, & Fabre

### Key Papers
- Jaynes & Cummings (1963): Light-matter interaction in cavities
- Grover (1996): Quantum search algorithm
- Shor (1994): Quantum factoring algorithm
- Knill & Laflamme (1997): Quantum error correction theory

### Tools & Libraries
- **QuTiP Documentation**: http://qutip.org/
- **Qiskit Documentation**: https://qiskit.org/
- **IBM Quantum**: https://quantum-computing.ibm.com/

---

## 👥 Contributors

- **Ana**: Quantum Error Correction (Basic bit-flip detection)
- **Chittesh**: Decoherence & Lindblad Master Equation
- **Ramya**: Grover's Algorithm Implementation
- **Yesh**: Full Error Correction Pipeline & Fidelity Verification
- **Project Lead**: Integrated quantum computing suite

---

## 📝 License

This educational project is provided as-is for learning purposes.

---

## 🤝 How to Contribute

To extend this project:

1. **New quantum algorithms**: Implement Shor's, VQE, QAOA
2. **Visualization**: Add more phase space representations
3. **Simulation**: Include more complex Hamiltonians
4. **Error models**: Realistic noise channels from real quantum hardware
5. **Optimization**: Improve computational efficiency of currently slow modules

---

## ❓ FAQ

**Q: Why use Wigner functions?**  
A: They provide intuitive phase-space visualization. Unlike other representations, negative values directly indicate quantum non-classicality.

**Q: What's the difference between coherent and Fock states?**  
A: Coherent states behave like classical light (Gaussian Wigner function). Fock states are pure quantum (negative Wigner values) with no classical counterpart.

**Q: Why do we need error correction for only 3 qubits?**  
A: This is an educational demonstration. Real systems need codes correcting multiple error types (phase flips, amplitude damping) with many more physical qubits per logical qubit.

**Q: Is Grover's algorithm practical?**  
A: For small databases only. For realistic large databases, quantum advantage is marginal after accounting for circuit depth and error rates.

**Q: How does decoherence relate to the quantum-to-classical transition?**  
A: Decoherence destroys the phase relationships (coherence) that make quantum systems powerful. Without protection (error correction), systems quickly behave classically.

---

**Happy quantum exploring! 🎲⚛️**
