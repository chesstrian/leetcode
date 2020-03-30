# https://leetcode.com/problems/intersection-of-two-arrays-ii/


class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        _hash = dict()
        result = []
        for i in nums1:
            if i in _hash:
                _hash[i] += 1
            else:
                _hash[i] = 1

        for i in nums2:
            if i in _hash and _hash[i] > 0:
                result.append(i)
                _hash[i] -= 1

        return result
