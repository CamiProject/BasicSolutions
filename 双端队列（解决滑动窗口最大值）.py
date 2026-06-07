# 滑动窗口最大值
## 核心思路
### 希望队列的头部（dq[0]）始终存储当前窗口中最大值的索引。维护一个双端队列保持单调递减。队列中存储的是数组元素的索引。队列中的索引对应的数值是 从大到小 排列的。

from collections import deque

def maxSlidingWindow(nums, k):
    if not nums or k == 0:
        return []
    
    dq = deque() # 双端队列存储索引，维持单调递减
    res = []
    
    for i, num in enumerate(nums):
        # 移除队尾所有小于等于当前值的元素
        while dq and nums[dq[-1]] <= num:
            dq.pop()
        
        dq.append(i)
        
        # 移除窗口左边界外的队头元素
        if dq[0] <= i - k:
            dq.popleft()
        
        # 窗口形成后，队头即为当前窗口最大值
        if i >= k - 1:
            res.append(nums[dq[0]])
            
    return res
