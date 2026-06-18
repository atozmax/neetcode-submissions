class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        repeateds = {}
        for e in nums:
            if e in repeateds:
                return True
            else:
                repeateds[e] = True
        return False