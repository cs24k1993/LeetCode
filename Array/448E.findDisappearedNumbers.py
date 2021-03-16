# coding:utf-8
# 第1种解法
def findDisappearedNumbers0(nums):
    temp = set(nums)
    res = []
    for i in range(1, len(nums) + 1):
        if i not in temp:
            res.append(i)
    return res

'''
抽屉原理(鸽巢原理) + 基于“异或运算”交换两个变量的值
'''
def findDisappearedNumbers(nums):
    # 基于异或运算交换数组两个位置的元素，不使用额外的空间
    def swap(nums, index1, index2):
        # 这一步是必要的，否则会使得一个数变成 0
        if index1 == index2:
            return
        nums[index1] = nums[index1] ^ nums[index2]
        nums[index2] = nums[index1] ^ nums[index2]
        nums[index1] = nums[index1] ^ nums[index2]
    for i in range(len(nums)):
        # 交换过来的数有很大的可能不在它最终应该呆的位置，因此需要在 for 循环中使用 while
        while nums[i] != nums[nums[i] - 1]:
            # 如果不在位置上，并且它将要去的那个位置上的数不等于自己，则交换
            swap(nums, i, nums[i] - 1)
    return [i + 1 for i, num in enumerate(nums) if num != i + 1]
print(findDisappearedNumbers([2,3,1,2,4,3]))


# 第2种解法
# 和第1种解法原理类似，不同的表述
def findDisappearedNumbers2(nums):
    res = []
    for i in range(len(nums)):
        while(nums[i]!=nums[nums[i]-1]):
            nums[nums[i]-1],nums[i]=nums[i],nums[nums[i]-1]
    for i in range(len(nums)):
        if(nums[i]!=i+1):
            res.append(i+1)
    return res
print(findDisappearedNumbers2([2,3,1,2,4,3]))


# 用set去重，求不同的值
# 第3种解法
def findDisappearedNumbers(nums):
    return list(set(range(1, len(nums)+1)) ^ set(nums))




