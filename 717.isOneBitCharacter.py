# coding:utf-8
# 第1种解法
'''
线性扫描：对bits数组从左到右扫描来判断最后一位是否为一比特字符。当扫描到第 i位时，
如果bits[i]=1，那么说明这是一个两比特字符，将 i的值增加 2。
如果bits[i]=0，那么说明这是一个一比特字符，将 i的值增加 1。
如果 i最终落在了 bits.length−1 的位置，那么说明最后一位一定是一比特字符。
时间复杂度：O(n)、空间复杂度O(1)
'''
def isOneBitCharacter(bits):
    i = 0
    while i < len(bits)-1:
        i += bits[i] + 1
    return i == len(bits) - 1


# 第2种解法
'''
三种字符分别为0,10,11，那么bits 数组中出现的所有 0 都表示一个字符的结束位置（无论其为一比特还是两比特）。
因此最后一位是否为一比特字符，只和他左侧出现的连续的 1 的个数（即它与倒数第二个 0 出现的位置之间的 1 的个数，
如果 bits 数组中只有 1 个 0，那么就是整个数组的长度减一）有关。如果 1 的个数为偶数个，
那么最后一位是一比特字符，如果 1 的个数为奇数个，那么最后一位不是一比特字符。
'''
def isOneBitCharacter2(bits):
    parity = bits.pop()
    while bits and bits.pop(): parity ^= 1
    return parity == 0
print(isOneBitCharacter2([1,1,1,0]))