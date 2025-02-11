# coding:utf-8
# 第1种解法
'''
1.具有度数 d 的数组必须有一些元素 x 出现 d 次。如果某些子数组具有相同的度数，
那么某些元素 x （出现 d 次）。最短的子数组是将从 x 的第一次出现到最后一次出现的数组。
2.对于给定数组中的每个元素，让我们知道 left 是它第一次出现的索引； right 是它最后一次出现的索引。
例如，当 nums = [1,2,3,2,5] 时，left[2] = 1 和 right[2] = 3。
3.然后，对于出现次数最多的每个元素 x，right[x] - left[x] + 1 将是我们的候选答案，
我们将取这些候选的最小值。
'''
def findShortestSubArray2(nums):
    count = 1
    res = 1
    nums.sort()
    for i in range(len(nums)-1):
        if nums[i+1] == nums[i]:
            count += 1
            res = max(res, count)
        else:
            count = 1
    return res

print(findShortestSubArray2([1,2,2,3,1,4,2]))


# 下面的解法有问题，Bug
def findShortestSubArray(nums):
    left, right, count = {}, {}, {}
    for i,x in enumerate(nums):
        if x not in left:
            left[x] = i
        right[x] = i
        # count 存储x出现的次数
        count[x] = count.get(x,0) + 1
    ans = len(nums)
    degree = max(count.values())
    for x in count:
        if count[x] == degree:
            ans = min(ans,right[x] - left[x] +1)
    return ans

print(findShortestSubArray([1,2,2,3,1,4,2]))


