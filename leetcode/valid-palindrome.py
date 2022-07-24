import re

class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.upper()
        s = re.sub("[^A-Z0-9]", "", s)
        return s == s[::-1]