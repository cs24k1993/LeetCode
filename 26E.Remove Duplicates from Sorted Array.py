#coding:utf-8
#第1种解法
def removeDuplicates(nums):
    # 利用set没有重复key的性质去重，再转换成list
    nums[:] = list(set(nums))
    # 不用排序也可以吧？反正题目只是要求返回数组长度，并不要求排序
    nums.sort()
    return len(nums)
print(removeDuplicates([1,2,3,3,4]))

#第2种解法
def removeDuplicates2(nums):
    length = 0
    # 要考虑空数组的情况
    if len(nums) == 0:
        return length
    # 每遇到一个不重复的数字，length就加1，并把不重复的数字赋值给nums[length]
    for i in range(len(nums)):
        if nums[length] < nums[i]:
            length += 1
            nums[length]=nums[i]
    return length+1
print(removeDuplicates2([1,1,2,2,2,3,4,5,5]))