import sys

def hanoi_towers(n, source, target, auxiliary, tower_state):
    if n == 1:
        top_disk = tower_state[source].pop()
        print(f"Move disk from {source} to {target}: {top_disk}")
        tower_state[target].append(top_disk)

        print(f"Intermediate state: {tower_state}")
        return

    hanoi_towers(n - 1, source, auxiliary, target, tower_state)
    top_disk = tower_state[source].pop()
    print(f"Move disk from {source} to {target}: {top_disk}")
    tower_state[target].append(top_disk)

    print(f"Intermediate state: {tower_state}")
    hanoi_towers(n - 1, auxiliary, target, source, tower_state)



def main():
    try:
        disks_number = int(sys.argv[1])
    except ValueError:
        print("Помилка: введіть число дисків")
        return

    num_list = list(range(1, disks_number + 1))
    num_list.reverse()

    initial_state = {'A': num_list, 'B': [], 'C': []}

    print(f"Initial state: {initial_state}")

    hanoi_towers(disks_number, 'A', 'C', 'B', initial_state)

    print(f"\nFinal state: {initial_state}")


if __name__ == "__main__":
    main()
