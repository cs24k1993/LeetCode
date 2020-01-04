# coding:utf-8
# 第1种解法
'''
三次反转，将数组分为两段
1.反转第一段，[4,3,2,1,5,6,7]
2.反转第二段，[4,3,2,1,7,6,5]
3.反转整体，[5,6,7,1,2,3,4]
'''
def rotate(nums,k):
    n = len(nums)
    # 必须加上下面式子，如果k>n，就是旋转了一圈以上，所以求余数
    k = k % n
    def swap(l,r):
        while(l<r):
            nums[l],nums[r] = nums[r],nums[l]
            l=l+1
            r=r-1
    swap(0,n-k-1)
    swap(n-k,n-1)
    swap(0,n-1)
    return nums
print(rotate([1,2,3,4,5,6,7],3))


# 第2种解法
# 本质还是三次反转
def rotate2(nums,k):
    n = len(nums)
    k = k % n
    nums[:] = nums[::-1]
    nums[:k] = nums[:k][::-1]
    nums[k:] = nums[k:][::-1]
    return nums
print(rotate2([1,2,3,4,5,6,7],3))


# 第3种解法
# 整个数组往后移k位，后面k位变成在前面
def rotate3(nums,k):
    n = len(nums)
    k = k % n
    nums[:] = nums[-k:] + nums[:-k]
    return nums
print(rotate3([1,2,3,4,5,6,7],3))