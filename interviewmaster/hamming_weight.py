class Solution:

    def hamming_weight(self, num: int) -> int:
        """
        docstring
        """
        count = 0
        while num:
            if num & 1 == 1:
                count += 1
            num = num // 2 
            # or we can write like num = numm >> 1
        return count
    

    def hamming_weight1(self, num):
        """
        docstring
        """
        pass
        count = 0
        while num:
            if num & 1 == 1:
                count += 1
            num = num // 2
        return count

if __name__ == "__main__":
    sol = Solution()
    print(sol.hamming_weight(9))