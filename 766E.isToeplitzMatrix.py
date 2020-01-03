# coding:utf-8
# 第1种解法
# 和矩阵右下角的元素比，如果不等，返回False
def isToeplitzMatrix(matrix):
    for i in range(len(matrix) - 1):
        for j in range(len(matrix[0]) - 1):
            if matrix[i][j] != matrix[i + 1][j + 1]:
                return False
    return True


# 第2种解法
# 利用切片，和矩阵左上角的元素比，如果不等，返回False
def isToeplitzMatrix2(matrix):
    for i in range(1,len(matrix)):
        if matrix[i][1:] != matrix[i-1][:-1]:
            return False
    return True