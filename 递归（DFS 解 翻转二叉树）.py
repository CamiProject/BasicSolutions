# 目标是反转一颗二叉树，包括每个子节点
# 核心思路是：递归解法，深度优先DFS
# 关键在于掌握递归思想即可（二叉树、链表、图 都是递归数据结构）

class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        if not root:
            return None
        temp = root.left
        root.left = root.right
        root.right = temp
        
        self.invertTree(root.left)
        self.invertTree(root.right)
        return root
