# coding:utf-8
# 第1种解法
'''
定义哨兵节点pre，哨兵节点广泛应用于树和链表中，如伪头、伪尾、标记等，它们是纯功能的
通常不保存任何数据，其主要目的是使链表标准化，如使链表永不为空、永不无头、简化插入和删除
在这里哨兵节点将被用于伪头
'''
def removeElements(head,val):
    p = ListNode(0)
    p.next = head

    pre,cur = p,head
    while cur:
        if cur.val == val:
            pre.next = cur.next
        else:
            # 如果不等，移动pre和cur指针，继续遍历链表
            pre = cur
        cur = cur.next

    return p.next


