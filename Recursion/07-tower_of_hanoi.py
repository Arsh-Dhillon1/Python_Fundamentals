def tower_of_hanoi(n,start,helper,destination):
    if n == 1:
        print(f"Move disk {n} from {start} to {destination}")
        return

    tower_of_hanoi(n-1,start,destination,helper)
    print(f"Move disk {n} from {start} to {destination}")
    tower_of_hanoi(n-1,helper,start,destination)

tower_of_hanoi(3,"A","B","C")

