def give_bmi(height: list[int | float], weight: list[int | float]) -> list[int | float]:
    try:
        assert isinstance(height, list)
        assert isinstance(weight, list)
        assert len(height) == len(weight)
        assert all(type(elem) is int or type(elem) is float for elem in height)
        assert all(type(elem) is int or type(elem) is float for elem in weight)
    except AssertionError:
        print("AssertionError: bad argument format")
        return
    res = [w / (h * h) for w, h in zip(weight, height)]
    return res


def apply_limit(bmi: list[int | float], limit: int) -> list[bool]:
    try:
        assert bmi is not None
        assert all(type(elem) is int or type(elem) is float for elem in bmi)
        assert type(limit) is int
    except AssertionError:
        print("AssertionError: bad argument format")
        return
    return [elem > limit for elem in bmi]
