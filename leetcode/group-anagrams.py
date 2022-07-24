import collections

class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        anagram = collections.defaultdict(list)
        
        for word in strs:
            anagram[''.join(sorted(word))].append(word)
        return list(anagram.values())

print(Solution().groupAnagrams(strs = ["eat","tea","tan","ate","nat","bat"]))
