# Module 6: System Integration & Fidelity Verification

## Overview
This module implements a full 3-qubit bit-flip quantum error correction pipeline using a 5-qubit system (3 data qubits + 2 ancilla qubits), operating in a 32-dimensional Hilbert space.

## What It Does
The pipeline runs through the following stages:

1. **Encode** — Prepares the logical `|+>` state and encodes it into the entangled state `(|000> + |111>) / sqrt(2)` across the three data qubits.
2. **Inject Error** — Simulates a bit-flip noise event (X gate) on data qubit 0.
3. **Syndrome Detection** — Uses CNOT gates to compute parity checks between qubit pairs into the ancilla qubits.
4. **Measure Ancilla** — Reads the ancilla state to extract a 2-bit syndrome identifying which qubit was flipped.
5. **Decode & Correct** — Uses a syndrome lookup table to apply the appropriate X correction gate.
6. **Fidelity Verification** — Calculates `F = |<psi_target|psi_corrected>|^2` to verify perfect recovery.
7. **Visualization** — Generates a 3-panel bar chart showing qubit state probabilities at each stage (encoded, corrupted, corrected).

## Requirements
- Python 3.x
- `numpy`
- `matplotlib`

## Usage
```bash
python Yesh_Phy_Project.py
```

## Output
- Console readout of the measured syndrome, detected error, correction applied, and final fidelity score.
- A matplotlib figure showing probability distributions across the 8 data qubit states at each pipeline stage.
