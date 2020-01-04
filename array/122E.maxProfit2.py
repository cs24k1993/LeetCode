# coding:utf-8
'''
贪心算法，可以在同一天买入和卖出，因此只要当天票价比昨天的高就可以卖出
'''
# 第1种解法
def maxProfit(prices):
    sum = 0
    for i in range(len(prices) - 1):
        profit = prices[i+1] - prices[i]
        if profit > 0:
            sum += profit
    return sum
print(maxProfit([7,1,5,3,6,4]))


# 第2种解法
def maxProfit2(prices):
    return sum(b - a for a, b in zip(prices, prices[1:]) if b > a)
print(maxProfit2([7,1,5,3,6,4]))

# 分解
def maxProfit3(prices):
    sum2=0
    for a, b in zip(prices, prices[1:]):
        if b > a:
            sum2 += b-a
    return sum2
print(maxProfit2([7,1,5,3,6,4]))