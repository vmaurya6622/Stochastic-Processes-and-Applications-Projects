import random
import matplotlib.pyplot as plt

P = [
    #     r    w    e    s
    [0.5, 0.3, 0.0, 0.2],  # r
    [0.2, 0.5, 0.1, 0.2],  # w
    [0.1, 0.3, 0.3, 0.3],  # e
    [0.0, 0.2, 0.3, 0.5],  # s
]

# States of the Markov Chain
states = ["r", "w", "e", "s"]


def simulate_markov_chain(start_state, N):
    current_state = start_state  # Initial state X0
    state_history = [current_state]
    for _ in range(N):
        current_index = states.index(current_state)
        transition_probabilities = P[current_index]
        next_state = random.choices(states, weights=transition_probabilities, k=1)[0]
        state_history.append(next_state)
        current_state = next_state
    return state_history


N = 100  # No. of steps
initial_state = "r"  # Starting state X0
trajectory = simulate_markov_chain(initial_state, N)

# Map states to numerical values for plotting
state_to_num = {state: i for i, state in enumerate(states)}
num_trajectory = [state_to_num[state] for state in trajectory]
# Plot the trajectory
plt.figure(figsize=(12, 6))
plt.plot(
    range(len(trajectory)),
    num_trajectory,
    marker="o",
    linestyle="-",
    color="b",
    label="State Transition",
)
plt.title(
    f"Markov Chain Simulation for {N} Steps Starting at '{initial_state}'",
    fontsize=16,
    fontweight="bold",
)
plt.xlabel("Step Number", fontsize=14, labelpad=10)
plt.ylabel("State", fontsize=14, labelpad=10)
plt.yticks(ticks=list(state_to_num.values()), labels=states, fontsize=12)
plt.xticks(fontsize=12)
plt.grid(color="gray", linestyle="--", linewidth=0.5, alpha=0.7)
plt.legend(loc="upper left")
# plt.legend(fontsize=12)
plt.tight_layout()
plt.show()

# Plot the bar chart
state_frequencies = {state: trajectory.count(state) for state in states}
print("Question 1 Execution initiated. \n")
print("Frequency of Each state: \n")
for state, frequency in state_frequencies.items():
    print(f"State {state}: {frequency}")

plt.figure(figsize=(10, 6))
plt.bar(
    state_frequencies.keys(),
    state_frequencies.values(),
    color="skyblue",
    edgecolor="black",
    alpha=0.7,
)
plt.title("Frequency of States in Markov Chain", fontsize=16, fontweight="bold")
plt.xlabel("States", fontsize=14)
plt.ylabel("Frequency", fontsize=14)
plt.grid(axis="y", color="gray", linestyle="--", linewidth=0.5, alpha=0.7)
plt.xticks(fontsize=12)
plt.yticks(fontsize=12)
plt.tight_layout()
plt.show()
