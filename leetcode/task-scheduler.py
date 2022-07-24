from collections import Counter


class Solution:
    def leastInterval(self, tasks: list[str], n: int) -> int:
        counter, retval = Counter(tasks), 0
        while True:
            temp = len(counter)
            for (task, cnt) in counter.most_common(n + 1):
                counter.subtract(task)
                counter += Counter()

            if not counter:
                retval += temp
                break
            retval += n + 1
        return retval
