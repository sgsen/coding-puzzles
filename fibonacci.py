from __future__ import annotations
import timeit

"""
1, 1, 2, 3, 5, 8, 13, 21
"""


def ogfib(n: int) -> int:
    if n <= 2:
        return 1
    else:
        fibsum: int = ogfib(n - 1) + ogfib(n - 2)
    return fibsum


def memofibfail(n: int) -> int:
    fibsums: dict[int, int] = {1: 1, 2: 1}

    def minifib(n: int = n, fibsums: dict[int, int] = {}) -> dict[int, int]:
        if n in fibsums:
            return fibsums
        else:
            fibsums1 = minifib(n - 1, fibsums)
            fibsums2 = minifib(n - 2, fibsums)
            fibsums[n] = fibsums1[n - 1] + fibsums2[n - 2]
            return fibsums

    fibsums = minifib(n, fibsums)
    result: int = fibsums[5]
    return result


def memofib(n: int, memo: dict[int, int] = {}) -> int:
    if n in memo:
        return memo[n]
    elif n <= 2:
        return 1
    else:
        memo[n] = memofib(n - 1, memo) + memofib(n - 2, memo)
        return memo[n]


def sumfib(n: int) -> int:
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
    return a


def test1():
    result = sumfib(10)
    expected = 55
    print(f"Result: {result}, Expected: {expected}")
    assert result == expected


def test2():
    result = sumfib(50)
    expected = 12586269025
    print(f"Result: {result}, Expected: {expected}")
    assert result == expected


def test3():
    result = memofib(10)
    expected = 55
    print(f"Result: {result}, Expected: {expected}")
    assert result == expected


def test4():
    result = memofib(50)
    expected = 12586269025
    print(f"Result: {result}, Expected: {expected}")
    assert result == expected


if __name__ == "__main__":
    execution_time = timeit.timeit(test1, number=1)
    print(f"Execution time: {execution_time:.6f} seconds")
    execution_time = timeit.timeit(test2, number=1)
    print(f"Execution time: {execution_time:.6f} seconds")
    execution_time = timeit.timeit(test3, number=1)
    print(f"Execution time: {execution_time:.6f} seconds")
    execution_time = timeit.timeit(test4, number=1)
    print(f"Execution time: {execution_time:.6f} seconds")
