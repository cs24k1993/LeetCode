# coding:utf-8
# 第1种解法
'''
把数组中的值当做字典的key，索引当做value，遍历的同时把key，value存入字典，进行查找
'''
def twoSum(nums,target):
    dct = {}
    for i in range(len(nums)):
        if target-nums[i] in dct:
            return [dct[target-nums[i]]+1,i+1]
        dct[nums[i]] = i
    # 列表中不存在两元素之和为target时返回0
    return 0
print(twoSum([1,2,3,4,6],9))