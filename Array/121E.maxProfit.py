# coding:utf-8
# 第1种解法
'''
1.用min_price保存列表中的最小值并根据此最小值计算当前的最大收益
2.比较收益的最大值
'''
def maxProfit(prices):
    min_price = float('inf') #正无穷大，prices[0]也可以？在线提交会报错
    max_profit = 0
    for i in range(len(prices)):
        min_price = min(prices[i], min_price)
        max_profit = max(max_profit, prices[i]-min_price)
    return max_profit
print(maxProfit([7,1,5,3,6,4]))


'''
其实两种都算是动态规划，都是记录之前的值，来更新当前的值。
第一种更好理解，记录最低值，不断更新最大高度差。
第二种则是经典的动态规划思路，套用经典的求最大连续子数组和就行？
'''
# 第2种解法
def maxProfit2(prices):
    temp = 0
    max_profit = 0
    for i in range(len(prices)-1):
        temp = max(0, prices[i+1]-prices[i]+temp)
        max_profit = max(max_profit, temp)
    return max_profit
