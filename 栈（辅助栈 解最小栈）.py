# 要在 o1 的时间复杂度弹出最小栈，不能用遍历法，核心思路是 用第二个栈 辅助栈：
# 主栈正常存数据，辅助栈 同步记录每一步的最小值
# push时候 辅助栈压入 当前值和栈顶的较小者。getMin时 直接读辅助栈的栈顶。
# 辅助栈 的每一层，都记住了 当时 的最小值，这样确保了不会混乱。

class MinStack:
    def __init__(self):
        self.stack = []
        self.min_stack = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        cur_min = val
        if self.min_stack:
            cur_min = min(val, self.min_stack[-1])
        self.min_stack.append(cur_min)

    def pop(self) -> None:
        self.stack.pop()
        self.min_stack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.min_stack[-1]
