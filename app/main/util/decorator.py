import functools

class FibDecorators(object):
    @classmethod
    def memoize_fib(f):
        cache = {}
        def decorated_function(*args):
            if args in cache:
                return cache[args]
            else:
                cache[args] = f(*args)
                return cache[args]
        return decorated_function