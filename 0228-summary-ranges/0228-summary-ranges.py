class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        output = []
        i= 0
        while i<len(nums):
            if i == len(nums)-1:
                output.append(f"{str(nums[i])}")
                break   
            if nums[i]!=nums[i+1]-1:
                output.append(f"{str(nums[i])}")     
            else:
                first =  nums[i]
                if i + 1 == len(nums)-1:
                    last = nums[i+1]
                    output.append(f"{str(first)}->{str(last)}")
                    break    
                while nums[i]==nums[i+1]-1 :
                    if i+1 == len(nums)-1:
                        last = nums[i+1]
                        output.append(f"{str(first)}->{str(last)}")
                        return output
                    i+=1
                else:
                    last = nums[i]
                    output.append(f"{str(first)}->{str(last)}")
            i+=1
        return output
