# 解题思路是利用3个指针：
# list1指针、list2指针、和curr指针

# 定义链表节点类
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val      # 节点存储的值
        self.next = next    # 指向下一个节点的指针

# 合并两个有序链表（升序）
def mergeTwoLists(list1, list2):
    # 创建一个哑节点（dummy node），值为 -1，方便处理边界情况
    dummy = ListNode(-1)
    # current 指针指向当前已合并链表的末尾
    current = dummy

    # 当两个链表都不为空时，比较当前节点的值
    while list1 and list2:
        if list1.val < list2.val:
            # 将 list1 的当前节点接到 merged 链表末尾
            current.next = list1
            # list1 指针后移
            list1 = list1.next
        else:
            # 将 list2 的当前节点接到 merged 链表末尾
            current.next = list2
            # list2 指针后移
            list2 = list2.next
        # current 指针后移，指向新加入的节点
        current = current.next

    # 当一个链表为空时，将另一个链表的剩余部分直接接在后面
    # list1 or list2 返回非空的那个链表
    current.next = list1 or list2

    # 返回哑节点的下一个节点，即真正合并后链表的头节点
    return dummy.next
