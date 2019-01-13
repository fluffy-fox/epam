from time import sleep
import functools

def delay(func):
    @functools.wraps(func)
    def wrapper(*args):
        sleep(3)
        return func(*args)
    return wrapper
