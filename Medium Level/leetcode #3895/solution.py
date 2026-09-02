class Solution:
    def countDigitOccurrences(self, nums: list[int], digit: int) -> int:


        count = 0

        for idx,val in enumerate(nums):
            while val > 0:
                digit_no = val%10
                if digit_no > 0 and digit_no == digit:
                    count+=1          
                val//=10

        return count   

