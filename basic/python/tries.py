class Trie():
    def __init__(self, children={}):
        self.isWord = False
        self.children = {}

    def print(self):
        stack = [self]
        while(len(stack) > 0):
            curr = stack.pop(0)
            if(curr.isWord):
                print('*')
            print(list(curr.children.keys()))
            stack.extend(list(curr.children.values()))

    def autocomplete(self, start:str):
        curr = self
        for i in range(len(start)):
            if(start[i] not in curr.children):
                return []
            curr = curr.children[start[i]]
        output = []
        _getListFromTrie(start, curr, output)
        return output


def _getListFromTrie(prefix:str, trie:Trie, output=[]):
    if trie:
        if trie.isWord:
            output.append(prefix)
        for key in trie.children:
            _getListFromTrie(prefix + str(key), trie.children[key], output)



def _buildTrie(listOfWords):
    trie = Trie({})
    for word in listOfWords:
        curr = trie
        for i in range(len(word)):
            if(word[i] not in curr.children):
                curr.children[word[i]] = Trie({})
            curr = curr.children[word[i]]
        curr.isWord = True

    return trie





inp = ["Abr", "Abraao", 'Abrd', 'Accd']
out =[]
a = _buildTrie(inp)

_getListFromTrie('', a, out)
# O()
print(a.autocomplete("Abr"))


23*20


