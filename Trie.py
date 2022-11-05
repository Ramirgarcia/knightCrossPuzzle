

class Trie:
    def __init__(self):
        keyList = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u', 'v', 'w','x','y','z',' ',
                   '0','1','2','3','4','5','6','7','8','9']
        self.data = {}
        for i in keyList:
            self.data[i] = None
        self.word = 'N'
        self.contain = ''


    def insert(self, rw = None, orig = None):
        if rw is None or rw == '':
            self.word = 'Y'
        else:
            c = rw[0]
            w = rw[1:]
            if self.data[c] is not None:
                self.data[c].insert(w, orig)
            else:
                self.data[c] = Trie()
                self.data[c].contain = self.contain + c
                self.data[c].insert(w,orig)


    def find(self, word):
        if self is None:
            return False
        elif word == "":
            if self.word == "Y":
                return True
            else:
                return False
        else:
            c = word[0]
            w = word.replace(word[0], '', 1)
            if self.data[c] is not None:
                return self.data[c].find(w)
            return False

    def pref(self,x):
        tmp = self
        for i in range(len(x)):
            if (tmp.data[x[i]] is not None):
                tmp = tmp.data[x[i]]
            else:
                return False
        return True






