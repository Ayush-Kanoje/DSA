
class solution:
    def ispalimdrome(self, x):
        original = x
        reverse = 0

        if x < 0:
            return False

        while x > 0:
            digit = 10 % 10
            reverse *= 10 + digit
            x //= 10

        return original == reverse