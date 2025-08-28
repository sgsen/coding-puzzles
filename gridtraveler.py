from __future__ import annotations
import timeit

"""
Problem:
m x n grid
start at top left
can only move down and to the right
function should return how many possible paths to get to bottom right

Results:
❯ uv run gridtraveler.py using gridTraveler function below
Result: 1, Expected: 1
Execution time: 0.000013 seconds
Result: 3, Expected: 3
Execution time: 0.000007 seconds
Result: 3, Expected: 3
Execution time: 0.000004 seconds
Result: 6, Expected: 6
Execution time: 0.000004 seconds
Result: 2333606220, Expected: 2333606220
Execution time: 368.973189 seconds

❯ uv run gridtraveler.py using memoGridTraveler function below
Result: 1, Expected: 1
Execution time: 0.000012 seconds
Result: 3, Expected: 3
Execution time: 0.000007 seconds
Result: 3, Expected: 3
Execution time: 0.000004 seconds
Result: 6, Expected: 6
Execution time: 0.000004 seconds
Result: 2333606220, Expected: 2333606220
Execution time: 0.000056 seconds
"""


def gridTraveler(m: int, n: int) -> int:
    if m == 0 or n == 0:
        totalPaths = 0
    elif m == 1 or n == 1:
        totalPaths = 1
    else:
        totalPaths = gridTraveler(m - 1, n) + gridTraveler(m, n - 1)
    return totalPaths


def memoGridTraveler(m: int, n: int, memo: dict[tuple[int, int], int] = {}) -> int:
    if (m, n) in memo:
        totalPaths = memo[(m, n)]
    elif (n, m) in memo:
        totalPaths = memo[(n, m)]
    elif m == 0 or n == 0:
        totalPaths = 0
    elif m == 1 or n == 1:
        totalPaths = 1
    else:
        memo[(m, n)] = memoGridTraveler(m - 1, n, memo) + memoGridTraveler(
            m, n - 1, memo
        )
        totalPaths = memo[(m, n)]
    return totalPaths


def test1():
    result = memoGridTraveler(1, 1)
    expected = 1
    print(f"Result: {result}, Expected: {expected}")
    assert result == expected


def test2():
    result = memoGridTraveler(2, 3)
    expected = 3
    print(f"Result: {result}, Expected: {expected}")
    assert result == expected


def test3():
    result = memoGridTraveler(3, 2)
    expected = 3
    print(f"Result: {result}, Expected: {expected}")
    assert result == expected


def test4():
    result = memoGridTraveler(3, 3)
    expected = 6
    print(f"Result: {result}, Expected: {expected}")
    assert result == expected


def test5():
    result = memoGridTraveler(18, 18)
    expected = 2333606220
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
    execution_time = timeit.timeit(test5, number=1)
    print(f"Execution time: {execution_time:.6f} seconds")
