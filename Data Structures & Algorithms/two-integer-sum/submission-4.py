class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        if nums[0]+nums[1] == target:
            return [0,1]
        if nums[len(nums)-2]+nums[len(nums)-1] == target:
            return [len(nums)-2, len(nums)-1]
        mp = {}
        for i,n in enumerate(nums):
            dif = target-n
            if dif in mp:
                return [mp[dif],i]
            mp[n] = i
        