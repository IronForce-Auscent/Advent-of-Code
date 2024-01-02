import functools
import time

def timer(func):
    @functools.wraps(func)
    def wrapper_timer(*args, **kwargs):
        start = time.perf_counter()
        value = func(*args, **kwargs)
        end = time.perf_counter()
        delta = end - start
        print(f"Elapsed time: {delta:0.10f} seconds")
        return value
    return wrapper_timer