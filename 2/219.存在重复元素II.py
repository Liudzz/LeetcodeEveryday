class Solution:
    def containsNearbyDuplicate(nums, k) -> bool:
        hashtabel = dict()
        repeat = []
        for i, num in enumerate(nums):
            if num in hashtabel:
                if num not in repeat:
                    repeat.append(num)
            hashtabel.setdefault(num, []).append(i)
        if len(repeat) == 0:
            return False
        for rep in repeat:
            for i in range(len(hashtabel[rep]) - 1):
                if hashtabel[rep][i + 1] - hashtabel[rep][i] <= k:
                    return True
        return False

if __name__=='__main__':
    nums = [1,0,1,1]
    k = 1
    print(Solution.containsNearbyDuplicate(nums,k))

# 60ms 26.3m