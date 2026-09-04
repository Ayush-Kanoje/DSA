
class Solution:
    def isFactorial(self,num):
        
        count = 0
        for i in num:
            if num%i == 0:
                count += 1

        return count


