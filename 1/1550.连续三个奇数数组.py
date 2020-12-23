class Solution:
    def threeConsecutiveOdds(self, arr: List[int]) -> bool:
        i = 0
        while(i<len(arr)-2):
            flag=1
            for j in range(3):
                if arr[i+j]%2:
                    continue
                else:
                    flag = 0
                    i = i+j+1
                    break
            if flag:
                return True
        return False