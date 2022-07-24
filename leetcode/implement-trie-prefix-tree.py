class Trie:
    def __init__(self):
        self.root = [False, {}]

    def insert(self, word: str) -> None:
        here = self.root
        for ch in word:
            if ch not in here[1]:
                here[1][ch] = [False, {}]
            here = here[1][ch]
        here[0] = True

    def search(self, word: str) -> bool:
        here = self.root
        for ch in word:
            if ch not in here[1]:
                return False
            here = here[1][ch]
        return here[0]

    def startsWith(self, prefix: str) -> bool:
        here = self.root
        for ch in prefix:
            if ch not in here[1]:
                return False
            here = here[1][ch]
        return True
