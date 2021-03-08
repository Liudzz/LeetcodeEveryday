# 前！缀！和！
class NumArray:

    def __init__(self, nums):
        self.a =[]
        for i in range(nums):
            j = input()
            self.a.append(j)

    def sumRange(self, i: int, j: int) -> int:
        sum = 0
        for num in range(i,j+1):
            sum += int(self.a[num])
        return sum

if __name__ == '__main__':
    obj = NumArray(5)
    print(obj)
    print(obj.sumRange(1,3))