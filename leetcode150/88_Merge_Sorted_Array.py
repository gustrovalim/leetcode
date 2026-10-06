from typing import List


class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """

        nums1[:] = nums1[:m] + nums2


        for i in range(len(nums1)):
            for j in range (i +1, len(nums1)):
                if nums1[i] > nums1[j]:
                    nums1[i], nums1[j] = nums1[j], nums1[i]


# nums1 = [1,2,3,0,0,0]
# m = 3
# nums2 = [2,5,6]
# n = 3

# Solution().merge(nums1, m, nums2, n)
# # [1,2,2,3,5,6]
# print(nums1)