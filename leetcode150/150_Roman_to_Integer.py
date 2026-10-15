class Solution:
    def romanToInt(self, s: str) -> int:
        n = 0
        i = len(s) - 1

        while i >= 0:
            if s[i] == "M" and s[i - 1] == "C" and i > 0:
                n = n + 900
                i -= 2
            elif s[i] == "D" and s[i - 1] == "C" and i > 0:
                n = n + 400
                i -= 2
            elif s[i] == "C" and s[i - 1] == "X" and i > 0:
                n = n + 90
                i -= 2
            elif s[i] == "L" and s[i - 1] == "X" and i > 0:
                n = n + 40
                i -= 2
            elif s[i] == "X" and s[i - 1] == "I" and i > 0:
                n = n + 9
                i -= 2
            elif s[i] == "V" and s[i - 1] == "I" and i > 0:
                n = n + 4
                i -= 2
            elif s[i] == "M":
                n = n + 1000
                i -= 1
            elif s[i] == "D":
                n = n + 500
                i -= 1
            elif s[i] == "C":
                n = n + 100
                i -= 1
            elif s[i] == "L":
                n = n + 50
                i -= 1
            elif s[i] == "X":
                n = n + 10
                i -= 1
            elif s[i] == "V":
                n = n + 5
                i -= 1
            elif s[i] == "I":
                n = n + 1
                i -= 1
        return n


# Better solution
#
# class Solution:
#     def romanToInt(self, s: str) -> int:
#         symbol_values = {
#             "I": 1,
#             "V": 5,
#             "X": 10,
#             "L": 50,
#             "C": 100,
#             "D": 500,
#             "M": 1000,
#         }

#         total = 0
#         value_to_the_right = 0  # value of the symbol we processed just before (to the right)

#         # Walk the string from right to left.
#         for symbol in reversed(s):
#             current_value = symbol_values[symbol]

#             if current_value < value_to_the_right:
#                 # A smaller symbol before a larger one means subtraction.
#                 # Example: the "I" in "IV" -> 5 - 1 = 4
#                 total -= current_value
#             else:
#                 # Normal case: add the value.
#                 # Example: the "V" in "VI" -> 5 + 1 = 6
#                 total += current_value

#             value_to_the_right = current_value

#         return total


s = Solution()
print(s.romanToInt(s="MMMCDXC"))
