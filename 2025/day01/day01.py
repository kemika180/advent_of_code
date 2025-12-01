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
            parsed_data.append((direction, count % 100, count // 100))
        except IndexError:
            print(f"IndexError on {item=}")
    return parsed_data


def follow_instructions(instructions: List[tuple]) ->  Tuple[List[int], int]:
    output = []
    clicks = 0
    position = 50
    # print(f"Dial starts by pointing at {50}")
    for direction, count, extra in instructions:
        new_clicks = extra
        previous = position
        if direction == "L":
            count *= -1
        position = (position + count) % 100
        output.append(position)
        # print(f"Rotating {direction}{abs(count)+100*extra} to point at {position}.")
        if (position == 0 and count != 0) or \
            (direction == "L" and position > previous and previous != 0) or \
            (direction == "R" and position < previous):
            new_clicks += 1
        if new_clicks > 0:
            # print(f"Points at zero {new_clicks} times.")
            clicks += new_clicks
    return output, clicks


def main():
    if len(argv) < 2:
        filename = "example.txt"
    else:
        filename = argv[1]
    contents = read_file(filename)
    directions = parse_data(contents)
    positions, clicks = follow_instructions(directions)
    counts = Counter(positions)
    print("Part 1 results:")
    print(f"  The dial ends at zero {counts[0]} times.")
    print("Part 2 results:")
    print(f"  The dial points at zero {clicks} times.")


if __name__ == '__main__':
    main()
