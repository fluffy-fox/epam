def raises(args):
    def decorator(func):
        def wrapper():
            try:
                return func()
            except:
                raise args
        return wrapper
    return decorator
