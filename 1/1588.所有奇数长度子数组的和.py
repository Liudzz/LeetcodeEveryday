class Solution:
    def sumOddLengthSubarrays(self, arr: List[int]) -> int:
        le = 1
        result = 0
        for i in range(le,len(arr)+1,2):
            for j in range(len(arr)+1-i):
                for k in range(i):
                    result += arr[j+k]
        return result