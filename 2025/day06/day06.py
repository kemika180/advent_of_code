from sys import argv
from aoc_logging import start_logging
from pytictoc import TicToc
import numpy as np

def read_file1(filename: str) -> list:
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

    return list(data_array)

def read_file2(filename: str) -> list:
    data_list = []
    number_list = []
    symbol_list = []
    with open(filename) as file:
        try:
            logger.info(f"opening {filename}")
            for line in file:
                line = list(line.rstrip('\n'))
                data_list.append(line)
            if filename == "example.txt":
                symbol_list = ''.join(data_list[3]).split()
                data_list = data_list[:3]
            else:
                symbol_list = ''.join(data_list[4]).split()
                data_list = data_list[:4]

        except FileNotFoundError:
            logger.error("file not found")
            raise FileNotFoundError("file not found")

    data_list = list(np.rot90(np.array(data_list), k=1))

    temp_list = []
    temp_list.append(symbol_list.pop())
    for i in range(0, len(data_list)):
        line = "".join(data_list[i]).strip()
        if line == "":
            number_list.append(temp_list.copy())
            temp_list = []
            temp_list.append(symbol_list.pop())
        else:
            temp_list.append(int(line))
    else:
        number_list.append(temp_list.copy())

    return number_list

def process_data(data: list) -> int:
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

    t.tic()
    data = read_file1(filename)
    total = process_data(data)
    logger.info(f"Part 1:\n  Grand Total = {total}")
    t.toc()
    t.tic()
    data2 = read_file2(filename)
    total = process_data(data2)
    logger.info(f"Part 2:\n  Grand Total = {total}")
    t.toc()

if __name__ == '__main__':
    logger = start_logging()
    logger.info("starting log")
    main()
