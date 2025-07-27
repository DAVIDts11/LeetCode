class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        i,j  = 0,(len(nums)-1)
        while True:
            if j==i+1 and nums[i]<target and nums[j]>target:
                return i+1
            if target == nums[i]:
                return i
            elif target == nums[j]:
                return j
            elif target >nums[j]:
                return j+1
            elif target < nums[i]:
                return 0
            elif  nums[(j+i)//2]>target:
                j = (j+i)//2
            elif nums[(j+i)//2]<target:
                i = (j+i)//2
            elif nums[(j+i)//2]==target:
                return (j+i)//2