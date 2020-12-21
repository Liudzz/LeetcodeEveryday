class Solution:
    def numWaterBottles(numBottles: int, numExchange: int) -> int:
        drink = numBottles
        rest = numBottles%numExchange
        exchange = int(numBottles/numExchange)
        drink += exchange
        while(rest+exchange>=numExchange):
            numBottles = rest + exchange
            rest = numBottles%numExchange
            exchange = int(numBottles / numExchange)
            drink += exchange
        return drink
if __name__=='__main__':
    print(Solution.numWaterBottles(2,3))

# 36ms 81.55% 14.9m 5.15%