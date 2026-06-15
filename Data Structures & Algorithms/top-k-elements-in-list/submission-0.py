class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hash = {}
        for i in nums:
            if i in hash:
                hash[i] +=1
            else:
                hash[i] = 1
        result = []
        for i in range(k):
            max1 = max(hash, key = hash.get)
            del hash[max1]
            result.append(max1)
        return result

