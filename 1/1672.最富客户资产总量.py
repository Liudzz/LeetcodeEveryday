class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        max = sum(accounts[0])
        for i in range(1,len(accounts)):
            j = sum(accounts[i])
            if j>max:
                max = j
        return max

    # 40ms 60.76% 14.8m 12.22%