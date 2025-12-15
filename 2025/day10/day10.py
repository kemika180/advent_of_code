from sys import argv
from aoc_logging import start_logging
from pytictoc import TicToc
from itertools import combinations
import numpy as np
from numpy.typing import NDArray
from scipy.optimize import milp, LinearConstraint

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
        joltages = item[2]
        buttons = item[1]
        vectors = []
        logger.info(f"for machine defined by {item}")
        for button in buttons:
            vector = [0]*len(joltages)
            if isinstance(button, int):
                button = [button]
            for wire in button:
                vector[wire] = 1
            vectors.append(np.array(vector))
        vectors = np.array(vectors).T
        logger.info(f"joltages = {list(joltages)}")
        logger.info(f"vectors =\n{vectors}")
        constraints = LinearConstraint(vectors, lb=joltages, ub=joltages)
        integrality = np.ones(shape=[len(buttons)])
        c = np.ones(shape=[len(buttons)])
        res = milp(c=c, integrality=integrality, constraints=constraints)
        presses = [int(round(item)) for item in res.x]
        assert res.success
        logger.info(f"presses = {presses}")
        logger.info(f"sum = {sum(presses)}")
        logger.info(f"fun = {round(res.fun)}")
        if int(round(res.fun)) != sum(presses):
            logger.info(f"sum/func mismatch:\n{res}")
        pushes += int(round(res.fun))
        logger.info(f"total = {pushes}")

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
    logger.info(f"Part 2:\n  Pushes required to match required joltages: {output}")
    t.toc()
    assert output > 20275

if __name__ == '__main__':
    logger = start_logging()
    logger.info("starting log")
    main()
