class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        num_frequency = {}
        
        for n in nums:
            if n not in num_frequency:
                num_frequency[n] = {"number":n, "frequency":1}
            else:
                num_frequency[n]["frequency"] += 1
        
        frequency_list = list(num_frequency.values())
        frequency_list.sort(key=lambda x:x["frequency"])

        return list(map(lambda x : x['number'], frequency_list[-k:]))
