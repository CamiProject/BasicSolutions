# 普通递归，求第n项，直接递归

def fib(n):
    # 1. 终止条件：第 1 项和第 2 项的值都是 1
    if n == 1 or n == 2:
        return 1
    # 2. 递归拆解：当前项 = 前一项 + 前两项
    return fib(n - 1) + fib(n - 2)

print(fib(6))  # 输出：8

# 优化思路：“记忆化递归”。

def fib(n, memo={}):
    # 1. 查表：如果之前已经算过 n 的结果，直接返回，不再重复计算
    if n in memo:
        return memo[n]
    
    # 2. 终止条件：如果 n 是 0 或 1，直接返回 n（fib(0)=0, fib(1)=1）
    if n <= 1:
        return n
    
    # 3. 递归计算：如果没有算过，才进行递归调用
    # 并将计算结果存入 memo 字典中，以便下次使用
    memo[n] = fib(n - 1, memo) + fib(n - 2, memo)
    
    # 4. 返回结果
    return memo[n]
