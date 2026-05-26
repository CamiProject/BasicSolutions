# 核心思路利用栈的结构

def isValid(s: str) -> bool:
    # 初始化一个空栈，用于存储尚未匹配的左括号
    stack = []
    # 定义一个哈希映射，键为右括号，值为对应的左括号，方便快速查找匹配
    mapping = {')': '(', ']': '[', '}': '{'}

    # 遍历输入字符串中的每一个字符
    for ch in s:
        # 1. 如果不是右括号（即是左括号），直接入栈
        if ch not in mapping:
            stack.append(ch)
        
        # 2. 如果是右括号，进行匹配检查
        else:
            # 栈空 或 栈顶不是对应的左括号 -> 失败
            if not stack or stack[-1] != mapping[ch]:
                return False
            stack.pop() # 匹配成功，弹出

    # 遍历结束后，如果栈为空，说明所有左括号都找到了对应的右括号，返回 True
    # 如果栈不为空，说明还有未闭合的左括号，返回 False
    return len(stack) == 0
