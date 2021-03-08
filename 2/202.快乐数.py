class Solution:
    def isHappy(n: int) -> bool:
        counter = 65535
        while(n!=1):
            s = str(n)
            n = 0
            for si in s:
                n += int(si)*int(si)
            if counter:
                counter -=1
            else:
                return False
        if n==1:
            return True

        # elif n==2 or n==3:
        #     return False
if __name__=="__main__":
    for i in range(1,11):
        print("{}:{}".format(i,Solution.isHappy(i)))