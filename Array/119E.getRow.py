# coding:utf-8
# 第1种解法
'''
第j行的数据, 应该由第j-1行的数据计算出来
假设第j-1行为[1,3,3,1], 那么我们前面插入一个0(j行的数据会比j-1行多一个)
然后执行相加[0+1,1+3,3+3,3+1,1] = [1,4,6,4,1], 最后一个1保留即可
1.第一个for循环是为了得到rowIndex之前行，每一行的值。知道前一行的值才能推出下一行的值
2.插入0，执行第二个for循环，由rowIndex-1行的值递推得到rowIndex行的值
3.第二个for循环了i次，而i行有i+1个数，所以每次都把最后一个1挤到列表最后面
'''
def getRow(rowIndex):
    r = [1]
    for i in range(1, rowIndex + 1):
        r.insert(0, 0)
        # 因为i行的数据长度为i+1, 所以j+1不会越界, 并且最后一个1不会被修改.
        for j in range(i):
            r[j] = r[j] + r[j + 1]
    return r
print(getRow(1))
