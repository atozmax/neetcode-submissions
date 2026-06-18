class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        repeateds = set()
        for e in nums:
            if e in repeateds:
                return True
            else:
                repeateds.add(e)
        return False