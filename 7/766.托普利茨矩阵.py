#执行用时：
# 48 ms
# 82.87%
# 14.8 MB
# 5.38%
class Solution:
    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
        hang = len(matrix)
        lie = len(matrix[0])
        for i in range(hang):
            j, k = i, 0
            while (j < hang - 1 and k < lie - 1):
                if matrix[j][k] != matrix[j + 1][k + 1]:
                    return False
                j += 1
                k += 1
        for i in range(1, lie):
            j, k = 0, i
            while (j < hang - 1 and k < lie - 1):
                if matrix[j][k] != matrix[j + 1][k + 1]:
                    return False
                j += 1
                k += 1
        return True