#dekorator co to by liczyl czas ile sie cos wykonuje
from functools import wraps
import time

class ClassDecorator:
    def __init__(self, func):
        self._func = func
        self.N = 0
        self.sum_time = 0
        self.min = 0
        self.max = 0

    def __call__(self, *args, **kwargs):
        #calculating time
        start_time = time.perf_counter()
        result = self._func(*args, **kwargs)
        end_time = time.perf_counter()
        total_time = end_time - start_time
        
        #calculating average performance
        self.N += 1
        self.sum_time += total_time
        average = self.sum_time/self.N

        #minimum and maximum
        if (self.N == 0):
            self.min = total_time
            self.max = total_time
        if (total_time < self.min):
            self.min = total_time
        if(total_time > self.max):
            self.max = total_time
        
        #printing results
        print(f' Function {self._func.__name__}{args} {kwargs} Took {total_time:.4f} seconds. On average it took: {average:.4f}, Minimum: {self.min:.4f}, Maximum: {self.max:.4f}')
        return self._func(*args, **kwargs)

@ClassDecorator
def calculate_something(num):
    """
    Simple function that returns sum of all numbers up to the square of num.
    """
    total = sum((x for x in range(0, num**2)))
    return total


calculate_something(10)
calculate_something(100)
calculate_something(1000)
calculate_something(5000)
calculate_something(10000)

