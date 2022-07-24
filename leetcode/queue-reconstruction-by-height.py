class Solution:
    def reconstructQueue(self, people: list[list[int]]) -> list[list[int]]:
        people.sort(key=lambda x:(-x[0], x[1]))
        answer = []
        for (height, k) in people:
            answer.insert(k, [height, k])
        return answer