def is_anagram(s: str, t: str) -> bool:
    result = {}
    for char in s:
        if char in result:
            result[char] += 1
        else:
            result[char] = 1
    for char in t:
        if char in result:
            result[char] -= 1
        else:
            return False
    r, = set(result.values())
    print(r)
    return r == 0



def is_anagram1(s: str, t: str) -> bool:
    if len(s) != len(t):
        return False
    counter = {}
    for char in s:
        counter[char] = counter.get(char, 0) + 1
    for char in t:
        if char not in counter or counter[char] == 0:
            return False
        else:
            counter[char] -= 1
    return True

is_anagram("anagram", "nagaram")