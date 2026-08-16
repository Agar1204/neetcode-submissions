class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        for i in range(m, n+m):
            nums1[i] = nums2[m-i]

        current = m
        while current < len(nums1):
            j = current - 1
            while j >= 0 and nums1[j+1] < nums1[j]:
                temp = nums1[j+1]
                nums1[j+1] = nums1[j]
                nums1[j] = temp
                j-=1
            current+=1
        


        