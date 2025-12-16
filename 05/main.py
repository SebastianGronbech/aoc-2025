import sys
from pathlib import Path


def part1(ranges, ids):
    ans = 0

    for id_ in ids:
        for start, end in ranges:
            if start <= id_ <= end:
                ans += 1
                break

    return ans


def part2(ranges):
    ranges.sort()

    last = -1
    ans = 0

    for start, end in ranges:
        if last >= start:
            start = last + 1

        if start <= end:
            ans += end - start + 1

        last = max(last, end)

    return ans


if __name__ == "__main__":
    for filename in sys.argv[1:]:
        print(f"Processing file: {filename}")

        path = Path(filename)

        with path.open("r", encoding="utf-8") as file:
            lines = [line.strip() for line in file if line.strip()]

        ranges = [tuple(map(int, line.split("-"))) for line in lines if "-" in line]
        ids = [int(line) for line in lines if "-" not in line]

        print(f"Part 1: {part1(ranges, ids)}")
        print(f"Part 2: {part2(ranges)}")
