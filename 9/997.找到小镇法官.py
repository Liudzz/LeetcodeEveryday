class Solution:
    def findJudge(N: int, trust)-> int:
        if N==1:
            return 1
        arr=[ [0 for j in range(N)] for i in range(N)]
        for t in trust:
            arr[t[0]-1][t[1]-1] = 1
        flag = 1
        for i in range(N):
            flag = 1
            for j in range(N):
                if arr[i][j] !=0:
                    flag = 0
                    break
            if flag:
                for j in range(N):
                    if j!=i and arr[j][i] != 1:
                        flag = 0
                        break
            if flag:
                return i+1
        if not flag:
            return -1
# 456 ms
# 8.68%
# 25.8 MB
# 5.11%