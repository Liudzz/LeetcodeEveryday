class Solution:
    def findContentChildren(g ,s) -> int:
        gtail = len(g)-1
        shead = 0
        g = sorted(g)
        s = sorted(s)
        while(gtail>=0 and shead<=(len(s)-1)):
            if (g[gtail]<=s[shead]):
                return min(gtail+1,len(s)-shead)
            else:
                if shead==(len(s)-1):
                    gtail -=1
                    # shead +=1
                elif gtail==0:
                    shead +=1
                else:
                    gtail -=1
                    shead +=1
if __name__=='__main__':
    g = [1,2]
    s = [1,2,3]
    print(Solution.findContentChildren(g,s))