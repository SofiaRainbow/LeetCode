"""
7. Reverse Integer
Given a 32-bit signed integer, reverse digits of an integer.

Example 1:

Input: 123
Output: 321

Example 2:

Input: -123
Output: -321

Example 3:

Input: 120
Output: 21

Note: Assume we are dealing with an environment which could only store integers within the
32-bit signed integer range: [−231,  231 − 1]. For the purpose of this problem, assume that your function returns 0
when the reversed integer overflows. """


class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        result = 0
        if 0 < x < (2 ** 31) - 1:
            x = str(x)
            result = int(x[::-1])
            if result >= (2 ** 31) - 1:
                result = 0
        elif 0 > x >= -2 ** 31:
            x = str(-x)
            result = -int(x[::-1])
            if result < -2 ** 31:
                result = 0
        return result


x = 123
x = -123
x = 120
solution = Solution()
results = solution.reverse(x)
print(results)
