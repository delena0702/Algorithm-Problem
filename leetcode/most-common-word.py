import collections
import re

class Solution:
    def mostCommonWord(self, paragraph: str, banned: list[str]) -> str:
        words = re.sub('([^a-z]|\s)+', ' ', paragraph.lower()).split()
        words = list(filter(lambda x: x not in banned, words))
        counter = collections.Counter(words)
        return counter.most_common(1)[0][0]