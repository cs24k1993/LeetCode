# coding:utf-8
# 第1种解法
# 利用双指针，一个指针是i，另一个指针是循环变量j
def largeGroupPositions(S):
    i = 0
    ans = []
    for j in range(len(S)):
        # 没有报索引错误，因为or中第一个条件成立，不执行下一个
        if j == len(S) -1 or S[j] != S[j+1]:
            # 满足条件就是较大分组
            if j - i + 1 >= 3:
                ans.append([i,j])
            # 移动指针i
            i = j + 1
    return ans


# 第2种解法
# 利用双指针，自己写的，有点麻烦
def largeGroupPositions2(S):
    temp = []
    left = right = 0
    count = 1    # 统计字母出现的次数
    for i in range(1, len(S)):
        # 如果两者相等，count加1，移动右指针
        if S[i] == S[i - 1]:
            count += 1
            right += 1
            if i == len(S) - 1 and count >= 3:
                temp.append([left, right])
        elif count >= 3:
            right = i - 1
            temp.append([left, right])
            left = right = i
            count = 1
        # 如果两者不等，同时移动两个指针，同时把count置1
        else:
            left = right = i
            count = 1
    return temp
