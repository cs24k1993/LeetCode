#coding:utf-8
#第1种解法
'''
依次扫描数组，小于目标值就继续，等于大于目标值就返回当前索引值
'''
def searchInsert2(nums,target):
    pos = 0
    for i in range(len(nums)):
        if nums[i] < target:
            pos = i + 1
        else:
            return i
    return pos
print(searchInsert2([6,7,8,9],10))


#第2种解法
'''
用python的index函数
'''
def searchInsert(nums,target):
    if target in nums:
        return nums.index(target)
    else:
        nums.append(target)
        nums = sorted(nums)
        return nums.index(target)
print(searchInsert([1,2,4],3))