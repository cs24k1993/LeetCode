'''
Input: [1,2,3]
Output: [1,2,4]
Explanation: The array represents the integer 123.
'''

class Solution:
    def plusOne(self, digits):
        j = len(digits) - 1
        while j >= 0:
            if digits[j] == 9:
                digits[j] = 0
                if j == 0:
                    digits.insert(0, 1)
            else:
                digits[j] += 1
                break
            j -= 1
        return digits

s = Solution()
print(s.plusOne([1,2,9]))