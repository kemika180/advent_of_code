from sys import argv
from aoc_logging import start_logging
from pytictoc import TicToc
import numpy as np
import numpy.typing as npt

def read_file1(filename: str) -> npt.NDArray:
    data_list = []
    with open(filename) as file:
        try:
            logger.info(f"opening {filename}")
            for line in file:
                line = line.rstrip().split()
                data_list.append(line)
        except FileNotFoundError:
            logger.error("file not found")
            raise FileNotFoundError("file not found")

    data_array = np.array(data_list)
    data_array = np.rot90(data_array, k=3)
    return data_array

def process_data(data: npt.NDArray) -> int:
    total = 0
    for line in data:
        logger.info(line)
        line_list = list(line)
        symbol = line_list.pop(0)
        number = line_list.pop(0)
        current_result = int(number)
        for number in line_list:
            match symbol:
                case '+':
                    current_result += int(number)
                case '*':
                    current_result *= int(number)
        logger.info(f"{current_result = }")
        total += current_result

    return total

def main():
    if len(argv) == 1:
        filename = "example.txt"
    else:
        filename = argv[1]
    t = TicToc()

    data = read_file1(filename)
    t.tic()
    total = process_data(data)
    print(f"Part 1:\n  Grand Total = {total}")
    t.toc()

if __name__ == '__main__':
    logger = start_logging()
    logger.info("starting log")
    main()
