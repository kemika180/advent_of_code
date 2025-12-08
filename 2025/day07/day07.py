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
        for j, item in enumerate(prev_list):
            if (item == '|' or item == 'S') and cur_list[j] == '.':
                cur_list[j] = '|'
        prev_list = cur_list.copy()
        logger.info("".join(cur_list))

    return total

def process_data2(data: list) -> int:
    prev_list = []
    num_lists = []
    for line in data:
        cur_list = list(line)
        num_list = [0]*len(data[0])
        if 'S' in cur_list:
            prev_list = cur_list.copy()
            logger.info("".join(cur_list))
            continue
        if "^" in cur_list:
            i = -1
            for _ in range(cur_list.count("^")):
                i = cur_list.index("^", i+1)
                if prev_list[i] == "|":
                    cur_list[i-1] = "|"
                    cur_list[i+1] = "|"
                    num_list[i-1] += num_lists[-1][i]
                    num_list[i+1] += num_lists[-1][i]
        assert len(cur_list) == len(prev_list)
        for x, item in enumerate(prev_list):
            if item == "S":
                num_list[x] = 1
                cur_list[x] = "|"
            if (item == "|") and cur_list[x] != "^":
                cur_list[x] = "|"
                num_list[x] += num_lists[-1][x]
        prev_list = cur_list.copy()
        logger.info("".join(cur_list))
        num_lists.append(num_list)
    width = len(str(max(num_lists[-1])))+1
    for line in num_lists:
        line_string = ""
        for item in line:
            if item == 0:
                item = ""
            line_string = f"{line_string}{item:^{width}}"
        logger.info(line_string)
    return sum(num_lists[-1])

def main():
    if len(argv) == 1:
        filename = "example.txt"
    else:
        filename = argv[1]
    t = TicToc()

    data = read_file(filename)
    t.tic()
    total = process_data(data)
    logger.info(f"Part 1:\n  Total splits = {total}")
    t.toc()

    t.tic()
    total = process_data2(data)
    logger.info(f"Part 2:\n  Total possible paths = {total}")
    t.toc()

if __name__ == '__main__':
    logger = start_logging()
    logger.info("starting log")
    main()
