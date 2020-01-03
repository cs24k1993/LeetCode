# coding:utf-8
# 第1种解法
'''
根据求和来判断
时间复杂度：O(n)、空间复杂度O(1)
'''
def pivotIndex(nums):
    S = sum(nums)
    leftSum = 0
    for i,x in enumerate(nums):
        if leftSum == S - leftSum - x:
            return i
        leftSum += x
    return -1