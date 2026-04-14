# Quick Start Guide 🚀

Get up and running with the Quantum Computing & Quantum Optics project in 5 minutes.

## Installation (≤2 minutes)

### Prerequisites
- Python 3.8 or higher
- pip package manager
- (Optional) Virtual environment

### Setup Steps

```bash
# Navigate to project directory
cd Physics_Project

# Create virtual environment (recommended)
python -m venv venv
source venv/bin/activate          # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt
```

**That's it!** You're ready to run quantum simulations.

---

## First Run: Start Here

### 1️⃣ **Visualize Quantum States** (3 min)

```bash
python main.py
```

**What you'll see**:
- 3D surface plot of coherent state Wigner function
- Contour plot of Fock state (showing quantum non-classicality)
- Density matrices for both states
- Terminal output explaining phase space

**Key takeaway**: Different quantum states have different "shapes" in phase space!

---

### 2️⃣ **Watch Rabi Oscillations** (2 min)

```bash
python rabi_oscillations.py
```

**What you'll see**:
- Graph showing photon number oscillating between 0 and 1
- Atom excited state oscillating between 0 and 1
- Perfect oscillations (ideal, no dissipation)

**Key takeaway**: Energy bounces between atom and cavity field—the foundation of quantum gates!

---

### 3️⃣ **Interactive Exploration** (5 min)

```bash
python interactive.py
```

**What you'll see**:
- Interactive window with a slider
- Move slider to change coherent state parameter (α)
- Wigner function updates in real-time
- Watch the Gaussian blob move across phase space

**Key takeaway**: Coherent states form a smooth manifold in phase space!

---

### 4️⃣ **Animated Evolution** (2 min)

```bash
python animation.py
```

**What you'll see**:
- Animation of Wigner function evolving over time
- Gaussian blob smoothly moving in phase space
- Each frame represents a different α value

**Key takeaway**: Coherent states follow classical-like trajectories!

---

## Student Projects: Dive Deeper

### 🔴 **Error Correction - Ana's Project** (2 min)

```bash
python Ana_project.py
```

**Topics covered**:
- 3-qubit bit-flip error correcting code
- Syndrome measurement without state collapse
- Error detection using ancilla qubits
- Mathematical fidelity calculation

**Output**: 
- Histogram of syndrome measurement results
- Confirmation of error detection
- Final fidelity = 100%

**Learn**: How quantum computers protect information from errors!

---

### 🟠 **Decoherence Effects - Chittesh's Project** (2 min)

```bash
python Chittesh_PhyProj.py
```

**Topics covered**:
- Theoretical Rabi oscillations (ideal)
- Realistic oscillations with noise (Lindblad master equation)
- Cavity decay ($\kappa$) and spontaneous emission ($\gamma$)
- Comparison of ideal vs. noisy dynamics

**Output**: 
- Blue dashed line: Perfect oscillations
- Red solid line: Damped oscillations (realistic)
- Graph shows how decoherence destroys quantum states

**Learn**: Why quantum computers are limited by environmental noise!

---

### 🟢 **Grover's Algorithm - Ramya's Project** (2 min)

```bash
python Phy_Ramya.py
```

**Topics covered**:
- Grover's quantum search algorithm
- Hadamard gates for superposition
- Oracle for marking target state
- Diffuser for amplitude amplification
- Visualization of amplitude amplification over iterations

**Output**: 
- 3 subplot figures showing state evolution
- Initial: Equal superposition (all states 1/8 probability)
- Iteration 1: Target probability increases significantly
- Iteration 2: Target dominates (~90% probability)

**Learn**: How quantum computers search faster than classical computers!

---

### 🔵 **Full Error Correction Pipeline - Yesh's Project** (2 min)

```bash
python Yesh_Phy_Project.py
```

**Topics covered**:
- Complete 5-qubit quantum error correction workflow
- Encoding logical state into physical qubits
- Injecting artificial bit-flip error
- Syndrome detection circuit
- Classical syndrome decoding
- Error correction and fidelity verification

**Output**: 
```
Syndrome Measured : '10'
Error Detected    : bit-flip on data qubit 0
Correction Applied: X gate on qubit 0
Final Fidelity F  = 0.999999
Result            : PERFECT CORRECTION VERIFIED
```

**Learn**: Complete end-to-end error correction routine!

---

## Understanding the Output

### Wigner Function Plots

**Colorbar interpretation**:
- **Yellow/Green regions**: High probability (positive Wigner values)
- **Dark/Negative regions**: Quantum correlations (negative Wigner values)
- **Black contour line**: W(x,p) = 0 boundary (classical possibility limit)

**Shape meanings**:
- **Gaussian blob** (Coherent): Classical-like distribution
- **Ring with negative center** (Fock): Purely quantum behavior

### Oscillation Plots

**Lines**:
- **Blue dashed**: Ideal system (no decoherence)
- **Red solid**: Realistic system (with dissipation)

**Y-axis**: Probability (0 to 1)  
**X-axis**: Time evolution  
**Dip between curves**: Measure of decoherence effect

### Error Correction Output

| Field | Meaning |
|-------|---------|
| Syndrome Measured | Binary result from ancilla qubits (00, 01, 10, or 11) |
| Error Detected | Which qubit was flipped (0, 1, 2, or None) |
| Correction Applied | Which X gate was applied (or Identity) |
| Final Fidelity | How close final state is to target (1.0 = perfect) |

