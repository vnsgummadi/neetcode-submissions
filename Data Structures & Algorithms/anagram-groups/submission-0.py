from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hash = {}
        for i,s in enumerate(strs):
            fre = [0]*26

            for j in s:
                fre[ord(j) - ord('a')] +=1

            key = tuple(fre)
            if key not in hash:
                hash[key] = []
            hash[key].append(s)

        return sorted(hash.values())





