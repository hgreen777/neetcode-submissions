class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums.sort()
        current_longest = 0
        current_run = 0
        next_num = 0
        for i, n in enumerate(nums):
            if i==0:
                next_num = n+1
                current_longest = 1
                current_run = 1
            else:
                if n == next_num:
                    current_run+=1
                    current_longest = max(current_longest, current_run)
                elif n == next_num-1:
                    continue
                else:
                    current_run = 1
                next_num = n+1
        return current_longest