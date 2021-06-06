class Solution:
    def romanToIntFirst(self, s):
        num = 0
        memo = {"I": 1,
                "V": 5,
                "X": 10,
                "L": 50,
                "C": 100,
                "D": 500,
                "M": 1000}
        num += memo[s[-1]]
        for i in range(len(s) - 2, -1, -1):
            if(memo[s[i]] < memo[s[i+1]]):
                num -= memo[s[i]]
                continue
            num += memo[s[i]]
        return num


def romanToIntSecond(self, s: str) -> int:
    # Mapping Roman letters to values
    mapp = {
        'I': '1',
        'V': '5',
        'X': '10',
        'L': '50',
        'C': '100',
        'D': '500',
        'M': '1000'
    }

    # Index, initially 0
    Idx = 0
    # Final result, initially 0
    final = 0

    while Idx < len(s):

        if Idx+1 < len(s) and int(mapp[s[Idx]]) < int(mapp[s[Idx+1]]):
            final += int(mapp[s[Idx+1]]) - int(mapp[s[Idx]])
            Idx += 2
        else:
            final += int(mapp[s[Idx]])
            Idx += 1

    return final


def romanToIntSecond(self, s: str) -> int:
    # Mapping Roman letters to values
    mapp = {
        'I': '1',
        'V': '5',
        'X': '10',
        'L': '50',
        'C': '100',
        'D': '500',
        'M': '1000'
    }

    # Index, initially 0
    Idx = 0
    # Final result, initially 0
    final = 0

    while Idx < len(s):

        if Idx+1 < len(s) and int(mapp[s[Idx]]) < int(mapp[s[Idx+1]]):
            final += int(mapp[s[Idx+1]]) - int(mapp[s[Idx]])
            Idx += 2
        else:
            final += int(mapp[s[Idx]])
            Idx += 1

    return final
