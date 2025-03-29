from typing import List


class Solution:

    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        if not strs:
            return []
        
        if len(strs) == 1:
            return [strs]
        
        result = {}
        for str in strs:
            sorted_str = "".join(sorted(str))
            if sorted_str not in result:
                result[sorted_str] = []
                result[sorted_str].append(str)
            else:
                result[sorted_str].append(str)
        return list(result.values())