# 目标是：长度为 n 的数组，所有数字在 1到n 的范围中 （1 < x < n)，数组中有重复数字 也有消失的缺失的数字，找出所有没出现过的数字。
# 解法1：核心思路是 集合法， seen = set(nums) 集合化之后，由“可重复、有索引”状态变成了“不重复、无索引”状态。

def findDisappearedNumbers(nums):
    seen = set(nums)
    
    missing = []
    for x in range(1, len(nums)+1):
        if x not in seen:
            missing.append(x)
    return missing