---

## Next Steps: Deeper Exploration

### 📖 **Read the Theory** (30 min)

Open `THEORY.md` for comprehensive mathematical background:
- Quantum mechanics postulates
- Wigner function derivation
- Jaynes-Cummings model details
- Lindblad master equation
- Error correction codes
- Grover's algorithm mathematics

### 🔬 **Experiment & Modify**

Try these modifications:

**Increase photon number** (in `states.py`):
```python
def generate_coherent_state(alpha=5.0, dim=30):  # More photons, higher dim
    ...
```

**Change coupling strength** (in `rabi_oscillations.py`):
```python
g = 0.1 * 2 * np.pi  # Stronger interaction = faster oscillations
```

**Add more decoherence** (in `Chittesh_PhyProj.py`):
```python
kappa = 0.1   # Stronger cavity decay
gamma = 0.1   # Stronger atomic decay
```

**Explore different Fock states** (in `main.py`):
```python
psi_f, rho_f = generate_fock_state(n=3)  # Try |3⟩ state
```

### 🖥️ **Understand the Code**

File organization:
```
main.py              ← Start here: Main entry point
├── states.py        ← Quantum state generation
├── wigner_plot.py   ← Visualization functions
├── rabi_oscillations.py  ← Light-matter interaction
├── animation.py     ← Animated evolution
├── interactive.py   ← Interactive exploration
└── [Student projects]
    ├── Ana_project.py
    ├── Chittesh_PhyProj.py
    ├── Phy_Ramya.py
    └── Yesh_Phy_Project.py
```

### 🎓 **Learning Roadmap**

**Week 1: Foundations**
1. Run `main.py` - understand Wigner functions
2. Run `rabi_oscillations.py` - see light-matter interactions
3. Read THEORY.md sections 1-2 - quantum mechanics basics

**Week 2: Decoherence**
1. Run `Chittesh_PhyProj.py` - observe decoherence
2. Modify decoherence parameters and rerun
3. Read THEORY.md section on decoherence (Lindblad equation)

**Week 3: Error Correction**
1. Run `Ana_project.py` - basic error detection
2. Run `Yesh_Phy_Project.py` - full pipeline
3. Read THEORY.md section on error correction
4. Understand syndrome table mapping

**Week 4: Algorithms**
1. Run `Phy_Ramya.py` - Grover's algorithm
2. Modify number of iterations and Fock states
3. Read THEORY.md section on quantum algorithms

---

## Common Issues & Fixes

### ❌ "ModuleNotFoundError: No module named 'qutip'"

**Solution**: Install dependencies
```bash
pip install -r requirements.txt
```

### ❌ "No module named 'qiskit_aer'"

**Solution**: Install Qiskit AER separately
```bash
pip install qiskit-aer
```

### ❌ Plots don't show up / window is blank

**Solution 1**: Add this at the end of scripts:
```python
plt.tight_layout()
plt.show()
```

**Solution 2**: Use different backend (if using headless server):
```bash
# Before running script
export MPLBACKEND=Agg
python script_name.py
```

### ❌ Simulation runs very slowly

**Causes & fixes**:
1. **Hilbert space too large**: Reduce `dim` parameter in states
2. **Time steps too many**: Reduce `points` in `tlist` (but may reduce accuracy)
3. **3D plotting slow**: Remove `plot_wigner_3d()` call, use `plot_wigner_with_negativity()` instead

### ❌ "Dimension mismatch" error

**Cause**: `dim` parameter too small for high quantum numbers  
**Fix**: Increase `dim` in state generation:
```python
generate_fock_state(n=5, dim=30)  # dim must be > n
```

---

## Performance Tips

**For faster execution**:
1. Reduce Hilbert space dimension (`dim=15` instead of 20)
2. Reduce phase space grid resolution (`points=150` instead of 200)
3. Use contour plots instead of 3D surface plots
4. Comment out visualization code if only examining numbers

**For better visualization**:
1. Increase resolution (`points=300`)
2. Use higher dimension for better accuracy
3. Save figures instead of interactive display:
```python
plt.savefig('figure.png', dpi=150)
```

---

## Project At a Glance

| Aspect | Details |
|--------|---------|
| **Topics** | Quantum states, light-matter interaction, decoherence, error correction, algorithms |
| **Language** | Python 3 |
| **Key Libraries** | QuTiP, Qiskit, NumPy, Matplotlib |
| **Total runtime** | ~15 minutes for all scripts |
| **Difficulty** | Intermediate (some quantum physics background helpful) |
| **Best for** | Learning quantum computing concepts through simulation |

---

## Get Help

### 📚 **Documentation**
- QuTiP: http://qutip.org/docs/
- Qiskit: https://qiskit.org/documentation/
- NumPy: https://numpy.org/doc/
- Matplotlib: https://matplotlib.org/stable/contents.html

### 🔍 **Understanding Concepts**
- Read `THEORY.md` (comprehensive theory guide)
- Check code comments in each file
- Cross-reference with references section in README.md

### 🧪 **Experiment**
- Modify parameters and see what happens
- Change initial states and starting conditions
- Combine modules in new ways

---

**Happy quantum exploring! Try running a script now:** 🎲⚛️

```bash
python main.py
```
