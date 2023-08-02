class trie_node:
    def __init__(self, char):
        self.char = char

        self.is_end = False

        self.counter = 0

        self.children = {}


class Trie:
    def __init__(self):
        self.root = trie_node("")

    def insert(self, word):
        cur_node = self.root
        for char in word:
            if char in cur_node.children:
                cur_node = cur_node.children[char]
            else:
                new_node = trie_node(char)
                cur_node.children[char] = new_node
                cur_node = new_node
        cur_node.is_end = True
        cur_node.counter += 1

    def dfs(self, cur_node, prefix):
        if cur_node.is_end:
            self.output.append((prefix + cur_node.char, cur_node.counter))
        for child in cur_node.children.values():
            self.dfs(child, prefix + cur_node.char)

    def query(self, x):
        self.output = []
        cur_node = self.root

        for char in x:
            if char in cur_node.children:
                cur_node = cur_node.children[char]
            else:
                return []

        self.dfs(cur_node, x[:-1])

        # return self.output
        return sorted(self.output, key = lambda x:x[1], reverse=True)

if __name__ == '__main__':
    t = Trie()
    t.insert("was")
    t.insert("what")
    t.insert("where")
    t.insert("wheres")
    print(t.query("wh"))

# https://albertauyeung.github.io/2020/06/15/python-trie.html/