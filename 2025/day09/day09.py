from sys import argv
from aoc_logging import start_logging
from pytictoc import TicToc

def read_file(filename: str) -> list:
    data_list = []
    with open(filename) as file:
        try:
            logger.info(f"opening {filename}")
            for line in file:
                line = line.rstrip().split(",")
                data_list.append(line)
        except FileNotFoundError:
            logger.error("file not found")
            raise FileNotFoundError("file not found")

    return data_list

def process_data(data: list) -> int:
    largest = 0
    for i, (x1, y1) in enumerate(data):
        for (x2, y2) in data[i+1:]:
            area = (abs(int(x2)-int(x1))+1)*(abs(int(y2)-int(y1))+1)
            largest = max([largest, area])
    return largest

def main():
    if len(argv) == 1:
        filename = "example.txt"
    else:
        filename = argv[1]
    t = TicToc()

    data = read_file(filename)
    t.tic()
    output = process_data(data)
    logger.info(f"Part 1:\n  Largest area is {output}")
    t.toc()

if __name__ == '__main__':
    logger = start_logging()
    logger.info("starting log")
    main()
