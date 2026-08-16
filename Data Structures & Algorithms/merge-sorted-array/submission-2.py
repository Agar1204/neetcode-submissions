class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        nums1_pointer = m-1
        nums2_pointer = n-1
        curr = m+n-1

        while nums1_pointer >= 0 and nums2_pointer >= 0:
            if nums2[nums2_pointer] > nums1[nums1_pointer]:
                nums1[curr] = nums2[nums2_pointer]
                curr-=1
                nums2_pointer-=1
            else:
                temp = nums1[curr]
                nums1[curr] = nums1[nums1_pointer]
                nums1[nums1_pointer] = temp
                curr-=1
                nums1_pointer-=1
        
        while nums2_pointer >= 0:
            nums1[curr] = nums2[nums2_pointer]
            nums2_pointer-=1
            curr-=1

        

        


        