class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash_map = {
        }

        for index, n in enumerate(nums):
            pair_n = target - n                

            if pair_n in hash_map:
                return [hash_map[pair_n], index]
            else:
                hash_map[n] = index

        return []