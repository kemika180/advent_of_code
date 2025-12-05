from sys import argv
from aoc_logging import start_logging
from pytictoc import TicToc
from typing import List, Tuple

def read_file(filename: str) -> Tuple[List, List]:
    ranges = []
    items = []
    top = True
    with open(filename) as file:
        try:
            logger.info(f"opening {filename}")
            for line in file:
                line = line.rstrip()
                if top:
                    if line == '':
                        top = False
                        continue
                    else:
                        data = line.split("-")
                        ranges.append((int(data[0]), int(data[1])))
                else:
                    items.append(int(line.rstrip()))
        except FileNotFoundError:
            logger.error("file not found")
            raise FileNotFoundError("file not found")
    return ranges, items

def check_items(ranges: List[tuple], items: List[int]) -> int:
    matches = 0
    ranges.sort(key=lambda range: range[0])
    for item in items:
        for r in ranges:
            if item < r[0]:
                logger.info(f"{item} is bad")
                break
            if r[0] <=item <= r[1]:
                logger.info(f"{item} is good")
                matches += 1
                break
        else:
            logger.info(f"{item} is bad")

    return matches

def check_ranges(ranges: List[tuple]) -> int:
    checked = []
    count = 0
    start = len(ranges)
    end = 0
    ranges.sort(key=lambda range: range[0])
    for i, (low, high) in enumerate(ranges):
        end += 1
        if (low, high) in checked:
            logger.info(f"({low}, {high}) already checked")
            continue
        logger.info(f"checking ({low}, {high})")
        for (low2, high2) in ranges[i+1:]:
            if high >= low2 or high + 1 == low2:
                logger.info(f"combining ({low}, {high}) and ({low2}, {high2})")
                high = max(high, high2)
                checked.append((low2, high2))
                continue
            else:
                logger.info(f"counting ({low}, {high})")
                count += len(range(low, high+1))
                break
        else:
            logger.info(f"counting ({low}, {high})")
            count += len(range(low, high+1))

    assert start == end
    return count

def main():
    if len(argv) == 1:
        filename = "example.txt"
    else:
        filename = argv[1]
    t = TicToc()

    ranges, items = read_file(filename)
    t.tic()
    matches = check_items(ranges, items)
    print(f"Part 1:\n  There are {matches} good items.")
    t.toc()
    t.tic()
    count = check_ranges(ranges)
    print(f"Part 2:\n  There are {count} possible items in the ranges provided.")
    t.toc()

if __name__ == '__main__':
    logger = start_logging()
    logger.info("starting log")
    main()
