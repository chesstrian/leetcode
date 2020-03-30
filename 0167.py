# https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/


class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        _hash = dict()
        for i, number in enumerate(numbers):
            diff = target - number
            if diff in _hash:
                return [_hash[diff] + 1, i + 1]
            else:
                _hash[number] = i

