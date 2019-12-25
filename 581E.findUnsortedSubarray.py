# coding:utf-8
# 第1种解法
'''
1.先排序得到一个新列表order_nums
2.用两个指针left和right指向原列表中顺序不对的地方
'''
def findUnsortedSubarray(nums):
    left = 0
    right = len(nums) - 1
    order_nums = sorted(nums)
    # 判断left和right时，不能是 < ，如果原列表已经是有序的，返回值应为0
    # left<=right时继续移动left和right，最后返回值right-left+1就是0
    # 如果用 < ，要讨论原列表是有序列表的情况
    while left <= right and nums[left] == order_nums[left]:
        left += 1
    while left <= right and nums[right] == order_nums[right]:
        right -= 1
    return right - left + 1
print(findUnsortedSubarray([1,2,3,4]))
print(findUnsortedSubarray([2,6,4,8,10,9,15]))
