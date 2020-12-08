class Solution:
    def rob(self, nums: List[int]) -> int:
        steal=[]
        for i in range(len(nums)):
            if i == 0:
                steal.append(nums[0])
            elif i==1:
                steal.append(max(nums[0],nums[1]))
            elif i >=2:
                steal.append(max(nums[i]+steal[i-2],steal[i-1]))
        if len(nums)==0:
            return 0
        else:
            return steal[-1]