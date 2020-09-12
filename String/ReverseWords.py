# reverse words in a sentence: "Alice likes Bob" becomes "Bob likes Alice"
def reverseWords(sentence):
    words = sentence.split(' ')
    reversed_sentence = ' '.join(reversed(words))
    return reversed_sentence

print(reverseWords('Alice likes Bobs'))