def twoSum(nums, target):
    hashmap = {}  # 1. 创建一个空字典，用来存储 {数值: 下标}
    
    # 2. 用enumerate同时获取下标和值
    for i, num in enumerate(nums):
        
        # 3. 计算当前数字需要的“另一半”是多少
        complement = target - num
        
        # 4. 关键步骤：检查“另一半”是否已经在字典里了
        if complement in hashmap:
            # 如果在，说明找到了！返回 [另一半的下标, 当前下标]
            return [hashmap[complement], i]
            
        # 5. 如果没找到搭档，就把当前的数字和下标存入字典，留给后面的人匹配
        hashmap[num] = i
        
    # 6. 如果循环结束还没返回，说明没找到（题目通常保证有解）
    return None
