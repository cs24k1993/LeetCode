# coding:utf-8
# 第1种解法
# 用哈希表
def findPairs(nums, k):
    res = 0
    dct = {}
    for i in nums:
        # 把nums中的元素存入字典中，用字典的get方法
        dct[i] = dct.get(i, 0) + 1
    if k < 0:
        return 0
    elif k == 0:
        # 如果nums有重复元素，要判断多次，用set去重
        for j in set(nums):
            if dct[j] >= 2:
                res += 1
    else:
        # 直接判断i+k是否在字典中统计次数
        for i in dct:
            if i + k in dct:
                res += 1
    return res
print(findPairs([1, 2, 3, 4, 5],1))


# 第2种解法
''''
1.把nums存入字典中
2.对nums进行排序，方便比较大小
3.根据k值、字典中的value值统计次数
'''
def findPairs2(nums,k):
    dct = {}
    for i in nums:
        if i not in dct:
            dct[i] = 1
        else:
            dct[i] += 1
    # print(dct)
    res = 0
    nums.sort()
    if k < 0:
        return 0
    if k == 0:
        for j in nums:
            if dct[j] != 1:
                res += 1
                dct[j] = 1
    else:
        for j in nums:
            # 如果满足条件的数字重复多次，则只算一次
            if dct[j] !=0:
                if j+k in dct:
                    res += 1
            dct[j] = 0
    return res
print(findPairs2([1, 2, 3, 4, 5],-1))
