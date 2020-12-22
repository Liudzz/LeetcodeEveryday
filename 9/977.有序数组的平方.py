class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        le = len(nums)
        left,right,cur=0,le-1,le-1
        result = [0]*le
        while left<=right:
            doubleleft = nums[left]*nums[left]
            doubleright = nums[right]*nums[right]
            if doubleleft>doubleright:
                result[cur] = doubleleft
                left +=1
            else:
                result[cur] = doubleright
                right -=1
            cur -=1
        return result
# 88ms 16.3mb