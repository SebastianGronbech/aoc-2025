import sys
from pathlib import Path


def part1(moves):
    pos = 50
    res = 0

    for turn, steps in moves:
        for _ in range(steps):
            match turn:
                case "L":
                    pos = (pos - 1 + 100) % 100
                case "R":
                    pos = (pos + 1) % 100
        if pos == 0:
            res += 1
    return res


def part2(moves):
    pos = 50
    laps = 0

    for turn, steps in moves:
        for _ in range(steps):
            match turn:
                case "L":
                    pos = (pos - 1 + 100) % 100
                case "R":
                    pos = (pos + 1) % 100
            if pos == 0:
                laps += 1
    return laps


if __name__ == "__main__":
    for filename in sys.argv[1:]:
        print(f"Processing file: {filename}")

        path = Path(filename)
        with path.open("r", encoding="utf-8") as file:
            lines = [line.strip() for line in file.readlines()]

        moves = [(line[0], int(line[1:])) for line in lines]

        print(f"Part 1: {part1(moves)}")
        print(f"Part 2: {part2(moves)}")
