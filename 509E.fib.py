# coding:utf-8
'''
求斐波那契数列第N项的值
1.利用一个数组temp，随着N的增加，temp[0]和temp[1]也随之变化，两者之和可以得出下一项的值。
2.根据N%2判断输出的是temp[0]还是temp[1]
'''
def fib(N):
    temp = [0,1]
    if N >= 2:
        for i in range(2,N+1):
            temp[i%2] = temp[0] + temp[1]
    return temp[N%2]
print(fib(5))


'''
青蛙跳台阶问题：一只青蛙一次可以跳上1级台阶，也可以跳上2级。
求该青蛙跳上一个n级的台阶总共有多少种跳法。
该问题可以转换为斐波那契数列，某个台阶数的跳法等于上上个台阶数跳法(再跳2个台阶可达)+
上个台阶数的跳法(再跳1个台阶可达)
'''
def jumpFloor(n):
    temp=[1,2]
    if n >= 3:
        for i in range(3,n+1):
            temp[(i+1)%2] = temp[0] + temp[1]
    return temp[(n+1)%2]
print(jumpFloor(6))


