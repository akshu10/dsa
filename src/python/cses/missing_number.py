"""
You are given all numbers between 1,2,...,n except one. Your task is to find the missing number.
Input
The first input line contains an integer n.
The second line contains n-1 numbers. Each number is distinct and between 1 and n (inclusive).
Output
Print the missing number.


Example
Input:
5
2 3 1 5

Output:
4
"""


def missing_number():
    n = int(input())
    sumOfN = n * (n + 1) // 2

    difference = sumOfN
    for num_str in input().split():
        num = int(num_str)

        difference -= num

    print(difference)


missing_number()
