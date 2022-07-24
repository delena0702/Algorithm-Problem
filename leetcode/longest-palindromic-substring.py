class Solution:
    def longestPalindrome(self, s: str) -> str:
        N = len(s)

        def expand(l, r):
            while l >= 0 and r < N and s[l] == s[r]:
                l, r = l-1, r+1
            return s[l+1:r]

        retval = ''
        for i in range(N):
            retval = max(retval, expand(i, i), expand(i, i+1), key=len)
        return retval
