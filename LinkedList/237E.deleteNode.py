# coding:utf-8
# 第1种解法
'''
这道题没有给出链表的头节点，而是直接给出要删除的节点，让我们进行原地删除
我们对于该节点的前一个节点一无所知，所以无法直接执行删除操作
因此，我们将要删除节点的 next 节点的值赋值给要删除的节点，转而去删除 next 节点，从而达成目的
删除节点有两种： 1.删除当前节点 2.删除后继节点
删除当前节点的方法 1.利用pre 2.利用next
'''
def deleteNode(node):
    node.val = node.next.val
    node.next = node.next.next

