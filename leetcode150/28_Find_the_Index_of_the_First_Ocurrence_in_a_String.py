class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        i, j = 0, 0
        while i < len(haystack) and j < len(needle):
            if needle[j] == haystack[i]:
                j += 1
                i += 1
            else:
                i = i + 1 - j
                j = 0
        if j == len(needle):
            return i - j
        return -1
