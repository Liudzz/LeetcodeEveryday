class Solution:
    def largeGroupPositions(s: str) :
        result = []
        if len(s) < 3:
            return result
        start, end, flag = 0, 1, 1
        while (end < len(s)):
            if s[end] != s[start]:
                if flag >= 3:
                    result.append([start, end - 1])
                flag = 1
                start = end
                end += 1
            else:
                flag += 1
                end += 1
                if end == len(s) and flag >= 3:
                    result.append([start, end - 1])
        return result
if __name__=='__main__':
    # s = "abbxxxxzzy"
    # s="abcdddeeeeaabbbcd"
    # s="aaa"
    s="bababbabaa"
    print(Solution.largeGroupPositions(s))
