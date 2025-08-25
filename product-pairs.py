"""
You are given an array of non-negative integers and a target product.
Write a function that prints all unique pairs of numbers from the array, whose multiplication equals the target product.

Example:
Input:
arr = [7, 1, 2, 3, 4, 5, 6]
product = 12

Output:
(3, 4), (2, 6)
or
(4, 3), (6, 2)

Notes:
Each pair should be printed only once. For example, if you print (3, 4), you should not print (4, 3) again.
If no such pairs exist, the function should not print anything.
"""

from __future__ import annotations
import timeit


def product_pairs(arr: list[int], target: int) -> list[tuple[int, int]]:
    pairs: list[tuple[int, int]] = []

    possible_pairs: dict[int, int] = {}

    for i in arr:
        # print(f"i = {i}")
        if i in possible_pairs:
            pair = (possible_pairs.pop(i), i)
            pairs.append(pair)
            # print(f"pair:{pair}")
            # print(f"possible pairs: {possible_pairs}")
        elif target % i == 0:
            # print(f"target % i {target % i}")
            factor: int = int(target / i)
            # print(f"factor = {factor}")
            possible_pairs[factor] = i
            # print(f"possible pairs: {possible_pairs}")
        else:
            pass

    # print(f"final pairs: {pairs}")
    # print(f"final possible pairs: {possible_pairs}")
    return pairs


def test():
    result = product_pairs([7, 1, 2, 3, 4, 5, 6], 12)
    expected = [(3, 4), (2, 6)]
    print(f"Result: {result}, Expected: {expected}")
    assert result == expected


if __name__ == "__main__":
    execution_time = timeit.timeit(test, number=1)
    print(f"Execution time: {execution_time:.6f} seconds")
