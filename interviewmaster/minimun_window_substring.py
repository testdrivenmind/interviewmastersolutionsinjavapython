from collections import defaultdict


class Solution:

    def min_window(self, s: str, t: str) -> str:
        """
        Approach: 
            len(t) < len(s) return ""
            put the chars in a default dict with count againt each

        """
        if not s or not t or len(s) < len(t):
            return ""
            
        t_map = defaultdict(int)
        for char in t:
            t_map[char] += 1


        window = {}
        res = [-1, -1]
        res_len = float('inf') 
        have = 0
        need = len(t_map)
        left = 0


        for right in range(len(s)):
            char = s[right]
            window[char] = window.get(char, 0) + 1

            if char in t_map and t_map[char] == window[char]:
                have += 1            

            while have == need:
                if (right - left + 1) < res_len:
                    res = [left, right]
                    res_len = right - left + 1

                window[s[left]] -= 1
                if s[left] in t_map and window[s[left]] < t_map[s[left]]:
                    have -= 1

                left += 1
        
        l, r = res
        return s[l:r+1] if res_len != float('inf') else ""

sol = Solution()
print("ereir")
print(sol.min_window("ADOBECODEBANC", "ABC"))