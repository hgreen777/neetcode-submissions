class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        expected_result = {}
        for i, a in enumerate(nums):
            # Check if the expected result is current
            if a in expected_result:
                return [expected_result[a], i]
            
            # Add expected result to current 
            exp = target - a
            expected_result[exp] = i
