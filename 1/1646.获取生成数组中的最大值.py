class Solution:
    def getMaximumGenerated(self, n: int) -> int:
        if n<=1:
            return n
        a=[0,1]
        for i in range(2,n+1):
            if i%2==0:
                a.append(a[int(i/2)])
            else:
                a.append(a[int((i-1)/2)]+a[int((i-1)/2)+1])
        return max(a)        
if __name__=='__main__':
    Solution.getMaximumGenerated(2)