def is_even(num: int) -> bool:
    """Check if a number is even."""
    return (num % 2 == 0)


def check_list(sorted_num: list):
    """Check if the list is valid for statistics calculations."""
    if len(sorted_num) == 0:
        raise ValueError("List is empty")
    if not all(isinstance(i, (int, float)) for i in sorted_num):
        # type error ?
        raise ValueError("List must contain only numbers")
    return True


def ft_mean(sorted_num: list) -> str:
    """Calculate the mean of a list of numbers."""
    check_list(sorted_num)
    mean = sum(sorted_num) / len(sorted_num)
    return str(mean)


def ft_median(nums: list) -> str:
    """Calculate the median of a list of numbers."""
    check_list(nums)
    nums.sort()
    if (not is_even(len(nums))):
        index = len(nums) // 2
        return str(nums[index])
    else:
        res = (nums[len(nums) // 2 - 1] + nums[len(nums) // 2]) / 2
        return str(res)


def ft_quartile(nums: list) -> str:
    """Calculate the first and third quartiles of a list of numbers."""
    check_list(nums)
    nums.sort()
    lnums = len(nums)
    try:
        assert lnums >= 4
        q1 = nums[lnums // 4]
        q3 = nums[3 * lnums // 4]
        return [float(q1), float(q3)]
    except AssertionError:
        raise ValueError("List must contain at least 4 elements \
                         for quartile calculation")


def ft_variance(nums: list):
    """Calculate the variance of a list of numbers."""
    check_list(nums)
    nums.sort()
    mean = float(ft_mean(nums))
    var = sum([(elem - mean) ** 2 for elem in nums]) / (len(nums))
    return (str(var))


def ft_std(nums: list) -> str:  # ecart type
    """Calculate the standard deviation of a list of numbers."""
    check_list(nums)
    nums.sort()
    std = float(ft_variance(nums)) ** 0.5
    return (str(std))


def ft_statistics(*args: any, **kwargs: any) -> None:
    """Calculate statistics based on provided numbers and operations."""
    numbers = list(args)
    for key, value in kwargs.items():
        if (len(numbers) > 0):
            try:
                match value:
                    case "mean":
                        print("mean :", ft_mean(numbers))
                    case "median":
                        print("median :", ft_median(numbers))
                    case "quartile":
                        print("quartile :", ft_quartile(numbers))
                    case "std":
                        print("std :", ft_std(numbers))
                    case "var":
                        print("var :", ft_variance(numbers))
                    case _:
                        pass
            except ValueError as e:
                print("ERROR:", e)
        else:
            print("ERROR")
