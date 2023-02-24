"""
Create a decorator function time_decorator which has to calculate the decorated function execution time and
put this time value in the execution_time dictionary where the key is the decorated function name.
The value is this function's execution time.
"""
from typing import Dict
import time

execution_time: Dict[str, float] = {}


def time_decorator(fn):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = fn(*args, **kwargs)
        end_time = time.time()
        total_time = end_time - start_time
        execution_time[fn.__name__] = total_time
        return result
    return wrapper


@time_decorator
def func_add(a, b):
    time.sleep(0.2)
    return a + b


print(func_add(10, 20))
print(execution_time)
