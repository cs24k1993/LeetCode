# coding:utf-8
# 第1种解法
'''
遍历链表，判断当前节点和下一节点的val，如果一致则将当前节点的next指向next.next
注意链表是空的情况。
'''
def deleteDuplicates(head):
    if head is None:
        return head

    pHead = head
    while head.next != None:
        if head.val == head.next.val:
            head.next = head.next.next
        else:
            head = head.next

    return pHead

