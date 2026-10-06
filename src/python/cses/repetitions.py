"""
You are given a DNA sequence: a string consisting of characters A, C, G, and T.
Your task is to find the longest repetition in the sequence. This is a maximum-length substring containing only one type of character.


Input
The only input line contains a string of n characters.


Output
Print one integer: the length of the longest repetition.
Constraints
Example
Input:
ATTCGGGA

Output:
"""

"""
idea: just increment the right wind
"""


def repetitions():

    string = input()

    same_char_count = 1
    previous_character = string[0]
    max_length = 1

    for i in range(1, len(string)):

        if previous_character and string[i] != previous_character:
            same_char_count = 1

        elif previous_character and previous_character == string[i]:
            same_char_count += 1

        max_length = max(same_char_count, max_length)
        previous_character = string[i]

    print(max_length)


repetitions()
