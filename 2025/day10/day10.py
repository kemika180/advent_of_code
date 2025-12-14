from sys import argv
from aoc_logging import start_logging
from pytictoc import TicToc
from itertools import combinations, combinations_with_replacement

def read_file(filename: str) -> list:
    data_list = []
    lights_dict = {".": False, "#": True}
    with open(filename) as file:
        try:
            logger.info(f"opening {filename}")
            for line in file:
                line = line.rstrip().split()
                data_list.append((
                    list(map(lambda item: lights_dict[item], list(eval(line[0].replace("[","'").replace("]","'"))))),
                    [eval(item) for item in line[1:-1]],
                    eval(line[-1].replace("{","(").replace("}",")"))
                ))
        except FileNotFoundError:
            logger.error("file not found")
            raise FileNotFoundError("file not found")
    return data_list

def process_lights(data: list) -> int:
    pushes = 0
    for item in data:
        lights = item[0]
        buttons = item[1]
        trials = []
        logger.info(f"for machine defined by {item}")
        for n in range(len(buttons)):
            combos = combinations(buttons, n+1)
            for combo in combos:
                trials.append(list(combo))
        for trial in trials:
            test = [False]*len(lights)
            for button in trial:
                if isinstance(button, int):
                    button = [button]
                for wire in button:
                    test[wire] = not test[wire]
            logger.info(f"output of {trial} -> {test}")
            if test == lights:
                logger.info(f"match found in {len(trial)} pushes")
                pushes += len(trial)
                break

    return pushes

def process_joltages(data: list) -> int:
    pushes = 0
    for item in data:
        joltages = list(item[2])
        buttons = item[1]
        logger.info(f"for machine defined by {item}")

    return pushes

def main():
    if len(argv) == 1:
        filename = "example.txt"
    else:
        filename = argv[1]
    t = TicToc()

    data = read_file(filename)
    t.tic()
    output = process_lights(data)
    logger.info(f"Part 1:\n  Pushes required to turn all machines on: {output}")
    t.toc()
    t.tic()
    output = process_joltages(data)
    logger.info(f"Part 2:\n  Pushes required to match joltages: {output}")
    t.toc()

if __name__ == '__main__':
    logger = start_logging()
    logger.info("starting log")
    main()
