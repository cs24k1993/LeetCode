def merge(nums1,m,nums2,n):
    i = m - 1
    j = n - 1
    for k in range(m+n-1,-1,-1):
        if i == -1:
            nums1[k]=nums2[j]
            j -= 1
        elif j == -1:
            break
        elif nums1[i] > nums2[j]:
            nums1[k] = nums1[i]
            i -= 1
        else:
            nums1[k] = nums2[j]
            j -= 1
    return nums1

print(merge([1, 2, 3, 4, 0, 0, 0],4, [2, 5, 6], 3))
