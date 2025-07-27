class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nums_dict = {}
        for index,value in enumerate(nums):
            if value in nums_dict and value* 2  == target:
                return [index,nums_dict[value]]

            else:
                nums_dict[value] = index

        for key,value in nums_dict.items():
            pair_value = (target - key) 
            if  pair_value in nums_dict and nums_dict[pair_value] != value:
                return [value,nums_dict[pair_value]]

        
        