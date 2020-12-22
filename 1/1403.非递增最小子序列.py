class Solution:
    def minSubsequence(nums) :
        nums.sort()
        le =len(nums)
        if le == 1:
            return nums
        for i in range(le):

            if sum(nums[le-i-1:])>sum(nums[:le-i-1]):
                j = nums[le-i-1:]
                j.reverse()
                return j
if __name__=='__main__':
    print(Solution.minSubsequence([7]))