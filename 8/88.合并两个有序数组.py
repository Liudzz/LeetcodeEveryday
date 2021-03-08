class Solution:
    def merge(nums1, m: int, nums2, n: int) -> None:
        i = 0
        for j in range(n):
            while (i < m):
                if nums2[j] >= nums1[i]:
                    i += 1
                else:
                    for k in range(j + i + 1, i, -1):
                        nums1[k] = nums1[k - 1]
                    nums1[i] = nums2[j]
                    m += 1
                    break
            if i >= m and nums2[j] >= nums1[i - 1]:
                nums1[i] = nums2[j]
                i += 1

if __name__=='__main__':
    nums1 = [1, 2, 3, 0, 0, 0]
    m,n = 3,3
    nums2 = [2,5,6]
    Solution.merge(nums1,m,nums2,n)
    print(nums1)
