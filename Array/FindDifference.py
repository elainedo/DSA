"""
Given two strings s and t which consist of only lowercase letters.

String t is generated by random shuffling string s and then add one more letter at a random position.

Find the letter that was added in t.

"""

def findTheDifference(s, t):
    charCode = 0
    for i in range(len(s)):
        charCode += ord(t[i])
        charCode -= ord(s[i])
    charCode += ord(t[-1])
    return chr(charCode)

print(findTheDifference("abc", "abcd"))