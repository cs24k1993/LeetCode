# coding:utf-8
# 第1种解法
'''
1.两个指针i和j，如果前面的元素都不为0，则i和j同时向右移动
2.如果遇到0元素，i继续向右移动，j指针停止移动，此时j指向0元素
3.交换相邻的非0元素和0元素，遍历即可
时间复杂度：O(n)，空间复杂度：O(1)
'''
def moveZeroes(nums):
    i = j = 0
    for i in range(len(nums)):
        if nums[i] != 0:
            nums[i],nums[j] = nums[j],nums[i]
            j += 1
    return nums
print(moveZeroes([2,0,1,3]))


# 第2种解法
# 利用python的生成器
def moveZeroes2(nums):
    def gen(nums):
        for x in nums:
            if x:
                yield x
    # i = 0一定要加上，不然报错？变量要先声明，这里不太懂
    i = 0
    for i,n in enumerate(gen(nums)):
        nums[i] = n
    for j in range(i+1,len(nums)):
        nums[j] = 0
    return nums
print(moveZeroes2([2,0,1,3]))


# 第3种解法
# 用python内置函数remove删除0，并在列表后面添加0
def moveZeroes3(nums):
    for i in range(len(nums)):
        try:
            nums.remove(0)
            nums.append(0)
        except:
            return nums


# 第4种解法
# 用python的sort函数(该函数没有返回值)
def moveZeroes4(nums):
    nums.sort(key=bool, reverse=True)
    return nums