# Example 1:

# Input: firstWord = "acb", secondWord = "cba", targetWord = "cdb"
# Output: true
# Explanation:
# The numerical value of firstWord is "acb" -> "021" -> 21.
# The numerical value of secondWord is "cba" -> "210" -> 210.
# The numerical value of targetWord is "cdb" -> "231" -> 231.
# We return true because 21 + 210 == 231.
# Example 2:

# Input: firstWord = "aaa", secondWord = "a", targetWord = "aab"
# Output: false
# Explanation:
# The numerical value of firstWord is "aaa" -> "000" -> 0.
# The numerical value of secondWord is "a" -> "0" -> 0.
# The numerical value of targetWord is "aab" -> "001" -> 1.
# We return false because 0 + 0 != 1.
# Example 3:

# Input: firstWord = "aaa", secondWord = "a", targetWord = "aaaa"
# Output: true
# Explanation:
# The numerical value of firstWord is "aaa" -> "000" -> 0.
# The numerical value of secondWord is "a" -> "0" -> 0.
# The numerical value of targetWord is "aaaa" -> "0000" -> 0.
# We return true because 0 + 0 == 0.

class Solution:
    def isSumEqual(self, firstWord: str, secondWord: str, targetWord: str) -> bool:
        first = []
        second = []
        third = []
        alphabet = [chr(i) for i in range(97, 97+26)]

        for index in range(len(firstWord)):
            for i in range(len(alphabet)):
                if firstWord[index] == alphabet[i]:
                    first.append(i)
        if first[0] == "a":
            first.pop(0)

        for index in range(len(secondWord)):
            for i in range(len(alphabet)):
                if secondWord[index] == alphabet[i]:
                    second.append(i)
        if second[0] == "a":
            second.pop(0)

        for index in range(len(targetWord)):
            for i in range(len(alphabet)):
                if targetWord[index] == alphabet[i]:
                    third.append(i)
        if third[0] == "a":
            third.pop(0)

        return int("".join(map(str, first))) + int("".join(map(str, second))) == int("".join(map(str, third)))
