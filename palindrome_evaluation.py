from typing import Dict


def TestPalindromeFunc():
    TestDict = {"blablabla": False, 
        "menem":True, 
        "example":False,
        "anna12321anna":True,
        "annaanna": True,
        "NeuqueN": True,
        "prueba": False,
        "Neuquen": False}
    
    for word, expected in TestDict.items():
        result = isPalindrome(word)
        if result != expected:
            print("function failed: word: {0}, expected: {1}, received: {2}".format(word, result, expected) )
        elif result == expected:
            print("fucntion worked ok for word {0}".format(word))
    return 

def isPalindrome(word):
    wordLength = len(word)
    lastCharPosition = wordLength -1
    for i in range(0, lastCharPosition//2):
        if word[i] != word[lastCharPosition-i]:
            return False
    return True

TestPalindromeFunc();
        