class Solution:
    def removeDuplicates(S: str) -> str:
        result = "."
        for s in S:
            # if len(result)==0:
            #     result += s
            # else:
            if result[-1]==s:
                result=result[:-1]
            else:
                result +=s
        return result[1:]

if __name__ == "__main__":
    a = "abbaca"
    print(Solution.removeDuplicates(a))