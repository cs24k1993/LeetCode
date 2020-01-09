# coding:utf-8
# 第1种解法
# 快慢指针 + 反转链表
def isPalindrome(head):
    fast = slow = head
    # 快慢指针，快指针到达尾部，慢指针到达中间
    while fast and fast.next:
        fast = fast.next.next
        slow = slow.next
    # 奇数长，fast指针在最后一个，slow在最中间，slow需要往后过一个
    # 偶数长，fast为空，slow指针中点过一个
    if fast:
        slow = slow.next
    # 反转链表
    pre = None
    cur = slow
    while cur:
        tmp = cur.next
        cur.next = pre
        pre, cur = cur, tmp
    # 比较值是否相等
    while pre and head:
        if pre.val != head.val:
            return False
        # 不要忘了加这个条件
        pre = pre.next
        head = head.next
    return True


# 第2种解法
# 借用列表，比较值的大小
def isPalindrome2(head):
    tmp = []
    while head:
        tmp.append(head.val)
        head = head.next
    l = 0
    r = len(tmp) - 1
    while l < r:
        if tmp[l] != tmp[r]:
            return False
        l += 1
        r -= 1
    return True
