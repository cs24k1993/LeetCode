# coding:utf-8
# 第1种解法
'''
1.把nums中所有元素存储到一维列表temp中
2.利用python切片在temp中截取所需的值
'''
def matrixReshape(nums,r,c):
    a = len(nums)
    b = len(nums[0])
    temp = []
    re_nums = []
    for i in range(a):
        for j in range(b):
            temp.append(nums[i][j])
    if a * b == r * c:
        for i in range(r):
            re_nums.append(temp[c * i:c + c * i])
        return re_nums
    else:
        return nums
print(matrixReshape([[1,2,3],[4,5,6]],3,2))


# 第2种解法
'''
1.熟悉python的生成器
2.yield from后面的参数必须是可迭代对象而yield不需要
'''
def matrixReshape2(nums,r,c):
    if r * c != len(nums) * len(nums[0]):
        return nums
    def gen(nums):
        for i in nums:
            yield from i
    it = gen(nums)
    return [[next(it) for _ in range(c)] for _ in range(r)]
print(matrixReshape2([[1,2,3],[4,5,6]],3,2))
