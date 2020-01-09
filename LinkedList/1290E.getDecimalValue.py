# coding:utf-8
# 第1种解法
def getDecimalValue(head):
    ans = 0
    cur = head
    while cur:
        # 也可以用移位来替代，移位要加括号，注意优先级
        # ans = (ans << 1) + cur.val
        ans = ans * 2 + cur.val
        cur = cur.next
    return ans


# 第2种解法
# 自己写的，有点复杂
def getDecimalValue2(head):
    count = 0
    cur1 = head
    while cur1:
        count += 1
        cur1 = cur1.next
    num = 0
    cur = head
    while cur:
        num += cur.val * pow(2, count - 1)
        cur = cur.next
        count -= 1
    return num
