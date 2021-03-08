class Solution:
    def nextGreaterElements(nums):
        l = len(nums)
        result = []
        for i in range(l):
            now = nums[i]
            flag  = 0
            if i==l-1:
                j=0
            else:
                j=i+1

            while j != i:
                next = nums[j]
                if next > now:
                    result.append(next)
                    flag = 1
                    break
                else:
                    j += 1
                    if j>= l:
                        j %= l
            if not flag:
                result.append(-1)
        return result

if __name__ == "__main__":
    nums = [1,2,1]
    print(Solution.nextGreaterElements(nums))