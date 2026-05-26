# 核心思路是：固定一个数，将剩下的问题转化为“两数之和”。通过先排序，再利用双指针，将时间复杂度控制在 O(n²)

from typing import List

def three_sum_optimized(nums: List[int]) -> List[List[int]]:
    # 1. 排序：这是双指针法的前提，能让相同的数相邻，方便去重
    nums.sort()
    res: List[List[int]] = []
    n = len(nums)

    # 2. 遍历第一个数 nums[i]
    # 只需要遍历到倒数第三个数，因为后面还要留两个位置给 left 和 right
    for i in range(n - 2):
        # 剪枝优化：因为数组已排序，如果第一个数都大于0，三数之和不可能为0
        if nums[i] > 0:
            break

        # 去重逻辑1：如果当前的数和前一个数一样，跳过，避免结果重复
        if i > 0 and nums[i] == nums[i - 1]:
            continue

        # 3. 双指针初始化：left 指向 i 后面，right 指向数组末尾
        left, right = i + 1, n - 1

        while left < right:
            s = nums[i] + nums[left] + nums[right]

            if s < 0:
                # 和太小，需要变大 -> 左指针右移
                left += 1
            elif s > 0:
                # 和太大，需要变小 -> 右指针左移
                right -= 1
            else:
                # 找到了一组解
                res.append([nums[i], nums[left], nums[right]])

                # 去重逻辑2：找到解后，继续移动指针并跳过相同的数
                # 这里利用了排序后相同元素相邻的特性
                left += 1
                right -= 1

                # 只要左指针当前的数和刚才用过的数一样，就一直右移
                while left < right and nums[left] == nums[left - 1]:
                    left += 1

                # 只要右指针当前的数和刚才用过的数一样，就一直左移
                while left < right and nums[right] == nums[right + 1]:
                    right -= 1

    return res
