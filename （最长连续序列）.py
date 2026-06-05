# 基础解法是 排序 + 连续检测

def longestConsecutive(nums):
    # 边界处理：如果列表为空，直接返回0
    if not nums:
        return 0

    # 对数组进行排序，使连续数字相邻
    nums.sort()

    # 初始化变量
    max_len = 1      # 记录全局最长连续序列长度
    current_len = 1  # 记录当前正在遍历的连续序列长度

    # 从第二个元素开始遍历（索引1）
    for i in range(1, len(nums)):
        if nums[i] == nums[i - 1]:
            # 情况1：重复元素（例如 [1, 2, 2, 3] 中的两个2）
            # 此时既不增加长度也不断开，直接跳过
            continue

        elif nums[i] == nums[i - 1] + 1:
            # 情况2：连续元素（当前数比前一个数大1）
            # 当前连续序列长度加1
            current_len += 1

        else:
            # 情况3：不连续（断开了）
            # 更新全局最大值，并重置当前长度为1
            max_len = max(max_len, current_len)
            current_len = 1

    # 循环结束后，最后一次连续序列可能还没更新到max_len中
    # 因此最后再比较一次取最大值
    return max(max_len, current_len)
