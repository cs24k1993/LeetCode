# coding:utf-8
# 第1种解法
# 快慢指针，是第234题的一部分
def middleNode(head):
    slow = fast = head
    while fast and fast.next:
        fast = fast.next.next
        slow = slow.next
    return slow
