import sys
from pathlib import Path


def is_invalid(number, repeat_count):
    return (
        len(number) % repeat_count == 0
        and number[: len(number) // repeat_count] * repeat_count == number
    )


def part1(ranges):
    ans = 0
    for start, end in ranges:
        for number in range(start, end + 1):
            if is_invalid(str(number), 2):
                ans += number

    return ans


def part2(ranges):
    ans = 0
    for start, end in ranges:
        for number in range(start, end + 1):
            number_str = str(number)

            for i in range(2, len(number_str) + 1):
                if is_invalid(number_str, i):
                    ans += number
                    break
    return ans


if __name__ == "__main__":
    for filename in sys.argv[1:]:
        print(f"Processing file: {filename}")

        path = Path(filename)
        with path.open("r", encoding="utf-8") as file:
            data = file.read()

        ranges = [
            tuple(map(int, line.split("-")))
            for line in data.replace("\n", "").strip().split(",")
            if line
        ]

        print(f"Part 1: {part1(ranges)}")
        print(f"Part 2: {part2(ranges)}")
