# Quantum Computing & Quantum Optics: Comprehensive Theory Guide

## Table of Contents
1. [Quantum Mechanics Fundamentals](#quantum-mechanics-fundamentals)
2. [Quantum States & Phase Space](#quantum-states--phase-space)
3. [Light-Matter Interaction](#light-matter-interaction)
4. [Quantum Decoherence](#quantum-decoherence)
5. [Quantum Error Correction](#quantum-error-correction)
6. [Quantum Algorithms](#quantum-algorithms)
7. [Mathematical Framework](#mathematical-framework)

---

## Quantum Mechanics Fundamentals

### Postulates of Quantum Mechanics

#### **Postulate 1: State Space**
Every quantum system is associated with a complex vector space (Hilbert space) $\mathcal{H}$. A state is represented by a normalized vector $|\psi\rangle \in \mathcal{H}$.

**Normalization condition**: $\langle\psi|\psi\rangle = 1$

#### **Postulate 2: Observables & Operators**
Physical observables are represented by Hermitian operators $\hat{O}$ acting on $|\psi\rangle$.

Properties:
- **Eigenvalue equation**: $\hat{O}|\psi_n\rangle = o_n|\psi_n\rangle$
- **Orthonormality**: $\langle\psi_m|\psi_n\rangle = \delta_{mn}$
- **Completeness**: $\sum_n |\psi_n\rangle\langle\psi_n| = I$

#### **Postulate 3: Measurement**
When measuring observable $\hat{O}$ on state $|\psi\rangle$:
- **Outcome**: One eigenvalue $o_n$ with probability $P_n = |\langle\psi_n|\psi\rangle|^2$
- **State collapse**: System collapses to eigenstate $|\psi_n\rangle$
- **Expected value**: $\langle O \rangle = \langle\psi|\hat{O}|\psi\rangle$

#### **Postulate 4: Time Evolution**
System evolves according to the **Schrödinger equation**:

$$i\hbar\frac{\partial|\psi\rangle}{\partial t} = \hat{H}|\psi\rangle$$

- **Solution**: $|\psi(t)\rangle = e^{-i\hat{H}t/\hbar}|\psi(0)\rangle = \hat{U}(t)|\psi(0)\rangle$
- **Unitary evolution**: $\hat{U}(t)$ is unitary ($\hat{U}^\dagger\hat{U} = I$)

### Density Matrix Formalism

For mixed states or ensemble descriptions:

$$\rho = \sum_i p_i |\psi_i\rangle\langle\psi_i|$$

where $p_i \geq 0$, $\sum_i p_i = 1$

**Key properties**:
- $\text{Tr}(\rho) = 1$ (normalization)
- $\text{Tr}(\rho^2) \leq 1$ (purity; equals 1 for pure states only)
- $\rho \geq 0$ (positive semi-definite)

**Expectation value**: $\langle O \rangle = \text{Tr}(\hat{O}\rho)$

---

## Quantum States & Phase Space

### Harmonic Oscillator & Ladder Operators

The quantum harmonic oscillator is fundamental to quantum optics and quantum computing.

**Hamiltonian**: 
$$\hat{H} = \hbar\omega\left(\hat{a}^\dagger\hat{a} + \frac{1}{2}\right) = \hbar\omega(\hat{N} + \frac{1}{2})$$

**Ladder operators** (annihilation & creation):
$$\hat{a}|n\rangle = \sqrt{n}|n-1\rangle$$
$$\hat{a}^\dagger|n\rangle = \sqrt{n+1}|n+1\rangle$$

**Commutation relation**: $[\hat{a}, \hat{a}^\dagger] = 1$

**Position & momentum operators**:
$$\hat{x} = \sqrt{\frac{\hbar}{2m\omega}}(\hat{a} + \hat{a}^\dagger)$$
$$\hat{p} = i\sqrt{\frac{\hbar m\omega}{2}}(\hat{a}^\dagger - \hat{a})$$

### Fock States (Number States)

Fock states $|n\rangle$ are energy eigenstates of the harmonic oscillator:

$$\hat{H}|n\rangle = \hbar\omega(n + \frac{1}{2})|n\rangle$$

**Properties**:

1. **Orthonormal**: $\langle m|n \rangle = \delta_{mn}$
2. **Complete basis**: $\sum_{n=0}^{\infty}|n\rangle\langle n| = I$
3. **Number definite**: $\hat{N}|n\rangle = n|n\rangle$ (exactly $n$ photons)
4. **Construction**:
$$|n\rangle = \frac{(\hat{a}^\dagger)^n}{\sqrt{n!}}|0\rangle$$

**Position-space wavefunction** (ground state $|0\rangle$):
$$\psi_0(x) = \left(\frac{m\omega}{\pi\hbar}\right)^{1/4} e^{-\frac{m\omega x^2}{2\hbar}}$$

**Higher states**: Hermite polynomials × Gaussian

### Coherent States

Coherent states $|\alpha\rangle$ are obtained by **displacing the vacuum**:

$$|\alpha\rangle = \hat{D}(\alpha)|0\rangle = e^{\alpha\hat{a}^\dagger - \alpha^*\hat{a}}|0\rangle$$

where $\alpha = |\alpha|e^{i\phi}$ is a complex number.

**Explicit expansion**:
$$|\alpha\rangle = e^{-|\alpha|^2/2}\sum_{n=0}^{\infty}\frac{\alpha^n}{\sqrt{n!}}|n\rangle$$

**Key properties**:

1. **Eigenstate of annihilation operator**:
$$\hat{a}|\alpha\rangle = \alpha|\alpha\rangle$$

2. **Minimum uncertainty** (saturates Heisenberg bound):
$$\Delta x \cdot \Delta p = \frac{\hbar}{2}$$

3. **Overlap with Fock states**:
$$\langle n|\alpha\rangle = e^{-|\alpha|^2/2}\frac{\alpha^n}{\sqrt{n!}}$$
$$P(n) = |\langle n|\alpha\rangle|^2 = e^{-|\alpha|^2}\frac{|\alpha|^{2n}}{n!}$$ 
(Poisson distribution with mean $|\alpha|^2$)

4. **Orthogonality** (not orthonormal):
$$\langle\alpha|\beta\rangle = e^{-|\alpha-\beta|^2/2 + \alpha^*\beta - |\alpha|^2/2 - |\beta|^2/2}$$
$$= e^{-(|\alpha|^2 + |\beta|^2)/2 + \alpha^*\beta}$$

5. **Overcomplete basis** (resolution of identity):
$$\frac{1}{\pi}\int d^2\alpha|\alpha\rangle\langle\alpha| = I$$

### Wigner Function: Quantum Phase Space

The **Wigner function** is the quasi-probability distribution in phase space:

$$W(\alpha, \alpha^*) = \frac{1}{\pi^2}\int d^2\beta e^{\beta\alpha^* - \beta^*\alpha} \text{Tr}(\rho e^{\beta\hat{a}^\dagger - \beta^*\hat{a}})$$

**Alternative form** (position-momentum basis):
$$W(x,p) = \frac{1}{\pi\hbar}\int_{-\infty}^{\infty} e^{i2py/\hbar}\langle x-y|\rho|x+y\rangle dy$$

#### Wigner Function Properties

1. **Real-valued**: Despite quantum mechanics being complex, $W(x,p) \in \mathbb{R}$

2. **Marginal distributions** recover quantum expectations:
$$\int W(x,p)dp = \langle x|\rho|x\rangle \text{ (position distribution)}$$
$$\int W(x,p)dx = \langle p|\rho|p\rangle \text{ (momentum distribution)}$$

3. **Normalization**: $\int d^2\alpha W(\alpha,\alpha^*) = \text{Tr}(\rho) = 1$

4. **Can be negative**: Unlike classical probability! Negative regions indicate quantum non-classicality.

5. **Specific examples**:

**Vacuum state** $|0\rangle$:
$$W(x,p) = \frac{2}{\pi\hbar}e^{-2(x^2 + p^2)/\hbar}$$
(Gaussian centered at origin)

**Coherent state** $|\alpha\rangle$:
$$W(x,p) = \frac{2}{\pi\hbar}e^{-2((x-\alpha_R)^2 + (p-\alpha_I)^2)/\hbar}$$
(Gaussian centered at $(\alpha_R, \alpha_I)$)

**Fock state** $|n\rangle$:
$$W(x,p) = \frac{2}{\pi\hbar}e^{-(x^2+p^2)/\hbar}(-1)^n L_n\left(\frac{4(x^2+p^2)}{\hbar}\right)$$
(Laguerre polynomial with NEGATIVE CENTRAL REGION)

### Physical Interpretation: Quantum vs Classical Light

| Property | Coherent State | Fock State | Classical Light |
|----------|:--:|:--:|:--:|
| **Photon number** | Random (Poisson) | Fixed (n) | N/A |
| **Phase** | Random | Undefined | Well-defined |
| **Wigner negativity** | No | Yes | No |
| **Shot noise** | Poisson | Sub-Poissonian | N/A |
| **Light source** | Laser | Parametric down-conversion | Light bulb |

**Key insight**: Fock states have **negative Wigner values**—they exhibit purely quantum behavior incompatible with classical probability. This makes them valuable for quantum advantage.

---

## Light-Matter Interaction

### Jaynes-Cummings Model

The **Jaynes-Cummings model** describes interaction between a two-level atom and a quantized electromagnetic field in a cavity.

#### Hamiltonian (Rotating Wave Approximation)

$$\hat{H} = \hbar\omega_c \hat{a}^\dagger\hat{a} + \hbar\omega_a \sigma_z + \hbar g(\hat{a}^\dagger\sigma_- + \hat{a}\sigma_+)$$

**Terms**:
- $\hbar\omega_c \hat{a}^\dagger\hat{a}$: Cavity photon energy
- $\hbar\omega_a \sigma_z$: Atomic transition energy
- $\hbar g(\hat{a}^\dagger\sigma_- + \hat{a}\sigma_+)$: Interaction term

**Operators**:
- $\hat{a}, \hat{a}^\dagger$: Cavity annihilation/creation operators
- $\sigma_+ = |e\rangle\langle g|$: Atomic raising operator
- $\sigma_- = |g\rangle\langle e|$: Atomic lowering operator  
- $\sigma_z = |e\rangle\langle e| - |g\rangle\langle g|$: Atomic inversion
- $g$: Coupling constant (transition rate)

#### Jaynes-Cummings Dynamics (Resonant Case: $\omega_c = \omega_a = \omega$)

**Initial state**: $|\psi(0)\rangle = |e,0\rangle$ (atom excited, cavity empty)

**Time evolution**:
$$|\psi(t)\rangle = \frac{1}{\sqrt{2}}\left[\cos(gt)|e,0\rangle - i\sin(gt)|g,1\rangle\right]$$

**Observable behavior** (Rabi oscillations):

$$P_e(t) = \langle e,\cdot|\psi(t)\rangle\langle\psi(t)|e,\cdot\rangle = \cos^2(gt)$$
$$P_g(t) = \sin^2(gt)$$

**Physical interpretation**: 
- Energy oscillates between atom and cavity field
- Period: $T_R = \pi/g$ (Rabi period)
- **Rabi frequency**: $\Omega_R = g$

#### Collapse and Revival

With Fock state initial condition $|\psi(0)\rangle = |e\rangle \otimes \frac{1}{\sqrt{N}}\sum_{n=0}^{N-1}|n\rangle$:

1. **Collapse** (~$\frac{\pi}{g}$): Oscillations decay due to phase mismatch from different photon numbers
2. **Revival** (~$\frac{2\pi N}{g}$): Phases realign, oscillations reappear

This is a hallmark of quantum coherence and entanglement!

---

## Quantum Decoherence

### Lindblad Master Equation

In reality, quantum systems interact with their environment, causing decoherence. The **Lindblad master equation** governs dissipative quantum dynamics:

$$\frac{d\rho}{dt} = -\frac{i}{\hbar}[\hat{H}, \rho] + \sum_k \mathcal{L}_k[\rho]$$

**Lindblad superoperator**:
$$\mathcal{L}_k[\rho] = \hat{L}_k\rho\hat{L}_k^\dagger - \frac{1}{2}\{\hat{L}_k^\dagger\hat{L}_k, \rho\}$$

where $\hat{L}_k$ are **Lindblad operators** (jump operators) describing dissipation channels.

### Physical Decoherence Channels

#### 1. **Cavity Decay** (Photon Loss)

**Operator**: $\hat{L}_{\text{decay}} = \sqrt{\kappa}\hat{a}$

**Effect**: Photons escape the cavity

$$\hat{a}\rho\hat{a}^\dagger - \frac{1}{2}\{\hat{a}^\dagger\hat{a}, \rho\} = \hat{a}\rho\hat{a}^\dagger - \frac{1}{2}\hat{a}^\dagger\hat{a}\rho - \frac{1}{2}\rho\hat{a}^\dagger\hat{a}$$

**Consequence**: Average photon number decays as $\langle n(t)\rangle = \langle n(0)\rangle e^{-\kappa t}$

**Timescale**: Cavity decay time $T_1 = 1/\kappa$

#### 2. **Spontaneous Emission** (Atomic Decay)

**Operator**: $\hat{L}_{\text{decay}} = \sqrt{\gamma}\hat{\sigma}_-$

**Effect**: Atom decays to ground state, emitting photon into environment

$$\hat{\sigma}_-\rho\hat{\sigma}_+ - \frac{1}{2}\{\hat{\sigma}_+\hat{\sigma}_-, \rho\}$$

**Consequence**: Atomic excitation decays as $P_e(t) = P_e(0)e^{-\gamma t}$

**Timescale**: Atomic decay time $T_1 = 1/\gamma$

#### 3. **Dephasing** (Pure Decoherence)

**Operator**: $\hat{L}_{\text{dephase}} = \sqrt{\gamma_\phi}\hat{\sigma}_z$

**Effect**: Random phase fluctuations destroy quantum coherence

$$\hat{\sigma}_z\rho\hat{\sigma}_z - \rho = -2(\rho - \text{diagonal part})$$

**Consequence**: Off-diagonal elements decay as $\rho_{ij}(t) \propto e^{-\gamma_\phi t}$ ($i \neq j$)

**Timescale**: Dephasing time $T_2 = 1/\gamma_\phi$

### Impact on Rabi Oscillations

**Without decoherence** (ideal):
$$P_e(t) = \cos^2(gt)$$
Perfect periodic oscillations with amplitude = 1.

**With decoherence** (realistic):
$$P_e(t) = \frac{1}{2}\left[1 + e^{-t/T_*}\cos(gt')\right]$$

where:
- $1/T_* = \gamma + \gamma_1/2$ (effective decay)
- $gt' = g\sqrt{1 - (\gamma t)^2/(2g)^2}$ (frequency shift)

**Observable effects**:
1. **Envelope decay**: Amplitude decreases exponentially
2. **Frequency shift**: Rabi frequency $g \to g'$ 
3. **Visibility loss**: Contrast between max and min decreases
4. **Energy dissipation**: System loses coherence to environment

---

## Quantum Error Correction

### Fundamental Problem

**Single quantum bit is fragile**:
- Decoherence timescale: ~microseconds (typical)
- Gate operation time: ~nanoseconds
- Error rate per operation: 0.1% - 1%

**Naïve solution fails**: Can't copy quantum states (No-Cloning Theorem)

### Bit-Flip Code (3-Qubit)

The simplest quantum error correcting code protects against bit-flip errors (X errors).

#### Encoding

Logical qubit → 3 physical qubits:
$$|0\rangle_L \to |000\rangle$$
$$|1\rangle_L \to |111\rangle$$

**General state**:
$$|\psi\rangle_L = \alpha|000\rangle + \beta|111\rangle$$

**Encoding circuit**:
```
|ψ> ----•-------•---- q0
        |       |
|0>  ---X---•---X---- q1
           |
|0>  -------X------- q2
```

where • = control, X = target of CNOT

#### Syndrome Detection

**Stabilizers** (commute with logical operators, anticommute with errors):
- $S_1 = Z_0 Z_1$ (checks parity of qubits 0,1)
- $S_2 = Z_1 Z_2$ (checks parity of qubits 1,2)

**Syndrome measurement** (without measuring data qubits!):
- Ancilla qubit a0: $\text{syndrome}_0 = q_0 \oplus q_1$ (XOR)
- Ancilla qubit a1: $\text{syndrome}_1 = q_1 \oplus q_2$ (XOR)

**Why it works**: CNOT entangles data qubits with ancillas but doesn't destroy superposition on data qubits (non-destructive measurement).

#### Syndrome Table & Error Correction

| Error Position | Syndrome | Correction |
|:--:|:--:|:--:|
| No error | 00 | Identity |
| Qubit 0 flip | 10 | X₀ |
| Qubit 1 flip | 11 | X₁ |
| Qubit 2 flip | 01 | X₂ |

**Algorithm**:
1. Measure syndrome bits from ancillas
2. Look up error position in table
3. Apply correction operator $X_i$ if needed
4. Discard ancillas

#### Fidelity

For perfect syndrome detection:
$$F = \langle\psi_{\text{target}}|\psi_{\text{corrected}}\rangle = 1.0$$

In practice with imperfect detection:
$$F = 1 - O(p^2)$$

where $p$ = physical error rate (threshold error correction requires $p < p_c \approx 1\%$)

### Stabilizer Formalism (General Framework)

**Stabilizer group** $S$: Set of commuting Hermitian operators that fix the code space

**Logical operators**: Operators that commute with all stabilizers but act non-trivially on logical qubits

**Code distance** $d$: Minimum number of physical errors needed to cause logical error

**Protection capability**: Can correct up to $\lfloor (d-1)/2 \rfloor$ errors

For bit-flip code: $d = 3$, corrects 1 error

---

## Quantum Algorithms

### Grover's Algorithm: Quantum Search

#### Problem
Search unsorted database of N elements for marked item.

**Classical**: $O(N)$ queries needed  
**Quantum**: $O(\sqrt{N})$ queries (quadratic speedup!)

#### Algorithm Components

**1. Superposition** (Hadamard on all qubits):
```
|00...0> --H--H--...--H-- 1/√N Σ|x>
```

Creates equal superposition:
$$|\psi_0\rangle = \frac{1}{\sqrt{N}}\sum_{x=0}^{N-1}|x\rangle$$

Initial probability of target: $P_0 = 1/N$

**2. Oracle** $U_\omega$ (marks target):
$$U_\omega|x\rangle = (-1)^{f(x)}|x\rangle$$

where $f(x) = 1$ if x is target, else $f(x) = 0$

**Effect**: Flips phase of target state

**3. Diffuser** $U_s$ (amplitude amplification):
$$U_s = 2|\psi_0\rangle\langle\psi_0| - I$$

**In components**:
- Reflect about $|\psi_0\rangle$: Apply $V = 2|0\rangle\langle 0| - I$ (Hadamard-based)
- This amplifies target amplitude while suppressing others

#### Geometric Picture

Grover's algorithm works by:

1. **Initial state**: Random superposition $|\psi_0\rangle$
2. **After oracle**: Flip phase of target  
3. **After diffuser**: 
   - Amplify target amplitude
   - Suppress other amplitudes
4. **Repeat**: Each iteration rotates state toward target

**Angle rotation per iterate**:
$$\theta = 2\arcsin(1/\sqrt{N})$$

**Number of iterations for success**:
$$G = \left\lfloor \frac{\pi}{4\theta} \right\rfloor \approx \frac{\pi\sqrt{N}}{4}$$

**Final probability**:
$$P_{\text{final}} \approx 1 - O(1/N)$$

Probability of measuring target approaches 1!

#### Circuit Example (3 qubits, N=8)

```
Initial:     |000>
    ↓ H⊗H⊗H
After H:     (1/√8)[|000> + |001> + ... + |111>]
    ↓ Oracle (mark |101>)
After O:     (1/√8)[|000> + ... - |101> + ... + |111>]
    ↓ Diffuser
After D:     Amplify |101>, suppress others
    ↓ Repeat (typically 2-3 times for N=8)
Final:       ~90% probability of measuring |101>
```

#### Quantum Advantage Conditions

Grover's algorithm provides speedup when:
1. **Database is unsorted** (classical requires sequential search)
2. **Oracle can be implemented efficiently** (few gates)
3. **Problem is "black box"** (structure unknown)

**Practical limitations**:
- Cannot check answer validity quantum mechanically
- Interfered by noise/decoherence
- Overhead of oracle implementation may dominate
- For NISQ devices: typically 10-100 qubits

---

## Mathematical Framework

### Linear Algebra Essentials

#### Hilbert Space Properties
- **Vector space**: Closed under addition & scalar multiplication
- **Inner product**: $\langle\psi|\phi\rangle$ (complex number)
- **Norm**: $\|\psi\| = \sqrt{\langle\psi|\psi\rangle}$
- **Orthogonality**: $\langle\psi|\phi\rangle = 0$ when $\psi \perp \phi$

#### Operator Properties
**Hermitian operator** ($\hat{H}^\dagger = \hat{H}$):
- Real eigenvalues (observable values)
- Orthogonal eigenstates

**Unitary operator** ($\hat{U}^\dagger\hat{U} = I$):
- Preserves norm (reversible)
- Eigenvalues on unit circle: $e^{i\theta}$

**Projector** ($\hat{P}^2 = \hat{P}$, $\hat{P}^\dagger = \hat{P}$):
- Projects onto eigenspace
- **Spectral decomposition**: $\hat{A} = \sum_i \lambda_i \hat{P}_i$

#### Commutation & Anti-commutation
- $[\hat{A},\hat{B}] = \hat{A}\hat{B} - \hat{B}\hat{A}$ (commutator)
- $\{\hat{A},\hat{B}\} = \hat{A}\hat{B} + \hat{B}\hat{A}$ (anti-commutator)
- $[\hat{A},\hat{B}] = 0$: operators share eigenbasis (simultaneously measurable)

#### Tensor Products (Composite Systems)
$$|\psi\rangle_A \otimes |\phi\rangle_B = |\psi\phi\rangle$$

**Hilbert space dimension**: $\dim H_A \times \dim H_B$

**Entanglement**: States not separable as products

### Time Evolution & Equations of Motion

#### Schrödinger Equation
$$i\hbar\frac{d|\psi\rangle}{dt} = \hat{H}|\psi\rangle$$

**Formal solution**:
$$|\psi(t)\rangle = e^{-i\hat{H}t/\hbar}|\psi(0)\rangle$$

**Interaction picture** (useful for perturbation theory):
$$|\psi_I(t)\rangle = \hat{U}_0^\dagger(t)|\psi_S(t)\rangle$$
$$i\hbar\frac{d|\psi_I\rangle}{dt} = \hat{H}_I(t)|\psi_I\rangle$$

where $\hat{H}_I(t) = \hat{U}_0^\dagger(t)\hat{H}'(t)\hat{U}_0(t)$ (interaction term in interaction picture)

#### Heisenberg Equation of Motion
$$\frac{d\hat{A}}{dt} = \frac{i}{\hbar}[\hat{H},\hat{A}] + \frac{\partial \hat{A}}{\partial t}$$

Gives time evolution of operator expectation values

#### Master Equation (Open System)
$$\frac{d\rho}{dt} = -\frac{i}{\hbar}[\hat{H},\rho] + \mathcal{D}[\rho]$$

where $\mathcal{D}[\rho]$ = dissipation superoperator (accounts for environment)

**Lindblad form**:
$$\mathcal{D}[\rho] = \sum_k \left(\hat{L}_k\rho\hat{L}_k^\dagger - \frac{1}{2}\{\hat{L}_k^\dagger\hat{L}_k, \rho\}\right)$$

### Quantum Information Measures

#### Von Neumann Entropy
$$S(\rho) = -\text{Tr}(\rho\log_2\rho) = -\sum_i \lambda_i \log_2\lambda_i$$

where $\lambda_i$ = eigenvalues of $\rho$

**Properties**:
- $S = 0$ for pure states
- $S = \log N$ for maximally mixed state in $N$-dimensional space
- Quantifies **information/entanglement**

#### Trace Distance (Distinguishability)
$$D(\rho,\sigma) = \frac{1}{2}\text{Tr}|\rho - \sigma|$$

Gives probability of distinguishing two states with optimal measurement

**Range**: $0 \leq D \leq 1$ ($D=1$ for orthogonal states)

#### Fidelity
$$F(\rho,\sigma) = \text{Tr}\sqrt{\sqrt{\rho}\sigma\sqrt{\rho}}^2$$

For pure states $|\psi\rangle, |\phi\rangle$:
$$F = |\langle\psi|\phi\rangle|^2$$

**Properties**:
- $0 \leq F \leq 1$
- $F = 1$ iff states identical
- $F = 0$ iff orthogonal

### Spin-1/2 System

Fundamental two-level system (qubit)

**Basis states**: $|0\rangle$ (spin up), $|1\rangle$ (spin down)

**Pauli matrices**:
$$\sigma_x = \begin{pmatrix} 0 & 1 \\ 1 & 0 \end{pmatrix}, \quad \sigma_y = \begin{pmatrix} 0 & -i \\ i & 0 \end{pmatrix}, \quad \sigma_z = \begin{pmatrix} 1 & 0 \\ 0 & -1 \end{pmatrix}$$

**Commutation**: $[\sigma_i, \sigma_j] = 2i\epsilon_{ijk}\sigma_k$

**Algebra**: $\sigma_i^2 = I$, $\sigma_i\sigma_j = i\epsilon_{ijk}\sigma_k$ (for $i \neq j$)

---

## Summary: Project Concepts Map

```
Quantum Mechanics
├── Postulates (State, Observable, Measurement, Evolution)
├── Density Matrix Formalism
└── Time Evolution (Schrödinger, Heisenberg, Master Equation)

Quantum States
├── Fock States |n⟩
├── Coherent States |α⟩
├── Wigner Function (Phase Space Representation)
└── Quantum Non-Classicality (Negative W)

Light-Matter Interaction
├── Jaynes-Cummings Model
├── Rabi Oscillations
└── Coherence & Entanglement

Decoherence
├── Lindblad Master Equation
├── Decay Channels (Photon Loss, Spontaneous Emission, Dephasing)
├── Decoherence Timescales (T₁, T₂)  
└── Collapse of Quantum Coherence

Quantum Error Correction
├── Bit-Flip Code (3-Qubit)
├── Syndrome Detection
├── Error Correction Lookup
└── Fidelity Verification

Quantum Algorithms
├── Grover's Algorithm (Quantum Search)
├── Oracle & Diffuser
├── Amplitude Amplification
└── Quadratic Speedup: O(√N)
```

---

## References

### Textbooks
- Nielsen, M., & Chuang, I. (2010). *Quantum Computation and Quantum Information*. Cambridge.
- Meystre, P., & Sargent III, M. (1990). *Elements of Quantum Optics*. Springer.
- Cohen-Tannoudji, C., Diu, B., & Laloë, F. (1977). *Quantum Mechanics*. Wiley.

### Key Papers
- Jaynes, E. T., & Cummings, F. W. (1963). Proceedings of IEEE, 51(1), 89-109.
- Grover, L. K. (1996). arXiv preprint quant-ph/9605043.
- Knill, E., Laflamme, R., & Zurek, W. H. (1997). arXiv preprint quant-ph/9611035.

### Computational Tools
- QuTiP: http://qutip.org/
- Qiskit: https://qiskit.org/

---

*This theory guide provides the mathematical and conceptual foundation for the Physics Project implementations.*
