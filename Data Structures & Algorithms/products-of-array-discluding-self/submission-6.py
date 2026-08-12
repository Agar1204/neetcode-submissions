class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        has_zero = False
        product = 1
        res = []
        for num in nums:
            if num == 0 and has_zero == False:
                has_zero = True
                continue
            product *= num
        
        for num in nums:
            if has_zero == False:
                res.append(int(product / num))
            else:
                if num == 0:
                    res.append(int(product))
                else:
                    res.append(0)
        return res
        
        
        