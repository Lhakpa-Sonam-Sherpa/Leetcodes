class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x == 0:
            return True
        elif x < 0 or (x % 10 == 0):
            return False
        else:
            rev = 0
            while x > rev:
                r = x % 10
                rev = rev * 10 + r
                x = x // 10

            return x == rev or x == rev // 10

sol = Solution()
print(sol.isPalindrome(121))
print(sol.isPalindrome(-121))
print(sol.isPalindrome(10)) 