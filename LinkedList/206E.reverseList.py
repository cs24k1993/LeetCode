# coding:utf-8
# 第1种解法
'''
解题思路：迭代，新建一个头结点，将所有的原链表节点从头到尾逐一取下
采用头插法插入整个链表到新建节点之前，则完成了链表逆序的目的
'''
def reverseList(head):
    if head == None or head.next == None:
        return head
    pre = None
    cur = head
    temp = None
    while cur:
        temp = cur.next
        cur.next = pre
        pre = cur
        cur = temp
    return pre


# 第2种解法
'''
遍历链表，在遍历的过程中更新两个指针pre, head：
pre, head分别指向前一个节点和当前节点，每次执行head.next = pre
nex用于提前保存下一个节点。
由于需要返回新的链表头部，所以设置跳出条件为head.next == null,跳出后将最后head指向pre，并返回head。
'''
def reverseList2(head):
    if not head: return
    pre = None
    while head.next:
        nex = head.next
        head.next = pre
        pre = head
        head = nex
    head.next = pre
    return head


# 第3种解法
# 递归，还没看懂
def reverseList3(head):
    if not head or not head.next: return head
    new_head = reverseList3(head.next)
    next_node = head.next
    next_node.next = head
    head.next = None
    return new_head
