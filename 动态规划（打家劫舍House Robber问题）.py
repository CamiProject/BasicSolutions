# 目标 = 一个list，每次不能同时偷相邻的两家，要求收益最大。
# 核心思路：自底向上的动态规划
# 核心方程：状态转移方程 f(i) = max(f(i - 1), f(i - 2) + nums[i])
# 当走到第 i 个房子时，只有两个选择：①不偷这一家，最大收益等于 f(i - 1) 上一家为止的钱、 ②偷这一家，收益等于f(i - 2) + nums[i]

def rob(nums):
    if not nums:
        return 0
    if len(nums) == 1:
        return nums[0]
    prev2 = nums[0]
    prev1 = max(nums[0], nums[1])
    for i in range(2, len(nums)):
        curr = max(prev1, prev2 + nums[i])
        prev2 = prev1
        prev1 = curr
    return prev1
