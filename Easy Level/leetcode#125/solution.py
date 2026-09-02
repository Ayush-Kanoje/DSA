class Solution:
    def isPalindrome(self,s:str):
        s2 = s.lower()
        strlist = []
    
        for val in s2:
            if val.isalnum(): 
                strlist.append(val)
        
        result = "".join(strlist)
        result2 = result[::-1]
       
        if result == result2:
            return True
        else:
            return False

sol = Solution()
result3 = sol.isPalindrome("0P")
print(result3)