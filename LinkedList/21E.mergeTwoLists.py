# coding:utf-8
# 第1种解法
# 递归：两个链表头部较小的一个与剩下元素的merge操作结果合并
def mergeTwoLists(l1,l2):
    if l1 is None:
        return l2
    elif l2 is None:
        return l1
    elif l1.val < l2.val:
        l1.next = mergeTwoLists(l1.next,l2)
        return l1
    else:
        l2.next = mergeTwoLists(l1,l2.next)
        return l2


# 第2种解法
'''
和第1种解法类似，只是简写了
在 Python 中，and 和 or 都有提前截至运算的功能。
and：如果 and 前面的表达式已经为 False，那么 and 之后的表达式将被 跳过，返回左表达式结果
or：如果 or 前面的表达式已经为 True，那么 or 之后的表达式将被跳过，直接返回左表达式的结果
'''
def mergeTwoLists2(l1, l2):
    if l1 and l2:
        if l1.val > l2.val: l1, l2 = l2, l1
        l1.next = mergeTwoLists2(l1.next, l2)
    return l1 or l2


# 第3种解法
# 迭代
def mergeTwoLists3(l1, l2):
    # 定义一个哑节点
    prehead = ListNode(-1)
    prev = prehead
    # 直到l1或者l2其中一个为空
    while l1 and l2:
        if l1.val <= l2.val:
            prev.next = l1
            l1 = l1.next
        else:
            prev.next = l2
            l2 = l2.next
        prev = prev.next
    # 把另一个非空的有序的链表，拼接到合并链表的后面
    prev.next = l1 if l1 is not None else l2
    return prehead.next