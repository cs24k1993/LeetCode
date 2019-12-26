# coding:utf-8
# 第1种解法
# 滑动窗口，得出各个连续递增序列的长度，取其中的最大值
def findLengthOfLCIS(nums):
    res = count = 1
    if len(nums) == 0:
        return 0
    for i in range(len(nums) - 1):
        if nums[i] < nums[i + 1]:
            count += 1
            res = max(res, count)
        else:
            count = 1
    return res
print(findLengthOfLCIS([1,3,5,4,7]))

