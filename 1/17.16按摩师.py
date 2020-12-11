class Solution:
    def massage(self, nums: List[int]) -> int:
        t = [0 for i in range(len(nums))]

        for i in range(0, len(t)):
            if i == 0:
                t[i] = nums[i]
            elif i >= 3:
                t[i] = max(nums[i] + t[i - 2], nums[i - 1] + t[i - 3])
            elif i >= 2:
                t[i] = max(nums[i] + t[i - 2], nums[i - 1])
            elif i < 2:
                t[i] = max(nums[i], nums[i - 1])
        if len(nums) !=0:
            return (t[-1])
        else:
            return 0