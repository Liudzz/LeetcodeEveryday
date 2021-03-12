class Solution:
    def calculate(s: str) -> int:
        numstack = []
        chasatck = []
        sa = 0
        s = s.replace(" ",'')
        while sa < len(s):
            if s[sa] not in ['+','-','*','/']:
                    numstack.append(int(s[sa]))
                    sa += 1
            else:
                if s[sa] in ["*","/"]:
                    last = numstack.pop()

                    next = int(s[sa+1])
                    if s[sa]=='*':
                        numstack.append(last*next)
                    else:
                        numstack.append(int(last/next))
                    sa += 2
                else:
                    chasatck.append(s[sa])
                    sa += 1
        while(len(chasatck) != 0):
            next = numstack.pop()
            last = numstack.pop()
            char = chasatck.pop()
            if char == "+":
                numstack.append(next+last)
            else:
                numstack.append(last-next)
        return numstack[0]

if __name__ == "__main__":
    s = " 3+5 / 2 "
    print(Solution.calculate(s))
    # print(ord('0'))
    # print(ord('9'))