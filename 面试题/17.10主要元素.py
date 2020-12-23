class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        le = len(nums)
        counter = dict()
        for i in range(le):
            if nums[i] not in counter.keys():
                counter[nums[i]]=1
            else:
                counter[nums[i]]+=1
        for key,value in counter.items():
            if value>int(le/2):
                return key
        return -1