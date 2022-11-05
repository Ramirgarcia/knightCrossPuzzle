import Node
import Trie
class gridClass:
    def __init__(self,listy,dict):
        self.listy = []
        self.words = []
        self.dict = dict
        for line in range(len(listy)):
            self.listy.append([])
            for l in listy[line]:
                x = Node.Node(l.lower())
                self.listy[line].append(x)
            self.listy[line].pop()

    def searchGrid(self, x, y, z = ''):
        if not(x >= len(self.listy) or x < 0 or y<0 or y >= len(self.listy) or self.listy[x][y].visit == 1 ):

            z += self.listy[x][y].letter
            self.listy[x][y].stri = z
            if(self.dict.pref(self.listy[x][y].stri)):
                self.listy[x][y].visit = 1

                self.words.append(self.listy[x][y].stri)

                gridClass.searchGrid(self,x + 1, y + 2,z)
                self.listy[x][y].visit = 0
                gridClass.searchGrid(self,x - 1, y + 2,z)
                self.listy[x][y].visit = 0
                gridClass.searchGrid(self,x + 1, y - 2,z)
                self.listy[x][y].visit = 0
                gridClass.searchGrid(self,x - 1, y - 2,z)
                self.listy[x][y].visit = 0
                gridClass.searchGrid(self,x + 2, y + 1,z)
                self.listy[x][y].visit = 0
                gridClass.searchGrid(self,x + 2, y - 1,z)
                self.listy[x][y].visit = 0
                gridClass.searchGrid(self,x - 2, y + 1,z)
                self.listy[x][y].visit = 0
                gridClass.searchGrid(self,x - 2, y - 1,z)
                self.listy[x][y].visit = 0



