# https://leetcode.com/problems/longest-palindromic-substring/
# Microsoft + Google + Samsung + Visa IQ
class Solution:
    def longestPalindrome(self, s: str) -> str:
        i = 0
        j = len(s)
        if i == j:
            return ""

        if self.is_palindrome(s):
            return s
        else:
            val1 = self.longestPalindrome(s[i + 1:j])
            val2 = self.longestPalindrome(s[i:j - 1])

            if len(val1) > len(val2):
                return val1
            else:
                return val2

        return ""

    @staticmethod
    def is_palindrome(s: str):
        return s == s[::-1]


# print(Solution().longestPalindrome("babad"))
print(Solution().longestPalindrome("abbcccbbbcaaccbababcbcabca"))
