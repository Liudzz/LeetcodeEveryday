import time
class Solution:
    def calPoints(ops) -> int:
        result = []
        total = 0
        for op in ops:
            if op not in ['C','D','+']:
                result.append(int(op))
            else:
                if op=='C':
                    result.pop()
                elif op == 'D':
                    result.append(2*int(result[-1]))
                elif op == '+':
                    result.append(int(result[-1])+int(result[-2]))
        for res in result:
            total += res
        return total

if __name__=="__main__":
    # ops = ["5","2","C","D","+"]
    ops = ["5", "-2", "4", "C", "D", "9", "+", "+"]
    j = time.time()
    i = Solution.calPoints(ops)
    print(time.time()-j)
    print(i)