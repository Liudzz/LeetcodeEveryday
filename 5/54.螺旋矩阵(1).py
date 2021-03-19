class Solution:
    def spiralOrder(matrix):
        if not matrix or matrix[0]:
            return []
        result = []
        top, bottom, left, right = 0, len(matrix) - 1, 0, len(matrix[0]) - 1
        # move = [(0,1),(1,0),(0,-1),(-1,0)]
        step, index, i, j,k= 0, 0, 0, 0, 0
        while(step<=len(matrix)*len(matrix[0])):
            # move right
            for k in range(j,right):
                result.append(matrix[i][j+k])
                step += 1
            j += k+1
            # mo

if __name__=="__main__":
    i=0
    for i in range(5):
        pass
    print(i)