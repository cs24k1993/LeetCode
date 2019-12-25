# coding:utf-8
# 第1种解法
'''
贪心算法：
如果一个0，前一个位置为0（或者在列表头）且后一个位置也为0（或者在列表尾），
则可以种花，即该元素置1，计数加1。
'''
def canPlaceFlowers(flowerbed, n):
    length = len(flowerbed)
    count = 0
    for i in range(length):
        if flowerbed[i] == 0 and (i == 0 or flowerbed[i-1] == 0) and (i == length-1 or flowerbed[i+1] == 0):
            count += 1
            flowerbed[i] = 1
    return count >= n


# 第2种解法
'''
1.首尾分别插入0，统计0的个数（列表中间两个1之间0的个数大于等于3时才能种花，
但首尾处两个0就能种花，所以在首尾分别插入0，对齐）
2.在两个1区间内根据0的个数判断可以种植的花数
'''
def canPlaceFlowers2(flowerbed, n):
    count = 0
    zeros = 0
    flowerbed.insert(0, 0)
    flowerbed.append(0)
    for i in flowerbed:
        if i == 0:
            zeros += 1
        else:
            # 0的个数 >= 3时才能种花
            if zeros > 2:
                count += (zeros - 1) // 2
            # 如果遇到1，zeros就清零
            zeros = 0
        if count >= n:
            return True
    if zeros > 2:
        count += (zeros - 1) // 2
    return count >= n


# 第3种解法
'''
这个是自己写的，太麻烦，辣眼睛
1.提取为1的索引，组成新的列表
2.分别讨论index1为0、1时的情况
3.当有两个1以上时，根据1索引的差值得出两个1之间可以种植花的数目
4.列表两边的1要分别讨论
'''
def canPlaceFlowers3(flowerbed,n):
    count = 0
    index1 = []
    for i in range(len(flowerbed)):
        if flowerbed[i] == 1:
            index1.append(i)
    if len(index1) == 0:
        # 列表全是0，根据0的个数判断能种多少花
        return n <= ((len(flowerbed) - 1) // 2 + 1)
    if len(index1) == 1:
        # 列表只有一个1，列表头、尾同时考虑
        return n <= ((index1[0] - 0) // 2 + (len(flowerbed) - 1 - index1[0]) // 2)
    for j in range(len(index1) - 1):
        # 索引差值 >= 4 时，中间才能种花（比如1001，1的索引差为3，两个1中间不能种花）
        if index1[j + 1] - index1[j] >= 4:
            count += (index1[j + 1] - index1[j] - 2) // 2
    return n <= ((index1[0] - 0) // 2 + count + (len(flowerbed) - 1 - index1[-1]) // 2)

