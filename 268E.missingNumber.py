# coding:utf-8
# 第1种解法
# 用数列的通项公式求和再减去列表元素之和，即为所求
def missingNumber(nums):
    n = len(nums) + 1
    return n * (n - 1) // 2 - sum(nums)


# 第2种解法
# 哈希表 dict和set 比 list查找速度要快很多
def missingNumber2(nums):
    dct = set(nums)
    for i in range(len(nums)):
        if i not in dct:
            return i
    return len(nums)
print(missingNumber2([0,2,3,1]))


# 第3种解法
# 位运算，异或方式，相同的元素异或后,一定是0
def missingNumber4(nums):
    miss = len(nums)
    for index, data in enumerate(nums):
        miss = miss ^ index ^ data
    return miss
print(missingNumber4([0,2,3,1]))


# 第4种解法
'''
利用set的异或运算，异或结果为两个集合中不同的元素，相同的元素则删除
由于set不可直接用索引，所以先转换成list，再取出所求的值
'''
def missingNumber4(nums):
    return list(set(nums)^set(list(range(len(nums)+1))))[0]


# 第5种解法
# 先排序，再把nums中的值和索引比较
def missingNumber5(nums):
    nums.sort()
    for i in range(len(nums)):
        if nums[i] != i:
            return i
    return len(nums)
print(missingNumber5([0,2,3,1]))