from math import sqrt
         
class Solution:
    def countFactors (self, num):
        count = 0
        for val in range(1, int(sqrt(num))+1):
            if num%val == 0:
                count +=1

                if num//val != val:
                    count += 1
                    
        return num_list     


# TC - O(sqrt(N)) + O(N log N) 
# Sc - O(k) : amount of factors i.e O(1)


