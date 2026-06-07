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


# 进阶解法是，哈希集合：首先全部存入哈希集合，然后找序列起点（若数字减一不在集合中，判断为序列起点），然后从序列起点开始数连续数字，记录序列长度

def longestConsecutive(nums):
    """
    找出未排序数组中最长连续序列的长度。
    例如：[100, 4, 200, 1, 3, 2] -> 最长连续序列 [1,2,3,4] -> 返回 4
    
    算法核心思想：
    1. 用哈希集合（set）实现 O(1) 的查找
    2. 只从每个连续序列的“起点”开始计数，避免重复统计
    3. 如何判断起点？如果 num-1 不在集合中，说明 num 是一个序列的开头
    """
    
    # 将数组转换为哈希集合，去除重复元素，实现 O(1) 的成员检查
    num_set = set(nums)
    
    # 记录最长连续序列的长度
    max_len = 0
    
    # 遍历集合中的每个数字（注意：遍历 set 而不是原数组，避免重复处理相同值）
    for num in num_set:
        
        # 关键判断：只有当前数字的前一个数 num-1 不存在于集合中时
        # 才说明 num 是一个连续序列的起点（最小值）
        if num - 1 not in num_set:
            
            # 初始化当前序列的开始数字和长度
            current = num      # 当前连续序列已到达的数字
            length = 1         # 当前序列长度（至少包含 num 自己）
            
            # 从起点开始，不断检查下一个数字 current+1 是否在集合中
            while current + 1 in num_set:
                current += 1   # 移动到下一个连续数字
                length += 1    # 序列长度增加
            
            # 更新全局最长长度
            max_len = max(max_len, length)
    
    return max_len
