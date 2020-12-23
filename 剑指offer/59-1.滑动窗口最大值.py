# 没读题写成最大和
# class Solution:
#     def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
#         maxnum,winsum= 0,0
#         for i in range(k):
#             winsum += nums[i]
#         maxnum = max(maxnum,winsum)
#         for i in range(1,len(nums)-k):
#             winsum = winsum+nums[i+k]-nums[i-1]
#             maxnum = max(maxnum,winsum)
#         return maxnum

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        maxarr = []
        if len(nums) == 0 and k == 0:
            return maxarr
        for i in range(0, len(nums) - k + 1):
            maxarr.append(max(nums[i:i + k]))
        return maxarr
# 488 ms
# 40.26%
# 18.1 MB
# 5.35%