def hanoi(n, source, target, auxiliary):
    if n == 1:
        print(f"Move disk 1 from rod {source} to rod {target}")
        return
    hanoi(n-1, source, auxiliary, target)
    print(f"Move disk {n} from rod {source} to rod {target}")
    hanoi(n-1, auxiliary, target, source)

def main():
    n = int(input("Enter the number of disks: "))
    hanoi(n, 'A', 'C', 'B')

if __name__ == "__main__":
    main()
