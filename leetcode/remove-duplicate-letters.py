class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        for ch in sorted(set(s)):
            substr = s[s.index(ch):]
            if set(s) == set(substr):
                return ch + self.removeDuplicateLetters(substr.replace(ch, ''))
        return ''
