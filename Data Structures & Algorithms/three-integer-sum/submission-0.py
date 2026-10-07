class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()  # Step 1: Sort array
        
        for i in range(len(nums)):
            # Skip positive starting numbers (impossible to sum to 0)
            if nums[i] > 0:
                break
                
            # Skip duplicate values for the first element
            if i > 0 and nums[i] == nums[i - 1]:
                continue
                
            # Step 2: Two-Pointer search for the remaining two numbers
            L, R = i + 1, len(nums) - 1
            while L < R:
                three_sum = nums[i] + nums[L] + nums[R]
                
                if three_sum > 0:
                    R -= 1
                elif three_sum < 0:
                    L += 1
                else:
                    res.append([nums[i], nums[L], nums[R]])
                    L += 1
                    R -= 1
                    
                    # Skip duplicate values for the second element
                    while L < R and nums[L] == nums[L - 1]:
                        L += 1
                        
        return res