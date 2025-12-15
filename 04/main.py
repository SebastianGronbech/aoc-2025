import sys
from pathlib import Path


def count_adjacent(diagram, row0, col0):
    count = 0

    for drow in [-1, 0, 1]:
        for dcol in [-1, 0, 1]:
            if drow == 0 and dcol == 0:
                continue

            row = row0 + drow
            col = col0 + dcol

            if 0 <= row < len(diagram) and 0 <= col < len(diagram[0]):
                if diagram[row][col] == "@":
                    count += 1

    return count


def next_state(diagram):
    removed = 0
    new_diagram = [row.copy() for row in diagram]

    for row in range(len(diagram)):
        for col in range(len(diagram[0])):
            adjacent = count_adjacent(diagram, row, col)

            if diagram[row][col] == "@" and adjacent < 4:
                new_diagram[row][col] = "."
                removed += 1

    return removed, new_diagram


def part1(diagram):
    res = 0
    for row in range(len(diagram)):
        for col in range(len(diagram[0])):
            if diagram[row][col] == "@" and count_adjacent(diagram, row, col) < 4:
                res += 1

    return res


def part2(diagram):
    ans = 0

    while True:
        removed, new_diagram = next_state(diagram)
        ans += removed

        if diagram == new_diagram:
            break

        diagram = new_diagram

    return ans


if __name__ == "__main__":
    for filename in sys.argv[1:]:
        print(f"Processing file: {filename}")

        path = Path(filename)
        with path.open("r", encoding="utf-8") as file:
            lines = [line.strip() for line in file.readlines()]

        diagram = [list(line) for line in lines]

        print(f"Part 1: {part1(diagram)}")
        print(f"Part 2: {part2(diagram)}")
