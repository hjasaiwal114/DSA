class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
         anagram = {}
         for s in strs:
              key = "".join(sorted(s))
              if key not in anagram