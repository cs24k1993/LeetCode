# coding:utf-8
# 第1种解法
# 依次扫描数组，小于目标值就继续，等于大于目标值就返回当前索引值
def searchInsert2(nums,target):
    pos = 0
    for i in range(len(nums)):
        if nums[i] < target:
            pos = i + 1
        else:
            return i
    return pos
print(searchInsert2([6,7,8,9],10))


# 第2种解法
# 用python的index函数
def searchInsert(nums,target):
    if target in nums:
        return nums.index(target)
    else:
        nums.append(target)
        nums = sorted(nums)
        return nums.index(target)
print(searchInsert([1,2,4],3))

# 第3种解法
# 因为是排序不重复数组，所以本题实质是二分查找
def searchInsert3(self, nums: List[int], target: int) -> int:
    if (not nums):
        return 0
    n = len(nums)
    l = 0
    r = n - 1
    res = -1
    while (l <= r):
        mid = (l + r) // 2
        if (nums[mid] == target):
            return mid
        elif (nums[mid] > target):
            r = mid - 1
        else:
            l = mid + 1
    res = l
    return res
print(searchInsert3([6,7,8,9],10))
