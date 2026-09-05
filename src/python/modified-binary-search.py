def binary_search(array: list[int], query: int) -> int:
    """
    This is a modified version of the binary which basically allows
    to search for the first occuring value of an element.
    Usually binary search does not always return the first occuring (first occurence) value from the left.
    But we can modify the algorithm a bit to support this behaviour.
    Only works for ASCENDING (as for descending the comparison has to change but the idea is the same)

    Test cases: [1,1] query = 1 || [] query = 2 || [1,2,3,4,5,6,7,7,8,8,9] query = 8
    """

    low: int = 0
    high: int = len(array) - 1

    while low <= high:
        middle_index = (low + high) // 2
        middle_element = array[middle_index]

        if middle_element == query:

            ## This line peeps at the previous element (to find the fist occurence).
            ## For descending array you'd look at middle_index + 1 instead.
            if middle_index - 1 >= 0 and array[middle_index - 1] == query:
                high = middle_index - 1
            else:
                return middle_index

        elif middle_element < query:  # look on the right side of the array
            low = middle_index + 1
        else:
            high = middle_index - 1

    return -1


test_cases = [
    {"input": {"array": [1, 2, 3, 4, 5, 6, 7, 8], "query": 8}, "output": 7},
    {"input": {"array": [1, 2, 3, 4, 5, 6, 7, 8], "query": 22}, "output": -1},
    {
        "input": {"array": [1, 2, 3, 4, 5, 6, 7, 7, 7, 7, 7, 8], "query": 7},
        "output": 6,
    },
    {
        "input": {"array": [1, 2, 3, 5, 5, 6, 7, 7, 9, 12, 15], "query": 5},
        "output": 3,
    },
]


for test in test_cases:
    print(binary_search(**test["input"]) == test["output"])
