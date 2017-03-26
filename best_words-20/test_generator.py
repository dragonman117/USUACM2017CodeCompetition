from random import randint

def random_letter(_):
    chars = 'abcdefghi'
    return chars[randint(0, len(chars) - 1)]

def random_word(size):
    return "".join(map(random_letter, range(size)))

def generateWords(n, size):
    for x in range(n):
        yield random_word(size)

def generateSong(n, size):
    for word in generateWords(n, size):
        print(word)

def generateAlbum():
    num_tracks = 100
    n = 20000
    word_size = 5

    print(num_tracks)
    for _ in range(num_tracks):
        print(n)
        generateSong(n, word_size)

def analyze():
    words = {}

    input()
    for _ in range(int(input())):
        w = input()
        if w in words:
            words[w] += 1
        else:
            words[w] = 1

    for w in sorted(words, key=words.get):
        print(w, words[w])


if __name__ == "__main__":
    generateAlbum()
    #analyze()
