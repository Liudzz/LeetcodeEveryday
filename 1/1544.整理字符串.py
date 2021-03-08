class Solution:
    def makeGood(s: str) -> str:
        result = ''
        for num in range(len(s)):
            if num == 0 :
                result += s[num]
            else:
                if len(result) == 0:
                    result += s[num]
                else:
                    if result[-1] != s[num]:
                        if result[-1].upper()==s[num] or result[-1].lower()==s[num]:
                            result = result[:-1]
                        else:
                            result += s[num]
                    else:
                        result += s[num]
        return result


if __name__=="__main__":
    # result = "abcdefg"
    # print(result[:-1])
    # s = "leEeetcode"
    s = "s"
    print(Solution.makeGood(s))