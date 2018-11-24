from time import time
import sys
import bloodcomp

if len(sys.argv) < 3:
    print("usage: main.py <dataset_file> <-b | -g | -p> [-t]")
    print("  options: \n"
          "   -b, Brutal force algorithm execution\n"
          "   -g, Greedy Algorithm execution\n"
          "   -p, Prim of a route\n"
          "   -t, Execution with time")

if len(sys.argv) == 3:
    if sys.argv[3] == "-b":
        persons = open(sys.argv[1], "r").read().split("\n")
        bloodcomp.get_combinations(persons)
    if sys.argv[3] == "-g":
        persons_sorted = sorted(persons, key=lambda x: x.split(":")[-1])
        bloodcomp.get_combinations(persons_sorted)
    if sys.argv[3] == "-p":
        print()

if sys.argv[3] == "-t":
    if sys.argv[3] == "-b":
        startTime = time()
        persons = open(sys.argv[1], "r").read().split("\n")
        bloodcomp.get_combinations(persons)
        elapsedTime = time() - startTime
        print("\nTotal execution time:", elapsedTime * 1000, "milliseconds")
    if sys.argv[3] == "-g":
        startTime = time()
        persons_sorted = sorted(persons, key=lambda x: x.split(":")[-1])
        bloodcomp.get_combinations(persons_sorted)
        elapsedTime = time() - startTime
        print("\nTotal execution time:", elapsedTime * 1000, "milliseconds")
    if sys.argv[3] == "-p":
        startTime = time()

        elapsedTime = time() - startTime
        print("\nTotal execution time:", elapsedTime * 1000, "milliseconds")
