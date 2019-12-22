#coding:utf-8
'''
https://leetcode.com/problems/maximum-subarray/discuss/20396/Easy-Python-Way
属于动态规划问题。该算法把一些子数组的和存到了原数组中的若干个位置，最后的return max(nums)就是返回最大的那个。
如果以i结尾的子数组的和是 ms(i)，而最大的那个，理所当然就是ms(i) = ms(i-1) + nums[i]推导出来的，
即我们要的结果，最大子数组的和。
'''
def maxSubArray(nums):
    for i in range(1, len(nums)):
        # nums[i - 1]存储的是i之前的元素和的最大值
        if nums[i - 1] > 0:
            nums[i] += nums[i - 1]
    return max(nums)

print(maxSubArray([1,-2,4,-3,10]))