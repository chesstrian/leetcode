# https://leetcode.com/problems/duplicate-zeros/


class Solution:
    def duplicateZeros(self, arr: List[int]) -> None:
        """
        Do not return anything, modify arr in-place instead.
        """
        last_index = -1
        for i, num in enumerate(arr):
            if i > last_index and num == 0:
                last_index = i + 1
                arr.insert(i, 0)
                arr.pop()

