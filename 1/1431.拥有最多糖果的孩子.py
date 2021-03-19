class Solution:
    def kidsWithCandies(candies, extraCandies: int) :
        if not len(candies):
            return []
        result = []
        biggest = max(candies)
        for i in range(len(candies)):
            if candies[i] + extraCandies >= biggest:
                result.append(True)
            else:
                result.append(False)
        return result
if __name__ == "__main__":
    candies = [2, 3, 5, 1, 3]
    extraCandies = 3
    print(Solution.kidsWithCandies(candies,extraCandies))