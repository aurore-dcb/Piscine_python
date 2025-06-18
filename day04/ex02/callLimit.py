def callLimit(limit: int):
    """Decorator to limit the number of calls to a function."""
    count = 0
    def callLimiter(function):
        # docstring ?
        def limit_function(*args: any, **kwds: any):
            # docstring ?
            nonlocal count
            if (count) < limit:
                count += 1
                return function(*args, **kwds)
            else:
                print(f"Error: {function} call to many times.")
        return limit_function
    return callLimiter
