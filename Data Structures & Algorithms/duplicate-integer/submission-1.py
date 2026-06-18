class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        repeateds = {}
        for e in nums:
            if str(e) in repeateds:
                return True
            
            repeateds[str(e)] = True
        return False