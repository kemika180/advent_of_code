from sys import argv
from aoc_logging import start_logging
from pytictoc import TicToc

def read_file(filename: str) -> list:
    data_list = []
    with open(filename) as file:
        try:
            logger.info(f"opening {filename}")
            for line in file:
                line = line.rstrip()
                data_list.append(line)
        except FileNotFoundError:
            logger.error("file not found")
            raise FileNotFoundError("file not found")

    return data_list

def process_data(data: list) -> int:
    total = 0
    prev_list = []
    for line in data:
        cur_list = list(line)
        if 'S' in cur_list:
            prev_list = cur_list.copy()
            logger.info("".join(cur_list))
            continue
        if "^" in cur_list:
            i = -1
            for _ in range(cur_list.count("^")):
                i = cur_list.index("^", i+1)
                if prev_list[i] == "|":
                    total += 1
                    cur_list[i-1] = "|"
                    cur_list[i+1] = "|"
        assert len(cur_list) == len(prev_list)
        for j, item in enumerate(prev_list):
            if (item == '|' or item == 'S') and cur_list[j] == '.':
                cur_list[j] = '|'
        prev_list = cur_list.copy()
        logger.info("".join(cur_list))

    return total

def main():
    if len(argv) == 1:
        filename = "example.txt"
    else:
        filename = argv[1]
    t = TicToc()

    t.tic()
    data = read_file(filename)
    total = process_data(data)
    logger.info(f"Part 1:\n  Total = {total}")
    t.toc()

if __name__ == '__main__':
    logger = start_logging()
    logger.info("starting log")
    main()
