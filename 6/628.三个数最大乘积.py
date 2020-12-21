class Solution:
    def maximumProduct(self, nums: List[int]) -> int:
        nums = sorted(nums)
        if nums[0]*nums[1]*nums[-1]>nums[-1]*nums[-2]*nums[-3]:
            return nums[0]*nums[1]*nums[-1]
        else:
            return nums[-1]*nums[-2]*nums[-3]

# 68 ms
# 95.09%
# 15.5 MB
# 5.22%