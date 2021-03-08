class Solution:
    def isValid(s: str) -> bool:
        a = []
        for character in s:
            if len(a) == 0 or character in ["(","{","["]:
                a.append(character)
            else:
                if (a[-1]=="(" and character==')') or (a[-1]=='[' and character==']') or (a[-1]=='{' and character=='}'):
                    a.pop()
                else:
                    return False
        if len(a)==0:
            return True
        else:
            return False

if __name__=="__main__":
    # s = "()"
    # s = "()[]{}"
    # s = "(]"
    # s = "([)]"
    s = "{[]}"
    print(Solution.isValid(s))