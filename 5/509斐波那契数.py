class Solution:
    class Solution:
        def fib(self, n: int) -> int:
            if n < 2:
                return n
            a, b = 0, 1
            for i in range(2, n + 1):
                c = a + b
                a, b = b, c
            return c
    # 40ms 63.62% 14.7m 15.44

            # def fib(self, n: int) -> int:
    #     a=[0]*(n+1)
    #     if n==0:
    #         return  a[n]
    #     a[1] = 1
    #     for i in range(2,n+1):
    #         a[i] = a[i-1]+a[i-2]
    #     return a[n]
    # 52ms 30.71% 14.8m 10.17%

if __name__=='__main__':
    print(Solution.fib())