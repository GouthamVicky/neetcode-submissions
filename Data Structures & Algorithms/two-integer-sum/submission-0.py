class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash_set={}
        for i in range(len(nums)):
            compliment=target-nums[i]
            
            if compliment in hash_set:
                return [hash_set[compliment],i]
            else:
                hash_set[nums[i]]=i