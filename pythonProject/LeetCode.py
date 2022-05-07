nums = [2, 7, 11, 15]
target = 9


def twoSum(nums, target):
    num_to_index = {}

    for i, num in enumerate(nums):
        print(i, '. ', num)
        if target - num in num_to_index:
            print( num_to_index[target - num], i )
            return [num_to_index[target - num], i]
        num_to_index[num] = i

    print(num_to_index)


newsums = twoSum(nums, target)
print(newsums)
