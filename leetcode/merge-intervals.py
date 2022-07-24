class Solution:
    def merge(self, intervals: list[list[int]]) -> list[list[int]]:
        intervals.sort(key=lambda x: x[0])
        N = len(intervals)

        index = 0
        retval = []
        while index < N:
            (s, e) = intervals[index]

            index += 1
            while index < N:
                if e < intervals[index][0]:
                    break
                e = max(e, intervals[index][1])
                index += 1
            retval.append([s, e])
        return retval
