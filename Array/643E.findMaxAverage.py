# coding:utf-8
# 第1种解法
'''
滑窗法：列表长度为1时要单独讨论
用a[]存储连续k个值的和，大小为k的窗口从左到右扫描得出最大和
'''
def findMaxAverage(nums,k):
    if k == len(nums):
        return sum(nums)/k
    a = [-float('inf')]*len(nums)
    a[0] = sum(nums[:k])
    for i in range(1,len(nums)-k+1):
        a[i] = a[i-1]-nums[i-1]+nums[i+k-1]
    return max(a)/k
print(findMaxAverage([1,12,-5,-6,50,3],4


# 第2种解法
# 自己写的，超时了
def findMaxAverage2(nums,k):
    maxAve = -float('inf')
    for i in range(len(nums) - k + 1):
        maxAve = max(maxAve, sum(nums[i:i + k]) / k)
    return maxAve
print(findMaxAverage2([1,12,-5,-6,50,3],4))
