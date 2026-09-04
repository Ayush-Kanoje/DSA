
# class Solution:
#     def isFactorial(self,num):
        
#         count = 0
        
#         for i in num:
#             if num%i == 0:
#                 count += 1

#         return count


num = 5
count = 0
        
for i in range(1,num+1):
    while i * i <= num:
        if num%i == 0:
            count += 1
                
print(count)