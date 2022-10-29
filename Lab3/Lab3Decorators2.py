import functools
import time

#@functools.lru_cache
def fibon(n):
    if n <2:
        return n
    return fibon(n-1) + fibon(n-2)

start = time.time()
for n in range(40):
    print(n, fibon(n))
stop = time.time()

print(f'{stop-start =}')