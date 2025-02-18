from typing import List


def reverse_string(s: List[str]) -> None:
    left: int = 0
    right: int = len(s) - 1

    while left < right:
        s[left], s[right] = s[right], s[left]
        left += 1
        right -= 1 
    print(s)

reverse_string(['n', 'a', 'v', 'a'])