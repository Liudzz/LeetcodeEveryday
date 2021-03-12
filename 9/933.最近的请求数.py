import collections
class RecentCounter:

    def __init__(self):
        self.a = collections.deque()



    def ping(self, t: int) -> int:
        self.a.append(t)
        while(len(self.a) and self.a[0]<t-3000):
            self.a.popleft()
        return len(self.a)

# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)
if __name__=="__main__":
    i = RecentCounter()
    print(i.ping(1))
    print(i.ping(100))
    print(i.ping(3001))
    print(i.ping(3002))