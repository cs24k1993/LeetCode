# coding:utf-8
# 第1种解法
'''
1.哈希表：用字典的key不能重复的性质
遍历数组，如果当前遍历的元素在字典中存在就返回True，不存在则把该元素添加进字典中
如果字典的长度大于k，说明里面全是不重复的key，删除最老的key，用字典来维护这个k大小的滑动窗口
2.复杂度分析：
时间复杂度：O(n)，做n次搜索，删除，插入操作，每次操作都耗费常数时间
空间复杂度：O(min(n,k))，开辟的额外空间取决于散列表中存储的元素的个数，也就是滑动窗口的大小O(min(n,k))
'''
def containsNearbyDuplicate(nums,k):
    dct = {}
    for i in range(len(nums)):
        if nums[i] in dct:
            return True
        dct[nums[i]] = i
        if len(dct) > k:
            del dct[nums[i-k]]
    return False
print(containsNearbyDuplicate([1,2,3,1],2))




