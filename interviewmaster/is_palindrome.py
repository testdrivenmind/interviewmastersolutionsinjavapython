from collections import deque


def is_palindrome(s: str) -> bool:
    left, right = 0, len(s) - 1
    while left < right:
        if not s[left].isalnum():
            left += 1
        elif not s[right].isalnum():
            right -= 1
        elif s[left].lower != s[right].lower():
            return False
        else:
            left += 1
            right -= 1
    return True


def is_palindrome1(s: str) -> bool:
    q = deque(s)
    while len(q) > 1:
        char_left = q.popleft()
        char_right = q.pop()

        if char_left.isalnum() and char_left.isalnum():
            if char_left != char_right:
                return False
        
    return True
