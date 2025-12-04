from sys import argv
import numpy as np
import numpy.typing as npt
from typing import Tuple
from aoc_logging import start_logging

def read_file(filename: str) -> npt.NDArray[np.str_]:
    output = []
    with open(filename) as file:
        try:
            logger.info(f"opening {filename}")
            for line in file:
                output.append(list(line.rstrip())+['.'])
            output.append(['.']*len(output[0]))
        except FileNotFoundError:
            logger.error("file not found")
            raise FileNotFoundError("file not found")
    return np.array(output)

def process_data(map: npt.NDArray[np.str_]) -> Tuple[int, npt.NDArray[np.str_]]:
    count = 0
    max_y = len(map)-1
    max_x = len(map[0])-1
    new_map = map.copy()
    for y, _ in enumerate(map):
        for x, _ in enumerate(map):
            symbol = map[y, x]
            if symbol == "@":
                block = map[max(y-1, 0):min(y+2, max_y), max(x-1, 0):min(x+2, max_x)]
                counts = np.sum(np.char.count(block, "@"))
                if counts < 5:
                    new_map[y, x] = "x"
                    count += 1
            elif symbol == "x":
                new_map[y, x] = '.'

    return count, new_map

def main():
    if len(argv) == 1:
        filename = "example.txt"
    else:
        filename = argv[1]

    map = read_file(filename)
    count, _ = process_data(map)
    print(f"Part 1:\n  There are {count} movable rolls.")

    movable = np.inf
    total = 0
    while movable > 0:
        for line in map:
            logger.info("".join(line))
        movable, map = process_data(map)
        total += movable
        logger.info(f"{movable = } {total = }")

if __name__ == '__main__':
    logger = start_logging()
    logger.info("starting log")
    main()
