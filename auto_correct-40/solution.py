def edit_distance(wordi, wordj, less_than):
    '''
    Find the edit distance between wordi and wordj
    return less_than if the edit distance is greater than or equal to less_than
    '''
    if len(wordi) < len(wordj):
        wordi, wordj = wordj, wordi

    e0 = range(len(wordj))
    e = []
    def num_edits(i, j):
        edits = min(
            i+1 if j == 0 else e[j-1],
            i if j == 0 else e0[j-1],
            e0[j]
        )
        return edits if wordi[i] == wordj[j] else edits + 1

    for i in range(len(wordi)):
        is_less_than = False
        for j in range(len(wordj)):
            e.append(num_edits(i, j))
            if e[-1] < less_than:
                is_less_than = True
            if e[-1] == -1:
                print(e0, e)
        if not less_than:
            return less_than
        else:
            e0 = e
            e = []

    return e0[-1]

class Spell_Checker:
    def __init__(self):
        self.words = {}

    def add_word(self, word):
        self.words[word] = True

    def spell_check(self, word):
        if self.is_a_word(word):
            return "CORRECT"
        else:
            max_edit_distance = 2

            edits = list(map(lambda w: (w, edit_distance(word, w, max_edit_distance)), self.words)) # get tuples of all words with their edit distances
            m = min(edits, key=lambda tup: tup[1])[1] # find the shortest edit distance

            if m == max_edit_distance:
                return "NO"

            suggestions = list(map(lambda tup: tup[0], filter(lambda tup: tup[1] == m, edits))) # get the words with the shortest edit distance

            if len(suggestions) == 1:
                return "YES " + suggestions[0]
            else:
                return "NO " + " ".join(suggestions)


    def is_a_word(self, word):
        return word in self.words

if __name__ == "__main__":
    n, k = map(int, input().split())

    checker = Spell_Checker()
    for _ in range(n):
        checker.add_word(input())
    for _ in range(k):
        print(checker.spell_check(input()))
