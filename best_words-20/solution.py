# Pseudo-code for solution
'''
load the words for each speech:
  keep track of how many times each speech uses a word
find each speech's best word:
  iterate through each speech:
    check each word in that speech that no other speech uses:
      compare it with the current best word:
      if it's better (higher word count OR used the same and has higher lexicographical value):
        set the new best word
'''


# SOLUTION 2 - Refactored a bit
def solution2():
    # Load the words in each speech
    speech_count = int(input())
    words = {}
    for s in range(speech_count): # for each speech
        for _ in range(int(input())): # for each word in speech
            w = input()
            if w not in words:
                words[w] = {}
                words[w][s] = 1
            elif s not in words[w]:
                words[w][s] = 1
            else:
                words[w][s] += 1

    # Find each speech's best word
    for s in range(speech_count):
        best_word = ""
        best_word_count = 0
        words_only_is_this_speech = (w for w in words if s in words[w] and len(words[w]) == 1)
        for w in words_only_is_this_speech:
            if words[w][s] > best_word_count or words[w][s] == best_word_count and w > best_word:
                best_word = w
                best_word_count = words[w][s]
        if best_word == "":
            print("Track", s, "has no unique words")
        else:
            print("Track ", s, "'s best word is ", best_word, sep='')

# SOLUTION 1 - I find it a bit messy
def count_word(word, dic):
    if word in dic:
        dic[word] += 1
    else:
        dic[word] = 1
def solution1():
    # Load the speeches and keep track of all used words
    speeches = []
    used_words = {}
    for i in range(int(input())):
        speeches.append({})
        for _ in range(int(input())):
            word = input()
            count_word(word, speeches[i])
            count_word(word, used_words)

    # Find each speech's best word and print it
    for trackNo in range(len(speeches)):
        speech = speeches[trackNo]
        best_word = ""
        best_word_count = 0
        for w in speech:
            used_in_other_speech = False
            for s in speeches:
                if not s == speech and w in s:
                    used_in_other_speech = True
                    break;
            if not used_in_other_speech:
                if speech[w] > best_word_count:
                    best_word = w
                    best_word_count = speech[w]
                elif speech[w] == best_word_count and w > best_word:
                    best_word = w
                    best_word_count = speech[w]
        if best_word == "":
            print("Track", trackNo, "has no unique words")
        else:
            print("Track ", trackNo, "'s best word is ", best_word, sep='')

if __name__ == '__main__':
    solution2()
