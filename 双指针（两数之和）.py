def twoSum_twoPointer(nums, target):
    left, right = 0, len(nums) - 1
    while left < right:
        summ = nums[left] + nums[right]
        if summ == target:
            return [left, right]
        elif summ < target:
            left += 1
        else:
            right -= 1
    return [-1, -1]
