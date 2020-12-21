# 824 ms
# 6.26%
# 19.4 MB
# 5.84%
class Solution:
    def findJudge(N: int, trust)-> int:
        oinum = [[0,0]for i in range(N)]
        for i in range(len(trust)):
            oinum[trust[i][0]-1][0] +=1
            oinum[trust[i][1]-1][1] +=1
        for i in range(N):
            if oinum[i][0]==0 and oinum[i][1] == N-1:
                return i+1
        return -1

if __name__=='__main__':
    N = 2
    trust = [[1, 2]]
    result = Solution.findJudge(N,trust)
    print(result)
