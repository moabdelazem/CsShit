""" 
Given two strings s and t, return true if t is an anagram of s, and false otherwise.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

 

Example 1:

Input: s = "anagram", t = "nagaram"
Output: true
Example 2:

Input: s = "rat", t = "car"
Output: false

"""

def validAnagram(s, t):
    # Using HashMaps

    # if len(s) != len(t):
    #     return False

    # countS, countT = {}, {}

    # for i in range(len(s)):
    #     countS[s[i]] = 1 + countS.get(s[i], 0)
    #     countT[t[i]] = 1 + countT.get(t[i], 0)

    # for c in countS:
    #     if countS[c] != countT.get(c, 0):
    #         return False
    # return True 

    # One Way Soultion
    return sorted(s) == sorted(t)
    

print(validAnagram("anagram", "nagaram"))
print(validAnagram("rat", "car"))
print(validAnagram("a", "ab"))
