# coding:utf-8
# 第1种解法
# 就是排序，求奇数位的和
def arrayPairSum(nums):
    nums.sort()
    return sum(nums[::2])


