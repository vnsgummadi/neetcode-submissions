class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
       
        mp = {}
        for i in range(len(nums)):
            dif = target-nums[i]
            if dif in mp:
                return [mp[dif],i]
            mp[nums[i]] = i
        