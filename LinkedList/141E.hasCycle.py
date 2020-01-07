# coding:utf-8
# 第1种解法
# 用set判断是否重复（set里面存储的是链表节点，是一个对象）
def hasCycle(head):
    hash_set = set()
    while head:
        if head in hash_set:
            return True
        hash_set.add(head)
        head = head.next
    return False


# 第2种解法
'''
快慢双指针：快指针走两步，慢指针走一步。如果链表有环，fast和slow一定会相遇
如果fast走到了链表尾部，说明链表没有环
'''
def hasCycle2(head):
    fast, slow = head, head
    # and后为什么还有一个判断？不然会报错
    while fast and fast.next:
        fast = fast.next.next
        slow = slow.next
        if fast == slow:
            return True
    return False


