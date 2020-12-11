class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        hashtable = dict()
        t = []
        for num in (nums):
            if num not in hashtable.keys():
                hashtable[num] = 1
            else:
                hashtable[num] += 1

        for num in nums:
            temp = 0
            for key in hashtable.keys():
                if key < num:
                    temp += hashtable[key]
            t.append(temp)
        return t

# 96ms 35.3% 15m 5.25%