class Solution:
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        result = [1]
        for _ in range(rowIndex):
            result = [x + y for x, y in zip([0] + result, result + [0])]
        return result


class Solution(object):
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        row = [0] * (rowIndex + 1)
        row[-1] = 1
        i = len(row) - 2
        for k in xrange(1, rowIndex + 1):
            row[i] = 1
            for j in xrange(i + 1, len(row) - 1):
                row[j] += row[j + 1]
            i -= 1

        return row