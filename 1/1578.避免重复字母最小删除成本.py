
class Solution:
    def minCost(s: str, cost) -> int:
        i = 0
        length = len(s)
        ret = 0

        while i < length:
            ch = s[i]
            maxValue = 0
            total = 0

            while i < length and s[i] == ch:
                maxValue = max(maxValue, cost[i])
                total += cost[i]
                i += 1

            ret += (total - maxValue)

        return ret


if __name__=='__main__':
    s="aaabbbabbbb"
    cost = [3,5,10,7,5,3,5,5,4,8,1]
    print(Solution.minCost(s,cost))
