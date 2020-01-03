# coding:utf-8
# 第1种解法
# 排序，然后判断，最后用index返回最大值的索引
def dominantIndex(nums):
    if len(nums) == 0:
        return -1
    if len(nums) == 1:
        return 0
    nums2 = sorted(nums)
    if nums2[-1] >= 2*nums2[-2]:
        return nums.index(nums2[-1])
    return -1
print(dominantIndex([3,6,1,0]))


# 第2种解法
def dominantIndex2(nums):
    max_index = nums.index(max(nums))
    nums.sort()
    if len(nums) == 1:
        return 0
    if nums[-1] >= 2*nums[-2]:
        return max_index
    return -1
print(dominantIndex2([3,6,1,0]))