

class Trie:
  def __init__(self):
      # we defie a map which will help us trace word. Currently it has only * denoting the beginning of trie
    self.root = {"*":"*"}

  def add_word(self, word):
      #Place a pointer called curr_node. Since this is a reference and not copy, any change you make to it reflects in root
    curr_node = self.root 
    #go over each letter, add it in the value of map
    for letter in word:
      if letter not in curr_node:
        curr_node[letter] = {}
    #Look at result below. Once you add w, you need to go to its value to add a map with key 'a'
      curr_node = curr_node[letter]
    #all letters added. now add * to final value of map as a dictionary. This denotes word is completed. Remember trie diagram
    curr_node["*"] = "*"
    
    ''' This is how it should look like once you add the word 'wait'
    self.root = {
    "*": "*",  # Root initialization.
    "w": {
        "a": {
            "i": {
                "t": {
                    "*": "*"  # Word "wait" is marked as complete here.
                }
            }
        }
    }
}
    '''
  
  def does_word_exist(self, word):
    curr_node = self.root
    #curr_node pointing back to root
    for letter in word:
        #If letter not a key in original map, return False
      if letter not in curr_node:
        return False
      # Say w found. No go to its value to find 'a' in next iteration. So update pointer    
      curr_node = curr_node[letter]
    #word completed. Now we should be left with only * at the end for the word to be completed
    #check if * in curr_node return True else return False
    return "*" in curr_node



trie = Trie()
words = ["wait", "waiter", "shop", "shopper"]
for word in words:
  trie.add_word(word)

print(trie.does_word_exist("wait")) #True
print(trie.does_word_exist("")) #True
print(trie.does_word_exist("waite")) #False
print(trie.does_word_exist("shop")) #True
print(trie.does_word_exist("shoppp")) #False