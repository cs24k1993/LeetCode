# coding:utf-8
# 第1种解法
'''
双指针，链表拼接
1.当 pA 到达链表的尾部时，将它重定位到链表 B 的头结点 (你没看错，就是链表 B)
2.类似的，当 pB 到达链表的尾部时，将它重定位到链表 A 的头结点
3.若在某一时刻 pA 和 pB 相遇，则 pA/pB 为相交结点
A + B - all = B + A - all(all为两链表相交部分的长度)
'''
def getIntersectionNode(headA,headB):
    ha,hb = headA,headB
    # 如果相交，ha为相交的链表节点；如果不想交，ha为None
    while ha != hb:
        # if ha，如果ha.next为None，则从开始遍历链表B
        # 用if ha.next会死循环
        ha = ha.next if ha else headB
        hb = hb.next if hb else headA
    return ha


# 第2种解法
'''
哈希表法：while循环要加上ha = ha.next，刚开始没加，超时了
遍历链表 A 并将每个结点的地址/引用存储在哈希表中。然后检查链表 B 中的每一个结点是否在哈希表中
若在，则有相交结点。不在，返回None
'''
def getIntersectionNodeB(headA,headB):
    hash_set = set()
    ha,hb = headA,headB
    while ha:
        hash_set.add(ha)
        ha = ha.next
    while hb:
        if hb in hash_set:
            return hb
        hb = hb.next
    return None