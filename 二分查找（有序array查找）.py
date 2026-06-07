def binary_search(arr, target):
    # 1. 初始化左右指针，分别指向数组的开头和结尾（闭区间）
    left, right = 0, len(arr) - 1

    # 2. 当左指针没有超过右指针时，循环继续
    # (只要区间 [left, right] 有效，就有机会找到目标)
    while left <= right:
        # 3. 计算中间位置的索引 (// 2 表示整除，取整数)
        mid = (left + right) // 2

        # 4. 情况一：中间值刚好是目标值
        if arr[mid] == target:
            return mid  # 直接返回找到的下标

        # 5. 情况二：中间值比目标小
        # 说明目标值在右半边（因为数组是有序的）
        # 所以把左边界移到 mid 的右边
        elif arr[mid] < target:
            left = mid + 1

        # 6. 情况三：中间值比目标大
        # 说明目标值在左半边
        # 所以把右边界移到 mid 的左边
        else:
            right = mid - 1

    # 7. 如果循环结束还没找到，说明目标不存在，返回 -1
    return -1
