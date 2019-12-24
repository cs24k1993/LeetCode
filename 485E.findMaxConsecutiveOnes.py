# coding:utf-8
# 第1种解法
# 遍历一次就可以，如果num不为0，就把cnt清零，继续下一轮寻找
def findMaxConsecutiveOnes(nums):
    cnt = 0
    res = 0
    for num in nums:
        if num == 1:
            cnt += 1
            res = max(res, cnt)
        else:
            cnt = 0
    return res
print(findMaxConsecutiveOnes([1,1,1,1,0,0,0,1,0,1,0,1]))


# 第2种解法
# 熟悉python map/reduce、join和split的用法
def findMaxConsecutiveOnes2(nums):
    return max(map(len, ''.join(map(str, nums)).split('0')))
    # return max(len (substr) for substr in ''.join([str(x) for x in nums]).split("0"))
print(findMaxConsecutiveOnes2([1,1,1,1,0,0,0,1,0,1,0,1]))

