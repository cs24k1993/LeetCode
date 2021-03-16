# coding:utf-8
# 第1种解法
def romanToint(s):
    res = 0
    a = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    for i in range(len(s)):
        if i < len(s)-1 and a[s[i]] < a[s[i+1]]:
            res -= a[s[i]]
        else:
            res += a[s[i]]
    return res

print(romanToint('MDIX'))