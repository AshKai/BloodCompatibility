from time import time
import sys
import bloodcomp

# dataset_file format: "Laura-21581654L:Y"

if len(sys.argv) < 3:
    print("usage: main.py <dataset_file> <-b | -g> [-o] [-t]")
    print("  options: \n"
          "   -b, Brutal force algorithm execution\n"
          "   -g, Greedy Algorithm execution\n"
          "   -o, Execution with output\n"
          "   -t, Execution with time")

if len(sys.argv) == 3:
    if sys.argv[2] == "-b":
        persons = open(sys.argv[1], "r").read().split("\n")
        bloodcomp.get_combinations(persons, False)
    if sys.argv[2] == "-g":
        # doesn't work properly, needs an heuristic
        persons_sorted = sorted(open(sys.argv[1], "r").read().split("\n"), key=lambda x: x.split(":")[-1])
        bloodcomp.get_combinations(persons_sorted, False)

if len(sys.argv) == 4 and sys.argv[3] == "-t":
    if sys.argv[2] == "-b":
        startTime = time()
        persons = open(sys.argv[1], "r").read().split("\n")
        bloodcomp.get_combinations(persons, False)
        elapsedTime = time() - startTime
        print("\nTotal execution time:", elapsedTime * 1000, "milliseconds")
    if sys.argv[2] == "-g":
        startTime = time()
        # doesn't work properly, needs an heuristic
        persons_sorted = sorted(open(sys.argv[1], "r").read().split("\n"), key=lambda x: x.split(":")[-1])
        bloodcomp.get_combinations(persons_sorted, False)
        elapsedTime = time() - startTime
        print("\nTotal execution time:", elapsedTime * 1000, "milliseconds")

if len(sys.argv) == 4 and sys.argv[3] == "-o":
    if sys.argv[2] == "-b":
        persons = open(sys.argv[1], "r").read().split("\n")
        bloodcomp.get_combinations(persons, True)
    if sys.argv[2] == "-g":
        # doesn't work properly, needs an heuristic
        persons_sorted = sorted(open(sys.argv[1], "r").read().split("\n"), key=lambda x: x.split(":")[-1])
        bloodcomp.get_combinations(persons_sorted, True)

if len(sys.argv) == 5 and sys.argv[4] == "-t" and sys.argv[3] == "-o":
    if sys.argv[2] == "-b":
        startTime = time()
        persons = open(sys.argv[1], "r").read().split("\n")
        bloodcomp.get_combinations(persons, True)
        elapsedTime = time() - startTime
        print("\nTotal execution time:", elapsedTime * 1000, "milliseconds")
    if sys.argv[2] == "-g":
        startTime = time()
        # doesn't work properly, needs an heuristic
        persons_sorted = sorted(open(sys.argv[1], "r").read().split("\n"), key=lambda x: x.split(":")[-1])
        bloodcomp.get_combinations(persons_sorted, True)
        elapsedTime = time() - startTime
        print("\nTotal execution time:", elapsedTime * 1000, "milliseconds")
