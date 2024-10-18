class WordDictionary:

    def __init__(self):
        self.root = {'*':'*'}

    def addWord(self, word: str) -> None:
        curr_node = self.root
        for letter in word:
            if letter not in curr_node:
                curr_node[letter] = {}
            curr_node = curr_node[letter]
        curr_node['*'] = '*'
        print("word added:",word)

    def search(self, word: str) -> bool:
        return self.rec(word, self.root)

    def rec(self,word, curr_node):
            if word == "":
                if '*' in curr_node:
                    return True
                else:
                    return False
            letter = word[0]
            if letter!= '.' and letter not in curr_node:
                return False
            elif letter!= '.':
                return self.rec(word[1:],curr_node[letter])
            
            else:
                for key in curr_node:
                    if key!= '*' and self.rec(word[1:],curr_node[key]):
                        return True
                return False




# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)