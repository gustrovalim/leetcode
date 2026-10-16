class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        first_word = strs[0]
        common_prefix = ""

        j = 0
        while j < len(first_word):
            current_char = first_word[j]
            i = 1
            while i < len(strs):
                word = strs[i]
                if j >= len(word):
                    return common_prefix
                if word[j] != current_char:
                    return common_prefix
                i += 1
            common_prefix += current_char
            j += 1
        return common_prefix


# Optimal solution: vertical scan with slicing
# Time: O(S), S = total characters across all words. We can't do better,
#       since in the worst case (all words identical) every character must be checked.
# Space: O(1) extra, the prefix is only created once at the end with a slice.
# class SolutionOptimal:
#     def longestCommonPrefix(self, strs: list[str]) -> str:
#         # Use the shortest word as reference: the prefix can't be longer than it,
#         # so j never goes past the end of any word and no length check is needed
#         shortest = min(strs, key=len)

#         for j in range(len(shortest)):
#             for word in strs:
#                 # First mismatch in column j: everything before j is the prefix
#                 if word[j] != shortest[j]:
#                     return shortest[:j]

#         # Every column matched: the whole shortest word is the prefix
#         return shortest
