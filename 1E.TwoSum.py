# coding:utf-8
# 第1种解法
# 用两个for循环，算法复杂度过高
def twoSum(nums,target):
    for i in range(len(nums)-1):
        for j in range(i+1,len(nums)):
            if nums[j] == target-nums[i]:
                return [i,j]
print(twoSum([1,2,3,4,5],9))


# 第2种解法
'''
1.要了解python中enumerate函数的用法
2.熟悉python的字典
3.把数组中的值当做字典的key，索引当做value，遍历的同时把key，value存入字典，进行查找
'''
def twoSum2(nums,target):
    dct={}
    for i,n in enumerate(nums):
        if target-n in dct:
            return [dct[target-n],i]
        # 这句不能放在if语句之前，解决list中有重复值或target-num=num的情况
        dct[n]=i
print(twoSum2([1,2,3,4,5],9))