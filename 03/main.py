import sys
from pathlib import Path


def part1(banks):
    ans = 0
    for bank in banks:
        best = -1

        for i in range(len(bank)):
            for j in range(i + 1, len(bank)):
                score = int(bank[i] + bank[j])

                if best == -1 or score > best:
                    best = score

        ans += best
    return ans


def part2(banks):
    ans = 0
    for bank in banks:
        jolts = 0

        for i in range(11):
            digit = max(bank[: i - 11])
            bank = bank[bank.index(digit) + 1 :]
            jolts = (jolts * 10) + int(digit)
        jolts = (jolts * 10) + int(max(bank))
        ans += jolts

    return ans


if __name__ == "__main__":
    for filename in sys.argv[1:]:
        print(f"Processing file: {filename}")

        path = Path(filename)
        with path.open("r", encoding="utf-8") as file:
            lines = [line.strip() for line in file.readlines()]

        print(f"Part 1: {part1(lines)}")
        print(f"Part 2: {part2(lines)}")
