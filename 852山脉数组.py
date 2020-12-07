class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        max = arr[0]
        for i in range(1,len(arr)):
            if arr[i]>max:
                max = arr[i]
            else:
                return i-1
