class Solution:
    def armstrongNo(self,n):
        no = n
        add = 0
        s = str(n)

        count = len(s)

        for val in s:
            num = no % 10
            add += num ** count
            no //= 10

        if add == n:
            return True
        else:
            return False
    


# TC - O(log10(n))
# SC - O(log10(n))