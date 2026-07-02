# 寻找 “买卖股票的最佳时机”  目标是：给定一个数组 prices（单日股价）的情况下，计算出你只进行一次买入和一次卖出所能获得的最大利润。
# 核心思路是：维护两个变量，只通过一次遍历实现，类似贪心算法
# 到目前为止遇到的最低价格，买入点 (buy) 、 到目前为止能获得的最大利润 (profit)

def maxProfit(price):
    buy = float('inf')
    profit = 0
    
    for sell in price:
        if sell < buy:
            buy = sell
        elif sell - buy > profit:
            profit = sell -buy
    return profit
