class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        #return arr.index(max(arr)) #方法1 36ms 93.41%
        min, max = 0, len(arr) - 1
        while (min < max):
            mid = min + int((max - min) / 2)
            if arr[mid] > arr[mid - 1] and arr[mid] > arr[mid + 1]:
                return mid
            elif arr[mid] > arr[mid - 1] and arr[mid] < arr[mid + 1]:
                min = mid
            elif arr[mid] < arr[mid - 1] and arr[mid] > arr[mid + 1]:
                max = mid
        # 二分 56ms 14.77