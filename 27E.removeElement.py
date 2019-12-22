#coding:utf-8
#第1种解法
'''
pop操作会删除一个元素后，把后面的元素自动前移，
倒序的话，把删去的窟窿以后的元素往前移，对前面没有遍历过的元素不会有影响
'''
def removeElement(nums,val):
    for i in range(len(nums) - 1, -1, -1):
        if nums[i] == val:
            nums.pop(i)
    return len(nums)
print(removeElement([1,2,2,3,4],2))


#第2种解法
'''
了解remove函数
in判断在不在
'''
def removeElement2(nums,val):
    while True:
        if val in nums:
            nums.remove(val)
        else:
            break
    return len(nums)
print(removeElement2([1,2,2,3,4,2,3],2))


#第3种解法
'''
利用双指针，值为val的就放到数组右边
'''
def removeElement3(nums,val):
    left = 0
    right = len(nums)-1
    while left < right:
        if nums[left] == val and nums[right] != val:
            nums[left],nums[right] = nums[right],nums[left]
            left += 1
            right -= 1
        elif nums[right] == val:
            right -= 1
        elif nums[left] != val:
            left += 1
    length = 0
    for i in range(len(nums)):
        if nums[i] != val:
            length += 1
        else:
            return length
print(removeElement3([1,2,2,3,4,2,3],2))