class Solution:
    def lastStoneWeight(stones) -> int:
        i = len(stones)
        while(i>=2):
            stones.sort()
            if stones[i-1]!=stones[i-2]:
                minis = stones[i-1]-stones[i-2]
            else:
                minis = 0
            del(stones[i-1])
            del(stones[i-2])
            if minis:
                stones.append(minis)
            i = len(stones)
        if i==0:
            return i
        else:
            return stones[i-1]
if __name__=='__main__':
    print(Solution.lastStoneWeight([2,7,4,1,8,1]))