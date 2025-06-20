def callLimit(limit: int):
    """Decorator to limit the number of calls to a function."""
    count = 0

    def callLimiter(function):
        """Actual decorator that tracks the call count."""
        def limit_function(*args: any, **kwds: any):
            """Function that limits the number of calls"""
            nonlocal count
            if (count) < limit:
                count += 1
                return function(*args, **kwds)
            else:
                print(f"Error: {function} call to many times.")
        return limit_function
    return callLimiter
