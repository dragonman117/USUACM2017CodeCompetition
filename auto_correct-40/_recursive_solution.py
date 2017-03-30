def alphabet():
    return 'abcdefghijklmnopqrstuvwxyz'

def mutate_insert(word, index, char):
    return word[:index] + char + word[index:]
def generate_insert_words(word):
    for char in alphabet():
        for index in range(len(word) + 1):
            yield mutate_insert(word, index, char)

def mutate_remove(word, index):
    return word[:index] + word[index+1:]
def generate_remove_words(word):
    return map(lambda i: mutate_remove(word, i), range(len(word)))

def mutate_swap(word, index, char):
    return word[:index] + char + word[index+1:]
def generate_swap_words(word):
    for char in alphabet():
        for index in range(len(word)):
            yield mutate_swap(word, index, char)

class Spell_Checker:
    def __init__(self):
        self.words = {}
        self.mutators = [generate_swap_words, generate_remove_words, generate_insert_words]

    def add_word(self, word):
        self.words[word] = True

    def spell_check(self, word):
        if word in self.words:
            return "CORRECT"
        else:
            return self.__check_for_edit_words(word)

    def __check_for_edit_words(self, word):
        check = {}
        for m in self.mutators:
            for x in m(word):
                check[x] = True

        suggestions = [w for w in check if w in self.words]

        if len(suggestions) == 1:
            return "YES " + suggestions[0]
        elif len(suggestions) > 1:
            return "NO " + " ".join(sorted(suggestions))
        else:
            suggestions = {}
            for w in check:
                for m in self.mutators:
                    for x in m(w):
                        if x in self.words:
                            suggestions[x] = True


            if len(suggestions) == 1:
                return "YES " + list(suggestions)[0]
            elif len(suggestions) > 1:
                return "NO " + " ".join(sorted(suggestions))
            else:
                return "NO"


if __name__ == "__main__":
    n, k = map(int, input().split())

    checker = Spell_Checker()
    for _ in range(n):
        checker.add_word(input())
    for _ in range(k):
        print(checker.spell_check(input()))
