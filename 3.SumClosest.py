class Solution(object):
    def threeSumClosest(self,nums,target):
        nums.sort()
        length = len(nums)
        ans = None
        for i in range(length - 2):
            left, right = i + 1, length - 1
            while (left < right):
                sum = nums[i] + nums[left] + nums[right]
                if ans is None or abs(sum - target) < abs(ans - target):
                    ans = sum
                elif sum > target:
                    right -= 1
                else:
                    left += 1
        return ans


