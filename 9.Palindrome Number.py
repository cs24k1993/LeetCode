#coding:utf-8
def isPalindrome(num):
    # return int(str(abs(x))[::-1]) == x

    if x < 0:
        return False
    str_1 = str(abs(x))
    str_2 = str_1[::-1]
    if str_1 == str_2:
        return True
    else:
        return False

print(isPalindrome(121)