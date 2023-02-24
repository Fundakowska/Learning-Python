"""
Create a decorator factory (decorator itself).
The factory accepts a function (lambda) as an input and returns a decorator
that will return the result of the function as the first argument.
The result of the decorated function is passed.
The function that the factory accepts can only take one positional parameter.
"""


def decorator_apply(lambda_func):
    def decorator_function(fn):
        def wrapper(a):
            return fn(lambda_func(a))
        return wrapper
    return decorator_function


@decorator_apply(lambda user_id: user_id + 1)
def return_user_id(num: int) -> int:
    return num


print(return_user_id(42))
