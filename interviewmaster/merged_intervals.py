from typing import List, Sequence


class Solution:

    def merge_intervals(self, intervals: List[List[int]]) -> List[List[int]]:

        intervals.sort()
        merged: List[List[int]] = [intervals[0]]

        for start, end in intervals:
            last_end = merged[-1][1]
            
            if start <= last_end: # overlapping case
                merged[-1][1] = max(end, last_end) # last_merged.end = max(current.end, last_merged.end)
            else:
                merged.append([start, end])
        return merged




nums = [1, 4, 59, 4]
nums1 = [[1,3], [15,18], [2,6],[8,10]]
last_element = nums1[-1]
nums.sort()
nums1.sort(key=lambda x: x[1])
print(nums)
print(nums1)
print(last_element[1])