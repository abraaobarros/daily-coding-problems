def find_num(nums, target):
    low = -1
    high = -1
    for pointer in range(0, len(nums)):
        if nums[pointer] == target:
            high = pointer
            if low == -1:
                low = pointer

    return (low, high)


  # Fill this in.
print(find_num([1, 1, 3, 5, 7], 1))
# (0, 1)
print(find_num([1, 2, 3, 4], 5))
