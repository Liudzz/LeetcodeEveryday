class Solution:
    def isPalindrome(s: str) -> bool:
        l = len(s)
        i,j = 0,l-1
        def checkalaph(chr):
            if (ord(chr) in range(ord('a'),ord('z')+1)) or (ord(chr) in range(ord('A'),ord('Z')+1)):
                return False
            else:
                return True

        while(i<j):
            while (s[i] == ' ' or checkalaph(s[i])):
                i += 1
            while(s[j] == ' ' or checkalaph(s[j])):
                j -= 1
            if s[i].lower() != s[j].lower():
                return False
            i += 1
            j -= 1
        return True

# s = "A man, a plan, a canal: Panama"
s ="race a car"
print(Solution.isPalindrome(s))

# i = 1 in range(1,3)
# print(i)