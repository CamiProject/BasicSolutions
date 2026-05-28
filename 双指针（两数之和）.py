# 解决“两数之和 II - 输入有序数组”，核心思想是利用数组的有序性，通过两个指针从两端向中间逼近。
# 达到时间复杂度O（n）【只遍历一遍】，空间复杂度O（1）【常数级的额外变量】

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
