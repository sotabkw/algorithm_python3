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


def isSumEqual(self, firstWord: str, secondWord: str, targetWord: str) -> bool:
    d = {
        'a': '0', 'b': '1', 'c': '2',
        'd': '3', 'e': '4', 'f': '5',
        'g': '6', 'h': '7', 'i': '8',
        'j': '9'
    }
    lst1 = []
    lst2 = []
    lst3 = []
    for i in firstWord:
        x = d.get(i)
        lst1.append(x)
    firstNum = int(''.join(lst1))

    for j in secondWord:
        y = d.get(j)
        lst2.append(y)
    secondNum = int(''.join(lst2))

    for k in targetWord:
        z = d.get(k)
        lst3.append(z)
    targetNum = int(''.join(lst3))

    result = firstNum + secondNum

    if result == targetNum:
        return True
    else:
        return False


def isSumEqual(self, firstWord: str, secondWord: str, targetWord: str) -> bool:
    str1 = ""
    for i in firstWord:
        str1 += str(ord(i)-ord('a'))

    str2 = ""
    for i in secondWord:
        str2 += str(ord(i)-ord('a'))

    target_str = ""
    for i in targetWord:
        target_str += str(ord(i)-ord('a'))

    if int(str1)+int(str2) == int(target_str):
        return True
    return False
