class Solution:
    def spiralOrder(matrix) :
        result = []
        i, j = 0, 0 # start location

        def move(i,j,direction, direc):
            k = 0
            if direc == 'r':
                j += 1
                if j<=direction:
                    for k in range(j,direction+1):
                        result.append(matrix[i][k])
                    return i,k
                else:
                    return i,j
            elif direc == 'b':
                i += 1
                if i <= direction:
                    for k in range(i, direction + 1):
                        result.append(matrix[k][j])
                    return k, j
                else:
                    return i,j
            elif direc == 'l':
                j -= 1
                if j >= direction:
                    for k in range(j,direction-1,-1):
                        result.append(matrix[i][k])
                    return i, k
                else:
                    return i,j
            elif direc == 't':
                i -= 1
                if i>=direction:
                    for k in range(i, direction-1,-1):
                        result.append(matrix[k][j])
                    return k,j
                else:
                    return i,j

        top, bottom, left, right = 0, len(matrix) - 1, 0, len(matrix[0]) - 1
        def check(top,bottom,left,right):
            if top == bottom and left == right:
                return False
            else:
                return True
        while(check(top,bottom,left,right)):
            result.append(matrix[0][0])

            i,j = move(i,j,right,"r")
            top += 1
            if not check(top, bottom, left, right):
                break

            i,j = move(i,j,bottom,"b")
            right -= 1
            if not check(top, bottom, left, right):
                break

            i,j = move(i,j,left,"l")
            bottom -= 1
            if not check(top, bottom, left, right):
                break

            i,j = move(i,j,top,"t")
            left += 1

        result.append(matrix[left][right])
        return result

if __name__ =='__main__':
    # matrix = [[1,2,3],[4,5,6],[7,8,9]]
    matrix = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]
    print(Solution.spiralOrder(matrix))