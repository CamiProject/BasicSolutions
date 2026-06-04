# 除了暴力枚举以外，还有prefix方法，核心思想是 前缀和 + 哈希表：
# 时间复杂度为 O(n)，一次遍历

def subarraySum(nums, k):
    prefix = 0          # 当前前缀和
    count = 0           # 满足条件的子数组个数
    mp = {0: 1}         # 哈希表：前缀和 -> 出现次数，初始放入 0（表示空前缀）
    for x in nums:
        prefix += x                     # 更新当前前缀和
        if prefix - k in mp:            # 检查是否存在所需前缀和
            count += mp[prefix - k]     # 加上出现次数
        mp[prefix] = mp.get(prefix, 0) + 1  # 记录当前前缀和（给后面使用）
# 等价于：
# if prefix in mp:
#     mp[prefix] = mp[prefix] + 1
# else:
#     mp[prefix] = 1
