class Solution:
    def palindrome(self, x: int):
        s = str(x)
        s2 = s[::-1]
        if s == s2:
            return True
        else:
            return False


# Simple input example
sol = Solution()
result = sol.palindrome(121)
print(result)