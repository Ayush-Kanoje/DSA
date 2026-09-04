class Solution:
    def commonFactors(self, a: int, b: int) -> int:
        
        a1 = ()
        b1 = ()

        for i in range(1,a+1):
            if a%i == 0:
                a1.add(i)

        for i in range(1, b+1):
            if b%i == 0:
                b1.add(i)


        common_fact = a1.intersection(b1)
        return common_fact

# TC - O(a+b)
# SC - O(a+b)