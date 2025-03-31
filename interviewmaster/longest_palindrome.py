class Solution:

    def expand_from_center(self, s: str, left: int, right: int) -> str:
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1
        return s[left + 1:right]
    
    def longest_palindrome(self, s: str):
        if not s or len(s) == 1:
            return s
        
        longest = ""

        for i in range(len(s)):
            odd_palindrome = self.expand_from_center(s, i, i)
            even_palindrome = self.expand_from_center(s, i, i+1)

            if len(odd_palindrome) > len(longest):
                longest = odd_palindrome
            
            if len(even_palindrome) > len(longest):
                longest = even_palindrome
        return longest

sl = Solution()
print(sl.longest_palindrome("babad"))