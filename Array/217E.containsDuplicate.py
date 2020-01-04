# coding:utf-8
# 第1种解法
def containsDuplicate(nums):
    dct = {}
    for i in range(len(nums)):
        if nums[i] in dct:
            return True
        dct[nums[i]] = 1
    return False
print(containsDuplicate([1,2,3,4]))


# 第2种解法
# 比较长度，利用set可以去重的性质
def containsDuplicate2(nums):
    return len(nums) != len(set(nums))
print(containsDuplicate2([1, 2, 3, 1]))


# 第3种解法
# 排序后比较相邻元素是否相等（另一种方法：用两个for循环，比较相邻元素是否相等）
def containsDuplicate3(nums):
    n=len(nums)
    if(n==0 or n==1):
        return False
    nums.sort()
    for i in range(1,n):
        if(nums[i]==nums[i-1]):
            return True
    return False
print(containsDuplicate3([1, 2, 3, 1]))


