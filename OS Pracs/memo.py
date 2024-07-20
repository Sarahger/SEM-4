MAX_HOLES = 100
MAX_BLOCKS = 100

def first_fit():
    fragmentation = 0
    memory = [0] * MAX_HOLES
    for i in range(num_blocks):
        for j in range(num_holes):
            if holes[j] >= blocks[i]:
                holes[j] -= blocks[i]
                fragmentation += holes[j]
                memory[j] = 1
                print(f"Block {i + 1} allocated to Hole {j + 1}")
                break
    print(f"Fragmentation: {fragmentation}")

def best_fit():
    fragmentation = 0
    memory = [0] * MAX_HOLES
    for i in range(num_blocks):
        best_fit_index = -1
        best_fit_size = MAX_BLOCKS + 1
        for j in range(num_holes):
            if holes[j] >= blocks[i] and holes[j] < best_fit_size:
                best_fit_size = holes[j]
                best_fit_index = j
        if best_fit_index != -1:
            holes[best_fit_index] -= blocks[i]
            fragmentation += holes[best_fit_index]
            memory[best_fit_index] = 1
            print(f"Block {i + 1} allocated to Hole {best_fit_index + 1}")
    print(f"Fragmentation: {fragmentation}")

def worst_fit():
    fragmentation = 0
    memory = [0] * MAX_HOLES
    for i in range(num_blocks):
        worst_fit_index = -1
        worst_fit_size = -1
        for j in range(num_holes):
            if holes[j] >= blocks[i] and holes[j] > worst_fit_size:
                worst_fit_size = holes[j]
                worst_fit_index = j
        if worst_fit_index != -1:
            holes[worst_fit_index] -= blocks[i]
            fragmentation += holes[worst_fit_index]
            memory[worst_fit_index] = 1
            print(f"Block {i + 1} allocated to Hole {worst_fit_index + 1}")
    print(f"Fragmentation: {fragmentation}")

if __name__ == "__main__":
    num_holes = int(input("Enter the number of holes: "))
    print("Enter the sizes of holes:")
    holes = [int(input()) for i in range(num_holes)]
    num_blocks = int(input("Enter the number of blocks: "))
    print("Enter the sizes of blocks:")
    blocks = [int(input()) for i in range(num_blocks)]
    print("\nFirst Fit Allocation:")
    first_fit()
    print("\nBest Fit Allocation:")
    best_fit()
    print("\nWorst Fit Allocation:")
    worst_fit()
