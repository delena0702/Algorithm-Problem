from collections import defaultdict


class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not t:
            return ""
        now, count = defaultdict(int), defaultdict(int)
        for ch in t:
            count[ch] += 1

        answer = ""
        l, r = 0, -1
        while True:
            isValid = True
            for (ch, cnt) in count.items():
                if now[ch] < cnt:
                    isValid = False
                    break

            if isValid:
                if not answer or r - l + 1 < len(answer):
                    answer = s[l:r+1]
                now[s[l]] -= 1
                l += 1

            else:
                if r + 1 == len(s):
                    break
                now[s[r + 1]] += 1
                r += 1
        return answer


print(Solution().minWindow(s="", t=""))
