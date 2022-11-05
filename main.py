
import gridClass
import Trie


if __name__ == '__main__':
    tryme = Trie.Trie()
    dictionary = open("words.txt", "r")
    fit = dictionary.readlines()
    dictionary.close()
    for x in fit:
        x = x.replace('\n', '')
        x = x.lower()
        tryme.insert(x)

    f = open('test.txt')
    listy = f.readlines()
    f.close()
    actualList = []
    Grid = gridClass.gridClass(listy,tryme)
    for x in range(len(Grid.listy)):
        for y in range(len(Grid.listy[0])):
            Grid.searchGrid(x,y)
    for word in range(len(Grid.words)):
        if (tryme.find(Grid.words[word]) and len(Grid.words[word])>4):
            actualList.append(Grid.words[word])
    actualList = list(dict.fromkeys(actualList))
    print(actualList)

