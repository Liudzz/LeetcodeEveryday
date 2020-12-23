class Solution:
    def firstUniqChar(s: str) -> int:
        checked=[]
        for i in range(len(s)):
            flag = 1
            if s[i] not in checked:
                for j in range(i+1,len(s)):
                    if s[i]==s[j]:
                        flag = 0
                        checked.append(s[j])
                        break
                if flag:
                    return i
        return -1
if __name__=='__main__':
    print(Solution.firstUniqChar("leetcode"))