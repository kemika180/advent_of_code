from sys import argv
from typing import List, Tuple
from collections import Counter

# https://adventofcode.com/2025/day/1

def read_file(filename: str) -> List[str]:
    output = []
    with open(filename) as file:
        for line in file:
            output.append(line.rstrip())
    return output


def parse_data(data: List[str]) -> List[tuple]:
    parsed_data = []
    for item in data:
        try:
            direction = item[0]
            count = int(item[1:])
            parsed_data.append((direction, count))
        except IndexError:
            print(f"IndexError on {item=}")
    return parsed_data


def follow_instructions(instructions: List[tuple]) ->  Tuple[List[int], int]:
    output = []
    clicks = 0
    position = 50
    for direction, count in instructions:
        if direction == "L":
            count *= -1
        position += count
        position = position % 100
        output.append(position)
    return output, clicks


def main():
    if len(argv) < 2:
        filename = "example.txt"
    else:
        match argv[1]:
            case "part1":
                filename = "part1.txt"
            case _:
                filename = "example.txt"
    contents = read_file(filename)
    directions = parse_data(contents)
    positions, clicks = follow_instructions(directions)
    counts = Counter(positions)
    print("Part 1 results:")
    print(f"  The dial points at zero {counts[0]} times.")
    print("Part 2 results:")
    print(f"  There were {clicks} clicks.")


if __name__ == '__main__':
    main()
