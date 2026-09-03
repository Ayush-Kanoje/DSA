class Solution:
    def palindrome(self, x: int):
        s = str(x)
        s2 = s[::-1]
        if s == s2:
            return True
        else:
            return False


# TC - O(log10(x))
# SC - O(log10(x))

