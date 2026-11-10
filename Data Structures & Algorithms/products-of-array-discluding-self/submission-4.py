class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        output = []
        prefix = 1 # Increases
        suffix = 1 # Decreases
        previous_num = 1
        zeroes = []
        for i,n in enumerate(nums):
            if n != 0:
                suffix *= n
            else:
                zeroes.append(i)

        z_len = len(zeroes)
        if z_len > 1:
            return [0] * len(nums)
        
        for i, current_num in enumerate(nums):
            if i in zeroes or z_len == 0:
                prefix *= previous_num
                suffix /= (
                    current_num
                    if current_num != 0
                    else 1
                )
                output.append(int(prefix * suffix))

                previous_num = current_num
            else:
                output.append(0)

        return output
        