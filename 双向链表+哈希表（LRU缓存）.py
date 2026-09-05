# 要设计一个缓存，有固定容量上限，如果缓存数据结构中储存的超出上限则淘汰最旧使用的数据（key）。
# 核心思路是用双向链表管理缓存的新旧顺序、用哈希表管理键的查找。因为二者的操作时间都是O1

class Node:
    def __init__(self, key = 0, val = 0):
        self.key = key
        self.val = val
        self.prev = None
        self.next = None
        
