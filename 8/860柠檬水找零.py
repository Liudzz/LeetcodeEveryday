class Solution:
    def lemonadeChange(bills) -> bool:
        change = dict()
        change['5'],change['10']=0,0
        for i in range(len(bills)):
            if bills[i]==5:
                change['5']+=1
            elif bills[i] == 10:
                if change['5'] == 0:
                    return False
                else:
                    change['5'] -= 1
                    change['10'] += 1
            elif bills[i] == 20:
                if change['10']!=0:
                    if change['5'] !=0:
                        change['5'] -= 1
                        change['10'] -= 1
                    else:
                        return False
                else:
                    if change['5']>=3:
                        change['5'] -= 3
                    else:
                        return False
        return True

if __name__=='__main__':
    result = Solution.lemonadeChange([5,5,5,10,20])
    print(result)