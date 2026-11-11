"""Print the Collatz sequence starting from 27 and the number of steps to reach 1."""


def collatz_sequence(start: int) -> list[int]:
    if start < 1:
        raise ValueError("start must be a positive integer")
    sequence = [start]
    n = start
    while n != 1:
        n = n // 2 if n % 2 == 0 else 3 * n + 1
        sequence.append(n)
    return sequence


def main() -> None:
    sequence = collatz_sequence(27)
    for n in sequence:
        print(n)
    print(f"Total steps: {len(sequence) - 1}")


if __name__ == "__main__":
    main()
