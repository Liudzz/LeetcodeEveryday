class Solution:
    def largestSumAfterKNegations(A,K) -> int:
        A.sort()
        min = 0
        for i in range(K):
            if A[i]<0:
                A[i] = -A[i]
                min +=1
            else:
                break
        A.sort()

        K -= min
        if K%2:
            A[0] = -A[0]
        return sum(A)


if __name__=='__main__':
    A = [2,-3,-1,5,-4]
    K = 2
    print(Solution.largestSumAfterKNegations(A,K))