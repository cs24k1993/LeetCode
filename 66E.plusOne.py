#coding:utf-8
# 第1种解法
# 把列表转换为整数再加1，然后把列表转为str类型，利用str的迭代，转换为列表
def plusOne(digits):
    sums = 0
    for i in digits:
        sums = sums * 10 + i #10进制乘以10，进行累和；
    sums_str = str(sums + 1)
    return [int(j) for j in sums_str]
print(plusOne([4,5,9]))


# 第2种解法
'''
1.熟悉python''.join()函数的用法
2.由于要加1，所以需先转换为整数才能加1
'''
def plusOne2(digits):
    return [int(j) for j in str(int(''.join(str(i) for i in digits)) + 1)]
print(plusOne2([1,2,3]))


