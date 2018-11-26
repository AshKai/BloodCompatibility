from time import time
import sys
import bloodcomp
import prim

if len(sys.argv) < 3:
    print("usage: main.py <dataset_file> <-b | -g | -p> [-t]")
    print("  options: \n"
          "   -b, Brutal force algorithm execution\n"
          "   -g, Greedy Algorithm execution\n"
          "   -p, Prim of a route\n"
          "   -t, Execution with time")

if len(sys.argv) == 3:
    if sys.argv[2] == "-b":
        persons = open(sys.argv[1], "r").read().split("\n")
        bloodcomp.get_combinations(persons)
    if sys.argv[2] == "-g":
        persons_sorted = sorted(open(sys.argv[1], "r").read().split("\n"), key=lambda x: x.split(":")[-1])
        bloodcomp.get_combinations(persons_sorted)
    if sys.argv[2] == "-p":
        graph = open(sys.argv[1], "r").read().split("\n")
        prim.init(graph)

if len(sys.argv) == 4 and sys.argv[3] == "-t":
    if sys.argv[2] == "-b":
        startTime = time()
        persons = open(sys.argv[1], "r").read().split("\n")
        bloodcomp.get_combinations(persons)
        elapsedTime = time() - startTime
        print("\nTotal execution time:", elapsedTime * 1000, "milliseconds")
    if sys.argv[2] == "-g":
        startTime = time()
        persons_sorted = sorted(open(sys.argv[1], "r").read().split("\n"), key=lambda x: x.split(":")[-1])
        bloodcomp.get_combinations(persons_sorted)
        elapsedTime = time() - startTime
        print("\nTotal execution time:", elapsedTime * 1000, "milliseconds")
    if sys.argv[2] == "-p":
        startTime = time()

        elapsedTime = time() - startTime
        print("\nTotal execution time:", elapsedTime * 1000, "milliseconds")
