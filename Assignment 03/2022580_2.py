import matplotlib.pyplot as plt
# JetBrainsMono Nerd Font Mono,'JetBrainsMono Nerd Font',JetBrainsMonoNL NFP
def complete_transition_matrix(matrix):
    for i in range(len(matrix)):
        row = matrix[i]
        row_sum = 0
        missing_index = -1
        for j in range(len(row)):
            if row[j] is None:
                if missing_index == -1:
                    missing_index = j
                else:
                    raise ValueError(
                        "More than one missing value in a row is not supported."
                    )
            else:
                row_sum += row[j]
        if missing_index != -1:
            matrix[i][missing_index] = 1 - row_sum
    return matrix

# i am assuming that there is only square matrices for matrix multiplication
def input_matrix():
    n = int(input("Enter the size of the matrix (n x n): "))
    matrix = []
    print(
        "\nInstructions:- \nEnter the matrix row by row. Use 'none' (without quotes) for missing values."
    )
    for i in range(n):
        row = input(
            f"Enter row {i + 1} (space-separated, e.g., '0.8 0.1 None'): "
        ).split()
        row = [None if value.lower() == "none" else float(value) for value in row]
        matrix.append(row)
    return matrix

# Note/ I have Added two matrices you should comment any one of it to use the other one.

P_partial = [
    [0.7, 0.2, None],  # Row 0, missing value
    [0.4, None, 0.0],  # Row 1, missing value
    [0.0, 1.0, 0.0],  # Row 2, no missing values
]

# P_partial = [
#     [0.5, None, 0.0, 0.2],  # Row 0, missing value
#     [None, 0.5, 0.1, 0.2],  # Row 1, missing value
#     [None, 0.3, 0.3, 0.0],  # Row 3, missing values
#     [0.0, 0.2, 0.3, None],  # Row 4, missing values
# ]

# Main code
print("Enter 0 if you want to use the Question's Matrix.")
print("Enter 1 if you want to Enter the Matrix values.\n")
taken_input = int(input("Enter Input Value: "))
if taken_input == 0:
    completed_matrix = complete_transition_matrix(P_partial)
elif taken_input == 1:
    print("Manual Transition Matrix Input")
    P_partial = input_matrix()
    completed_matrix = complete_transition_matrix(P_partial)

print("\nCompleted Transition Matrix:")
for row in completed_matrix:
    print(row)

# Part 02 Initialised
print("Part 02 Initialised")

def multiply_matrices(A, B):
    n = len(A)
    result = [[0 for _ in range(n)] for _ in range(n)]
    for i in range(n):
        for j in range(n):
            for k in range(n):
                result[i][j] += A[i][k] * B[k][j]
    return result

def compute_matrix_power(P, power):
    n = len(P)
    result = [[1 if i == j else 0 for j in range(n)] for i in range(n)]
    for _ in range(power):
        result = multiply_matrices(result, P)
    return result

# Storing a00 values to observe convergence at each step from 0 to 50
iterations = list(range(1, 51))
a00_values = []

for step in iterations:
    P_power = compute_matrix_power(P_partial, step)
    if step == 10:
        print("\nP^10 (Transition Matrix after 10 steps):")
        for row in P_power:
            print(row)
    elif step == 20:
        print("\nValue of a00 in P^10:", P_power[0][0])
        print("\nP^20 (Transition Matrix after 20 steps):")
        for row in P_power:
            print(row)
        print("\nValue of a00 in P^20:", P_power[0][0])
    elif step == 50:
        print("\nP^50 (Transition Matrix after 50 steps):")
        for row in P_power:
            print(row)
        print("\nValue of a00 in P^50:", P_power[0][0])
    a00_values.append(P_power[0][0])  # First row, first column value

# Plotting the values of a00
plt.figure(figsize=(10, 6))
plt.plot(
    iterations,
    a00_values,
    marker="o",
    linestyle="-",
    color="purple",
    label="Value of a00",
)
plt.title("Convergence of a00 in Transition Matrix", fontsize=16, fontweight="bold")
plt.xlabel("Iterations (Number of Steps)", fontsize=14, labelpad=10)
plt.ylabel("Value of a00", fontsize=14, labelpad=10)
plt.xticks(fontsize=12)
plt.yticks(fontsize=12)
plt.axhline(y=a00_values[-1], color="green", linestyle="--", label="Steady-State Value")
plt.grid(color="gray", linestyle="--", linewidth=0.5, alpha=0.7)
plt.legend(fontsize=11.5)
plt.tight_layout()
plt.show()
