class Solution:
    def backspaceCompare(S: str, T: str) -> bool:
        ns, nt='', ''
        def process(str,nstr):
            for st in str:
                if st!="#":
                    nstr += st
                else:
                    if len(nstr)!=0:
                        nstr = nstr[:-1]
            return nstr
        ns = process(S,ns)
        nt = process(T,nt)
        if ns==nt:
            return True
        else:
            return False
if __name__=="__main__":
    # S = "ab#c"
    # T = "ad#c"
    # S = "ab##"
    # T = "c#d#"
    # S = "a##c"
    # T = "#a#c"
    S = "a#c"
    T = "b"
    print(Solution.backspaceCompare(S,T))


