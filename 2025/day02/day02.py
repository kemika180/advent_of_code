from sys import argv
from typing import List, Set
from collections import Counter

# https://adventofcode.com/2025/day/2

def read_file(filename: str) -> List[str]:
    output = []
    try:
        with open(filename) as file:
            output = file.readline().rstrip().split(",")
        return output
    except FileNotFoundError:
        raise FileNotFoundError(f"{filename} was not found")


def parse_data(data: List[str]) -> List[tuple]:
    parsed_data = []
    for item in data:
        items = item.split("-")
        parsed_data.append((items[0], items[1]))
    return parsed_data


def process_ranges1(ranges: List[tuple]) -> List[int]:
    invalid_ids = []
    for low, high in ranges:
        for num in range(int(low), int(high)+1):
            number = str(num)
            length = len(number)
            if length % 2 != 0:
                continue
            if number[length // 2:] != number[:length // 2]:
                continue
            # print(num)
            invalid_ids.append(num)

    return invalid_ids


def process_ranges2(ranges: List[tuple]) -> Set[int]:
    invalid_ids = set()
    for low, high in ranges:
        for num in range(int(low), int(high)+1):
            number = str(num)
            length = len(number)
            for n in range(2, length+1):
                if length % n != 0:
                    continue
                l = length // n
                chunks = [number[i:i+l] for i in range(0, length, l)]
                # print(f"{n=} {chunks=}")
                if len(Counter(chunks)) != 1:
                    continue
                if num not in invalid_ids:
                    # print(num)
                    invalid_ids.add(num)

    return invalid_ids


def main():
    if len(argv) < 2:
        filename = "example.txt"
    else:
        filename = argv[1]
    data = read_file(filename)
    ranges = parse_data(data)
    ids1 = process_ranges1(ranges)
    print(f"Part 1:\n  Total of invalid IDs is {sum(ids1)}.")
    ids2 = process_ranges2(ranges)
    print(f"Part 2:\n  Total of invalid IDs is {sum(ids2)}.")


if __name__ == '__main__':
    main()
