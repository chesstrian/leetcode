# https://leetcode.com/problems/two-sum/


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        _hash = dict()
        for i, num in enumerate(nums):
            diff = target - num
            if diff not in _hash:
                _hash[num] = i
            else:
                return [_hash[diff], i]
