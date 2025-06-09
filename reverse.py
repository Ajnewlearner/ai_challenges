class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        reverse = int(str(abs(x))[::-1])
        if reverse > 2147483648:
            return 0
        if x < 0:
            reverse = -reverse
        return reverse
s = Solution()
print(s.reverse(345))    