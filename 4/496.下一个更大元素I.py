class Solution:
    def nextGreaterElement(nums1, nums2) :
        result = []
        for num in nums1:
            flag = 0
            for j in range(len(nums2)):
                if nums2[j] == num:
                    if j < len(nums2):
                        for k in range(j+1,len(nums2)):
                            if nums2[k]>num:
                                result.append(nums2[k])
                                flag = 1
                                break
                        if not flag:
                            result.append(-1)
        return result
if __name__ == "__main__":
    # nums1 = [4,1,2]
    # nums2 = [1,3,4,2]
    nums1 = [2, 4]
    nums2 = [1, 2, 3, 4]
    print(Solution.nextGreaterElement(nums1,nums2))