# coding:utf-8
# 第1种解法
# 用set操作去重，然后移除两次最大值即得第三大的值
def thirdMax(nums):
    set_nums = set(nums)
    if len(set_nums) < 3:
        return max(set_nums)
    set_nums.remove(max(set_nums))
    set_nums.remove(max(set_nums))
    return max(set_nums)
print(thirdMax([2,0,1,1,3]))


# 第2种解法
'''
维护一个长度为3的set，遍历列表后，如果tmp长度小于3则返回最大值，
否则返回set中的最小值，即第三大的值
'''
def thirdMax2(nums):
    tmp = set()
    for n in nums:
        tmp.add(n)
        if len(tmp) > 3:
            tmp.remove(min(tmp))
    if len(tmp) < 3:
        return max(tmp)
    return min(tmp)
print(thirdMax2([2,0,1,1,3]))
