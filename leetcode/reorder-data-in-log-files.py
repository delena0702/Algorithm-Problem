class Solution:
    def reorderLogFiles(self, logs: list[str]) -> list[str]:
        let, dig = [], []
        for log in logs:
            if log.split()[1].isdigit():
                dig.append(log)
            else:
                let.append(log)
        let.sort(key=lambda x: (x.split()[1:], x.split()[0]))
        return let + dig