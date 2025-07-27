class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count_dict = {}
        
        for num in nums:
            if num in count_dict:
                count_dict[num] +=1
            else:
                count_dict[num] =1
            
            if count_dict[num]>(len(nums)/2):
                break

        return num

