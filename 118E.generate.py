# coding:utf-8
# 第1种解法
'''
1.初始化结果数组，numRows表示结果数组dp的行数，每一行的元素个数等于所处第几行。全部初始化为0
2.将边界全部初始化为1
3.遍历dp，将为0的位置使用动态规划填入，公式：dp[i][j]=dp[i-1][j-1]+dp[i-1][j]
'''
def generate(numRows):
    dp = [[0] * n for n in range(1, numRows + 1)]
    for i in range(numRows):
        dp[i][0] = dp[i][-1] = 1
    for j in range(numRows):
        for k in range(j + 1):
            if (dp[j][k] == 0):
                dp[j][k] = dp[j-1][k-1] + dp[j-1][k]
    return dp
print(generate(5))