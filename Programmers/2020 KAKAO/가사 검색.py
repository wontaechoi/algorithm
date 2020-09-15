class Node:
    def __init__(self, node):
        self.node = node
        self.data = {}
        self.children = {}


class Trie:
    def __init__(self, head=None):
        self.head = Node(head)

    def insert(self, string):
        current = self.head
        if len(string) not in current.data:
            current.data[len(string)] = 0
        current.data[len(string)] += 1
        for c in string:
            if c not in current.children:
                current.children[c] = Node(c)
                current.children[c].data[len(string)] = 1
            else:
                if len(string) not in current.children[c].data:
                    current.children[c].data[len(string)] = 0
                current.children[c].data[len(string)] += 1
            current = current.children[c]

    def search(self, string):
        alpha = string.split('?')[0]

        current = self.head
        for c in alpha:
            if c not in current.children:
                return 0
            current = current.children[c]
        if len(string) in current.data:
            return current.data[len(string)]
        return 0


def solution(words, queries):
    front = Trie()
    back = Trie()
    for word in words:
        front.insert(word)
        back.insert(word[::-1])
    answer = []

    for query in queries:
        if '?' * len(query) == query:
            if len(query) in front.head.data:
                answer.append(front.head.data[len(query)])
            else:
                answer.append(0)
        elif '?' == query[0]:
            answer.append(back.search(query[::-1]))
        else:
            answer.append(front.search(query))
    return answer