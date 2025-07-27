class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        p1 = 0 
        p2 = 0 

        while p2<n:
            if p1==m+p2:
                # nums1 = nums1[:p1] + nums2[p2:]
                # print("nums1[:p1] = ",nums1[:p1])
                # print("nums2[p2:] = ",nums2[p2:])
                while p2<n:
                    nums1.insert(p1,nums2[p2])
                    p1+=1
                    p2+=1

                print("nums1 = ",nums1)
                break

            if nums1[p1]<nums2[p2]:
                    p1+=1              
            else:
                nums1.insert(p1,nums2[p2])
                p1+=1
                p2+=1
        # nums1 = nums1[:(m+n)]
        while len(nums1)>m+n:
            nums1.pop()
        
        print("nums1 (right before return) = ",nums1)
        return