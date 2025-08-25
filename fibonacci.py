from __future__ import annotations
import timeit

"""
1, 1, 2, 3, 5, 8, 13, 21
"""


def fib(n: int) -> int:
    if n <= 2:
        return 1
    else:
        fibsum: int = fib(n - 1) + fib(n - 2)
    return fibsum


def superfib(n: int) -> int:
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


def test1():
    result = fib(10)
    expected = 55
    print(f"Result: {result}, Expected: {expected}")
    # assert result == expected


def test2():
    result = fib(20)
    expected = 6765
    print(f"Result: {result}, Expected: {expected}")
    # assert result == expected


def test3():
    result = superfib(10)
    expected = 55
    print(f"Result: {result}, Expected: {expected}")
    # assert result == expected


def test4():
    result = superfib(20)
    expected = 6765
    print(f"Result: {result}, Expected: {expected}")
    # assert result == expected


if __name__ == "__main__":
    execution_time = timeit.timeit(test1, number=1)
    print(f"Execution time: {execution_time:.6f} seconds")
    execution_time = timeit.timeit(test2, number=1)
    print(f"Execution time: {execution_time:.6f} seconds")
    execution_time = timeit.timeit(test3, number=1)
    print(f"Execution time: {execution_time:.6f} seconds")
    execution_time = timeit.timeit(test4, number=1)
    print(f"Execution time: {execution_time:.6f} seconds")
