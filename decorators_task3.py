"""
Create decorator validate, which validates arguments in the set_pixel function.
All function parameters should be between 0(int) and 256(int) inclusive.
If all parameters are valid, the set_pixel function should return a "Pixel created!" message.
Otherwise, it should return the "Function call is not valid!" message.
Use functools.wraps where necessary.
Don't forget about doc strings.
"""
from functools import wraps


def validate(fn):
    @wraps(fn)
    def wrapper(*args):
        for i in args:
            if i < 0 or i > 256:
                return "Function call is not valid!"
        return fn(*args)
    return wrapper


@validate
def set_pixel(x: int, y: int, z: int) -> str:
  return "Pixel created!"


print(set_pixel(256, 256, 256))
