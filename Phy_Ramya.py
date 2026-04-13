import numpy as np
import matplotlib.pyplot as plt

# ==========================================
# 1. Build the 3-qubit state vector simulator
# ==========================================

N = 8 # 3 qubits means 2^3 = 8 states
states = ['000', '001', '010', '011', '100', '101', '110', '111']

# Initialize the state vector to |000>
initial_state = np.zeros((N, 1))
initial_state[0, 0] = 1.0

# Define the 2x2 Hadamard matrix
H = (1 / np.sqrt(2)) * np.array([[1, 1], 
                                 [1, -1]])

# Create the 8x8 Hadamard matrix for 3 qubits using Kronecker products (tensor products)
H2 = np.kron(H, H)
H3 = np.kron(H2, H)

# Apply Hadamard to all qubits to create an equal superposition
superposition_state = np.dot(H3, initial_state)

# ==========================================
# 2. Create 8x8 matrices for the Oracle and Diffuser
# ==========================================

# Let's set our target state to '101' (which is index 5)
target_index = 5
print(f"Our target state is |{states[target_index]}>")

# Build the Oracle (U_w): Identity matrix, but with -1 at the target index
oracle = np.eye(N)
oracle[target_index, target_index] = -1

# Build the Diffuser (U_s): 2 * |s><s| - I
# |s> is the equal superposition state
diffuser = 2 * np.dot(superposition_state, superposition_state.T) - np.eye(N)

# ==========================================
# 3. Program the main simulation loop & Plotting
# ==========================================

# Keep track of probabilities for plotting
def get_probabilities(state_vector):
    return np.abs(state_vector.flatten())**2

iterations = 2
current_state = superposition_state

# Set up the plot grid (1 row, 3 columns)
fig, axes = plt.subplots(1, 3, figsize=(18, 5), sharey=True)
fig.suptitle("Grover's Algorithm: Amplitude Amplification (Target = |101>)", fontsize=16)

# Plot 1: Initial Superposition
axes[0].bar(states, get_probabilities(current_state), color='skyblue')
axes[0].set_title('Initial Equal Superposition')
axes[0].set_ylabel('Probability')
axes[0].set_ylim(0, 1)

# Simulation Loop
for i in range(iterations):
    # Step 1: Apply the Oracle (Flip the phase of the target)
    current_state = np.dot(oracle, current_state)
    
    # Step 2: Apply the Diffuser (Amplify the target)
    current_state = np.dot(diffuser, current_state)
    
    # Plot the results after each iteration
    axes[i+1].bar(states, get_probabilities(current_state), color='salmon')
    axes[i+1].set_title(f'After Iteration {i+1}')
    axes[i+1].set_xlabel('Quantum States')

plt.tight_layout()
plt.show()

# Print final probability of measuring the target
final_probs = get_probabilities(current_state)
print(f"Final probability of measuring |{states[target_index]}>: {final_probs[target_index]*100:.2f}%")