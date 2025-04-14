class Solution:

    def lengthOfLongestSubString(self, s: str) -> int:
        
        if len(s) == 1:
            return len(s)
        if len(s) == len(set(s)):
            return len(s)      
        char_set = set()
        left = 0
        max_length = 0

        for right in range(len(s)):
            while s[right] in char_set:
                char_set.remove(s[left])
                left += 1
        
            char_set.add(s[right])
            max_length = max(max_length, right - left + 1)
        return max_length
       
    
    def lengthOfLongestSubString(self, s: str) -> str:

        char_set = set() # storing values in sliding window
        left = 0
        str_start_index = 0
        max_length = 0

        for right, char in enumerate(s):
            while char in char_set:
                char_set.remove(char)
                left += 1

                char_set.add(char)

                if right - left + 1 > max_length:
                    max_length = right - left + 1
                    str_start_index = left
                
        longest_sub_string = s[str_start_index:str_start_index+max_length]
        return longest_sub_string








s = Solution()
print(s.lengthOfLongestSubString("abcabcbb"))
print(s.lengthOfLongestSubString("bbbbb"))
print(s.lengthOfLongestSubString("pwwkew"))
print(s.lengthOfLongestSubString("au"))
print(s.lengthOfLongestSubString("ckilbkd"))
print(s.lengthOfLongestSubString("aab"))

d = "abc"
print(d[1:2])