class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result = {}
        sorted_strs = list(map(lambda x: "".join(sorted(x)), strs))    

        for index, sorted_str in  enumerate(sorted_strs):
            original_str = strs[index]
            if "".join(sorted(original_str)) == sorted_str:
                if sorted_str not in result:
                    result[sorted_str] = [original_str]
                else:
                    result[sorted_str].append(original_str)

        return list(result.values())    