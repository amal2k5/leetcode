class Solution:
    def sortArrayByParityII(self, nums: List[int]) -> List[int]:

        even_index = 0
        odd_index = 1
        n = len(nums)
        zero_arr = [0] * n

        for num in nums:
            if num % 2 == 0:
                zero_arr[even_index] = num
                even_index += 2
            else:
                zero_arr[odd_index] = num
                odd_index += 2
                
        return zero_arr        

                    



            

        