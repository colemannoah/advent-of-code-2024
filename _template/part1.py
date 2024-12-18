import sys


def main(input: list[str]) -> None:
    print(input)


if __name__ == "__main__":
    input = []

    for line in sys.stdin:
        input.append(line.strip())

    main(input)
