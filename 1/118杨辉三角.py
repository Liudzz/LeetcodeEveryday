class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        trangle=[]
        for i in range(numRows):
            trangle.append([])
            rownum = i+1
            for j in range(rownum):
                if j==0 or j==i:
                    trangle[i].append(int(1))
                else:
                    trangle[i].append(int(trangle[i-1][j-1]+trangle[i-1][j]))
        return trangle

        #print(trangle)
