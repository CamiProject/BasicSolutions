# 核心思路是：利用最小堆始终维护每个链表的当前最小节点，每次取出全局最小值。

def mergeKLists(lists):
    dummy = ListNode(0)  # 创建一个值为0 的链表节点，指针为空的 前驱节点
    curr = dummy          # 当前指针，用于构建结果链表
    heap = []             # 最小堆，存储 (节点值, 链表索引, 节点)
    # 将每个链表的头节点入堆
    for i, node in enumerate(lists):
        if node:
            heapq.heappush(heap, (node.val, i, node))
