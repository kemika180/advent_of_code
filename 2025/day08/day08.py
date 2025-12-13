from sys import argv
from aoc_logging import start_logging
from pytictoc import TicToc
from typing import Tuple
from math import sqrt

def read_file(filename: str) -> list:
    data_list = []
    with open(filename) as file:
        try:
            logger.info(f"opening {filename}")
            for line in file:
                line = line.rstrip().split(",")
                line = [int(num) for num in line]
                data_list.append(line)
        except FileNotFoundError:
            logger.error("file not found")
            raise FileNotFoundError("file not found")

    return data_list

def parse_data(data: list) -> dict:
    logger.info("parsing data")
    j_dict = {}
    for n, (x, y, z) in enumerate(data):
        j_dict[f"J{n}"] = {"x": x,"y": y,"z": z}

    return j_dict

def process_junctions(junctions: dict) -> dict:
    logger.info("processing junctions")
    distances = {}
    keys = list(junctions.keys())
    for n, x in enumerate(keys):
        i = junctions[x]
        for y in keys[n+1:]:
            j = junctions[y]
            distances[(x, y)] = {"d": round(sqrt((i["x"]- j["x"])**2 + (i["y"]-j["y"])**2 + (i["z"]-j["z"])**2), 3)}
    key_list = list(sorted(distances, key=lambda item: distances[item]["d"]))
    for key in key_list:
        i, j = key
        logger.info(f"{key}: {distances[key]["d"]} - ({junctions[i]["x"]},{junctions[i]["y"]},{junctions[i]["z"]})x({junctions[j]["x"]},{junctions[j]["y"]},{junctions[j]["z"]})")

    return distances

def connect_junctions(distances: dict, size: int) -> Tuple[list, list, int, int]:
    logger.info(f"connecting {size} junctions")
    circuits = []
    key_list = list(sorted(distances, key=lambda item: distances[item]["d"]))

    for _ in range(size):
        key = key_list.pop(0)
        i, j = key
        logger.info(f"  connecting {i} to {j}")
        for circuit in circuits:
            if i in circuit and j in circuit:
                break
            elif i in circuit and j not in circuit:
                circuit.append(j)
                break
            elif i not in circuit and j in circuit:
                circuit.append(i)
                break
        else:
            circuits.append([i, j])

    check_circuits = True
    logger.info(f"\nchecking circuits for connections")
    while check_circuits:
        check_circuits = False
        new_circuits = []
        removed_circuits = []
        for i, circuit1 in enumerate(circuits):
            if circuit1 in removed_circuits:
                continue
            for circuit2 in circuits[i+1:]:
                if circuit2 in removed_circuits:
                    continue
                if bool(set(circuit1).intersection(circuit2)):
                    check_circuits = True
                    logger.info(f"  joining {circuit1} and {circuit2}")
                    circuit1 = set(circuit1).union(circuit2)
                    if circuit2 not in removed_circuits:
                        removed_circuits.append(circuit2)
            new_circuits.append(list(circuit1))
        circuits = new_circuits

    logger.info("\ncircuits:")
    for circuit in circuits:
        logger.info(f"  {circuit}")
    sizes = []
    for circuit in circuits:
        sizes.append(len(circuit))
    sizes.sort(reverse=True)
    logger.info(f"{sizes = }")
    result = sizes[0]*sizes[1]*sizes[2]

    return circuits, key_list, len(circuits), result

def join_circuits(junctions: dict, circuits: list, distances: list):
    for junction in junctions:
        for circuit in circuits:
            if junction not in circuit:
                continue
            else:
                break
        else:
            circuits.append([junction])

    last1 = "error"
    last2 = "error"

    while len(circuits) > 1:
        key = distances.pop(0)
        i, j = key
        logger.info(f"  connecting {i} to {j}")
        for circuit in circuits:
            if i in circuit and j in circuit:
                break
            elif i in circuit and j not in circuit:
                circuit.append(j)
                break
            elif i not in circuit and j in circuit:
                circuit.append(i)
                break
        else:
            circuits.append([i, j])

        last1 = i
        last2 = j

        check_circuits = True
        logger.info(f"\nchecking circuits for connections")
        while check_circuits:
            check_circuits = False
            new_circuits = []
            removed_circuits = []
            for i, circuit1 in enumerate(circuits):
                if circuit1 in removed_circuits:
                    continue
                for circuit2 in circuits[i+1:]:
                    if circuit2 in removed_circuits:
                        continue
                    if bool(set(circuit1).intersection(circuit2)):
                        check_circuits = True
                        logger.info(f"  joining {circuit1} and {circuit2}")
                        circuit1 = set(circuit1).union(circuit2)
                        if circuit2 not in removed_circuits:
                            removed_circuits.append(circuit2)
                new_circuits.append(list(circuit1))
            circuits = new_circuits

    print(f"last added were {last1} at {junctions[last1]} and {last2} at {junctions[last2]}")
    return junctions[last1]['x'] * junctions[last2]['x']

def main():
    if len(argv) == 1:
        filename = "example.txt"
    else:
        filename = argv[1]
    t = TicToc()

    if filename == "example.txt":
        size = 10
    else:
        size = 1000
    data = read_file(filename)
    t.tic()
    junctions = parse_data(data)
    distances = process_junctions(junctions)
    circuits, distances, circuit_num, result = connect_junctions(distances, size)
    logger.info(f"Part 1:\n  Total number of circuits = {circuit_num}")
    logger.info(f"  Resultant product = {result}")
    t.toc()
    t.tic()
    answer = join_circuits(junctions, circuits, distances)
    logger.info(f"Part2:\n  Product of the x coordinate of the last 2 junctions = {answer}")
    t.toc()

if __name__ == '__main__':
    logger = start_logging()
    logger.info("starting log")
    main()
