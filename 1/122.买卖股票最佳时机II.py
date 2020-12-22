class Solution:
    def maxProfit(prices) -> int:
        le = len(prices)
        earn,i = 0,0
        while i<le-1:
            for j in range(i+1,le):
                if prices[j]-prices[i]<=0:
                    i = j
                    break
                else:
                    if j<le-1:
                        if prices[j]<prices[j+1]:
                            continue
                        else:
                            earn += prices[j]-prices[i]
                            i=j+1
                            break
                    elif j==le-1:
                        earn += prices[j]-prices[i]
                        return earn

        return earn


if __name__=='__main__':
    prices =  [7,1,5,3,6,4]
    print(Solution.maxProfit(prices))

# 76ms 67.72 15.7m 11.07