"""
Write a decorator that logs information about calls of decorated functions,
the values of its arguments, keyword arguments, and execution time.
The log should be written to a file.
"""
import time
import logging

logger = logging.getLogger(__name__)


def log(fn):
    def wrapper(*args, **kwargs):
        logger.info('%s(%s, %s)', fn, args, kwargs)
        start_time = time.time()
        result = fn(*args, **kwargs)
        print(kwargs)
        end_time = time.time()
        total_time = end_time - start_time
        args_text = ''
        for i in range(len(args)):
            if i == 0:
                args_text += f'a={args[0]}, '
            if i == 1:
                args_text += f'b={args[1]}, '
            if i == 2:
                args_text += f'c={args[2]}, '
        kwargs_text = ''
        for i in kwargs:
            kwargs_text += f'{i}={kwargs[i]}, '

        with open('log.txt', 'a') as f:
            f.writelines(f"{fn.__name__}; args: {args_text[:len(args_text)-2]}; kwargs: {kwargs_text[:len(kwargs_text)-2] }; execution time: {total_time:.2f} sec.")
        return result
    return wrapper


@log
def foo(a, b, c, d):
    ...


print(foo(1, 2, c=3, d=5))
