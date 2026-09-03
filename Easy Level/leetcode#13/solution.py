class Solution:
    def romanToInt(self, s: str) -> int:
        roman_val = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000
        }

        total = 0

        roman_list = list(s)

        for idx, val in enumerate(roman_list):

            current = roman_val[val]

            if idx + 1 < len(roman_list):
                next_val = roman_val[roman_list[idx + 1]]

                if current < next_val:
                    total -= current
                else:
                    total += current
            else:
                total += current

        return total



# TC - O(n)
# SC - O(n)
