# coding:utf-8
# 第1种解法
'''
动态规划：计算花费f[i]的递归关系：f[i] = cost[i]+min(f[i+1],f[i+2])
1.当我们要计算f[i]时，要先计算出f[i+1]和f[i+2]，所以我们从后往前计算f
2.在第i步，让f1,f2为f[i+1]，f[i+2]的旧值，并将其更新为f[i],f[i+1]的新值
3.当我们从后遍历i时，我们会保持这些更新。最后答案是min(f1,f2)
'''
def minCostClimbingStairs(cost):
    f1 = f2 = 0
    for x in reversed(cost):
        f1, f2 = x + min(f1, f2), f1
    return min(f1, f2)

print(minCostClimbingStairs([10,15,20]))

a, b = 1, 2
print(a, b)