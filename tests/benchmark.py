import os, sys
sys.path.append(os.path.realpath(os.path.join(os.path.dirname(__file__), '..')))

import timeit

BENCHMARK_ITERATIONS = 1000000
NANOS_IN_SECOND = 1000000000

def measure(name, stmt, setup, count):
  timer = timeit.Timer(stmt, setup)
  total_nanos = timer.timeit(count) * NANOS_IN_SECOND
  per_op_nanos = round(total_nanos / count, 1)
  print("%-18s%14s%20s ns/op" % (name, count, per_op_nanos))

measure("damm.Digit (small)", "damm.Digit('123')", "import damm", BENCHMARK_ITERATIONS)
measure("damm.Digit (large)", "damm.Digit('00123014764700968325')", "import damm", BENCHMARK_ITERATIONS)
