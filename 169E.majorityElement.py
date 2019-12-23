# coding:utf-8
# 第1种解法
'''
摩尔投票法：当一个数的重复次数超过数组长度的一半，
每次将两个不相同的数删除，最终剩下的就是要找的数。
'''
def majorityElement(nums):
    res = 0
    count = 0
    for i in range(len(nums)):
        # count为0，就把nums中新的元素赋值给res，重新计数
        if count == 0:
            res = nums[i]
        if nums[i] == res:
            count += 1
        else:
            count -= 1
    if count>0:
        return res
print(majorityElement([2,3,3,3,3,2]))


# 第2种解法
'''
把列表中的元素存入字典key中，并用value记录元素出现的次数，
如果次数大于n，返回该元素
'''
def majorityElement2(nums):
    dct = {}
    n = len(nums) // 2
    if len(nums) == 1:
        return nums[0]
    for i in range(len(nums)):
        if nums[i] not in dct:
            dct[nums[i]] = 1
        else:
            dct[nums[i]] += 1
            if dct[nums[i]] > n:
                return nums[i]
print(majorityElement2([2,2,1,1,1,2,2]))


# 第3种解法
# 排序，列表中间的元素就是多数元素
def majorityElement3(nums):
    nums.sort()
    return nums[len(nums) // 2]
print(majorityElement3([2,3,3,3,3,2]))