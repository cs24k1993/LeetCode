#coding:utf-8
class Solution:
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        for i in range(len(nums)):

            if target > nums[len(nums) - 1]:  # can be replaced by nums[-1]
                return len(nums)

            if target == nums[i]:
                return i
            elif target > nums[i]:
                continue
            else:
                return i

        # 2
        for i in range(len(nums)):

            if target > nums[len(nums) - 1]:
                return len(nums)

            if target > nums[i]:
                continue
            else:
                return i

        # 3
        if target > nums[len(nums) - 1]:
            return len(nums)

        for i in range(len(nums)):

            if target > nums[i]:
                continue
            else:
                return i

        # 二分查找速度快一些
