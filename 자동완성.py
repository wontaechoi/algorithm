class Node():
    def __init__(self, key, data=''):
        self.key = key
        self.data = [data]
        self.children = {}


class Trie:
    def __init__(self):
        self.head = Node(None)

    def insert(self, string):
        current = self.head
        for c in string:
            if c in current.children:
                current = current.children[c]
                current.data.append(string)
            else:
                current.children[c] = Node(c, string)
                current = current.children[c]

    def find(self, word):
        current = self.head
        count = 0
        for c in word:
            current = current.children[c]
            count += 1
            if len(current.data) == 1 and current.data[0] == word:
                break
        return count


def solution(words):
    trie = Trie()
    for word in words:
        trie.insert(word)
    answer = 0
    for word in words:
        answer += trie.find(word)
    return answer