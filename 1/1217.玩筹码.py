class Solution:
    def minCostToMoveChips(position) -> int:
        odd,even=0,0
        for pos in position:
            if pos%2:
                odd +=1
            else:
                even +=1
        return min(odd,even)


if __name__=='__main__':
    chips = [2,2,2,3,3]
    print(Solution.minCostToMoveChips(chips))
# 36ms 81.53 14.9m 6.07%