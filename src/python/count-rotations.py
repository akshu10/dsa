def count_rotation_linear_search(nums: list[int]) -> int:
    """
    An attempt at a brute force solution
    Idea: The number of the rotations is basically the position of smallest/first element
    in the current list.
    Since that shows how much the element has moved/rotated to the right
    """

    for i in range(1, len(nums)):
        if nums[i] < nums[i - 1]:
            return i

    return 0


def count_rotation_binary_search(nums: list[int]) -> int:

    low = 0
    high = len(nums) - 1

    while low <= high:

        ## This means the array is already sorted therefor 0 rotations were made [EDGE CASE]
        if nums[low] <= nums[high]:
            return low

        # Find the middle element
        middle = (low + high) // 2
        next_index = (middle + 1) % len(nums)
        prev_index = (middle - 1 + len(nums)) % len(nums)

        # Check if the middle element is the smallest element
        if nums[middle] <= nums[prev_index] and nums[middle] <= nums[next_index]:
            return middle

        ## If the middle element is not smallest element such on the right/left of the list
        if nums[middle] >= nums[low]:
            # The left half is sorted, so the drop-off is on the right.
            # Move the 'low' bookend past the middle.
            low = middle + 1

        else:
            # The right half is sorted, so the drop-off is on the left.
            # Move the 'high' bookend before the middle.
            high = middle - 1

    return 0


test_cases = [
    {"input": {"nums": []}, "output": 0},
    {"input": {"nums": [1]}, "output": 0},
    {"input": {"nums": [5, 7, 8, 1, 3, 4]}, "output": 3},
    {"input": {"nums": [6, -2, 0, 1, 3]}, "output": 1},
]


for test in test_cases:
    print(count_rotation_linear_searchs(**test["input"]) == test["output"])
    print(count_rotation_binary_search(**test["input"]) == test["output"])
