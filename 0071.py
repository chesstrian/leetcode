# https://leetcode.com/problems/simplify-path/


class Solution:
    def simplifyPath(self, path: str) -> str:
        result = []
        paths = path.split('/')

        for _p in paths:
            if _p == '..':
                result and result.pop()
            elif _p not in ('', '.'):
                result.append(_p)

        return '/' + '/'.join(result)

