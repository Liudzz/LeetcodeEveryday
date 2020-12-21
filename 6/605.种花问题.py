class Solution:
    def canPlaceFlowers(flowerbed ,n) -> bool:
        planted = 0
        canplant = 0
        for i in range(len(flowerbed)):
            if flowerbed[i] == 1:
                planted = 1
            else:
                if planted == 0:
                    if i + 1 < len(flowerbed):
                        if flowerbed[i + 1] != 1:
                            canplant += 1
                            planted = 1
                    if i == len(flowerbed) - 1:
                        canplant += 1
                        planted = 1
                else:
                    planted = 0
            if canplant >= n:
                return True
        return False

if __name__=='__main__':
    flowerbed = [1,0,0,0,1,0,0]
    n =2
    result = Solution.canPlaceFlowers(flowerbed,n)
    print(result)