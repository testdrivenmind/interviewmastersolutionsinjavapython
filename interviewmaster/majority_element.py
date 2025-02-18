from typing import List


def majority_element(nums: List[int]) -> int:
    counter: dict = {}
    for num in nums:
        counter[num] = counter.get(num,0) + 1
    max_key = max(counter, key=counter.get)
    return max_key


my_dict = {"a": 10, "b": 25, "c": 15}
max_key, max_value = max(my_dict.items(), key=lambda item: item[1])
print(max_key, max_value)

def majority_element1(nums: List[int]) -> int:
    candidate: int = nums[0]
    count: int = 0
    for num in nums:
        if count == 0:
            candidate = num
        count += 1 if num == candidate else -1 
    return candidate

print(majority_element1([3, 2, 3]))