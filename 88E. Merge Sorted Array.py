# coding:utf-8
#第1种解法
#利用切片，把nums2插入nums1后面，再排序。哈哈哈，有点魔鬼
def merge(nums1,m,nums2,n):
    nums1[m:]=nums2[:]
    nums1.sort()
    return nums1
print(merge([1,2,3],3,[2,5,6],3))


#第2种解法
# nums1中的[0,0,0]是为了给nums2中元素留位置
def merge2(nums1,m,nums2,n):
    i = m - 1
    j = n - 1
    # 从后向前归并，比较 nums1 和 nums2 末尾的元素哪个大，谁大谁出列，覆盖 nums1
    for k in range(m + n - 1, -1, -1):
        # 注意：同样要把 nums1 和 nums2 归并完成的逻辑写在前面，否则会出现数组下标越界异常
        if i == -1:
            # 直接把 nuns2 还没看的元素复制到 nums1 即可，在 Java 中有更好的方法
            nums1[k] = nums2[j]
            j -= 1
        elif j == -1:
            # 这里直接 break 掉就可以了，因为 nums2 遍历完成以后，nums1 剩下的元素虽然还没有看，但一定是排定以后的那个样子
            break
        elif nums1[i] > nums2[j]:
            nums1[k] = nums1[i]
            i -= 1
        else:
            nums1[k] = nums2[j]
            j -= 1
    return nums1
print(merge2([1, 2, 3, 4, 0, 0, 0],4, [2, 5, 6], 3))