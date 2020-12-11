class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        if len(cost) == 0:
            return 0
        else:
            for i in range(len(cost)+1):
                if i==0:
                    now =0
                    prev=0
                    pc=0
                elif i==1:
                    pc = now+cost[i-1]
                    now = min(pc,prev)
                    prev = now
                else:
                    now = min(prev+cost[i-1],pc)
                    pc = prev+cost[i-1]
                    prev = now

            return now

