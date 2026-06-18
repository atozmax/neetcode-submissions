class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        len_s = len(s)
        len_t = len(t)
        if len_s != len_t:
            return False
        
        ch_hash_map = {}

        for ch in s:
            if ch not in ch_hash_map:
                ch_hash_map[ch] = 1
            else:
                ch_hash_map[ch] = ch_hash_map[ch] +1

        for ch_2 in t:
            if ch_2 not in ch_hash_map:
                return False
            else:
                if ch_hash_map[ch_2]<=0:
                    return False
                
                ch_hash_map[ch_2] = ch_hash_map[ch_2] - 1
        
        for v in ch_hash_map.values():
            if v>0:
                return False
        return True
