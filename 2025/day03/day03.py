from sys import argv
from typing import List
from aoc_logging import start_logging



def read_file(filename: str) -> List[str]:
    output = []
    with open(filename) as file:
        try:
            logger.info(f"opening {filename}")
            for line in file:
                output.append(line.rstrip())
        except FileNotFoundError:
            logger.error("file not found")
            raise FileNotFoundError("file not found")
    return output

def parse_data(data: List[str]) -> List[List[int]]:
    output = []
    for line in data:
        new_list = []
        for number in list(line):
            new_list.append(int(number))
        output.append(new_list)
    return output


def process_data(data: List[List[int]]) -> List[int]:
    output = []
    for line in data:
        logger.info("".join([str(n) for n in line]))
        first = max(line[:-1])
        i = line.index(first)
        second = max(line[i+1:])
        number = first*10+second
        output.append(number)
        logger.info(number)

    return output

def process_data2(data: List[List[int]]) -> List[int]:
    output = []
    for line in data:
        number_list = []
        logger.info("".join([str(n) for n in line]))
        for number in range(12, 0, -1):
            number -= 1
            reverse_line = list(reversed(line))
            num = max(reverse_line[number:])
            i = line.index(num)
            line = line[i+1:]
            number_list.append(str(num))
        new_number = int("".join(number_list))
        logger.info(f"{new_number}")
        output.append(new_number)

    return output

def main():
    if len(argv) == 1:
        filename = "example.txt"
    else:
        filename = argv[1]

    data = read_file(filename)
    parsed_data = parse_data(data)
    output = process_data(parsed_data)
    print(f"Part 1:\nSum of the resultant numbers is {sum(output)}.")

    output2 = process_data2(parsed_data)
    print(f"Part 2:\nSum of the resultant numbers is {sum(output2)}.")


if __name__ == '__main__':
    logger = start_logging()
    logger.info("starting log")
    main()
