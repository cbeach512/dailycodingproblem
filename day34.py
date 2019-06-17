#!/usr/bin/env python3
"""Problem - Day 34
Given a string, find the palindrome that can be made by inserting the fewest number of characters as possible anywhere in the word. If there is more than one palindrome of minimum length that can be made, return the lexicographically earliest one (the first one alphabetically).
For example, given the string "race", you should return "ecarace", since we can add three letters to it (which is the smallest amount to make a palindrome). There are seven other palindromes that can be made from "race" by adding three letters, but "ecarace" comes first alphabetically.
As another example, given the string "google", you should return "elgoogle".
"""
def palCheck(s):
    for i in range(len(s)//2):
        if s[i] != s[-i-1]:
            return False
    return True


def subPal(s):
    s_len = len(s)
    pals = list()
    start = 0
    end = s_len
    while end - start > 1:
        while end <= len(s):
            if palCheck(s[start:end]):
                pals.append((start, end))
            start += 1
            end += 1
        if pals:
            return pals
        end -= start + 1
        start = 0
    return pals


def getPal(s):
    if palCheck(s):
        return s
    s_len = len(s)
    sub_pals = subPal(s)
    offset = 1
    pal = str()
    if sub_pals:
        pals = list()
        for s_p in sub_pals:
            s_p_len = s_p[1] - s_p[0]
            if s_p[0] == 0:
                for l in range(s_len - s_p_len):
                    pal += s[s_p[1]:][-l-offset]
                pals.append(pal + s)
            elif s_p[1] == s_len:
                for l in range(s_len - s_p_len):
                    pal += s[:s_p[0]][-l-offset]
                pals.append(s + pal)
            else:
                pass
        return min(pals)
    elif min(s[0], s[-1]) == s[0]:
        offset += 1
    for l in range(s_len-1):
        pal += s[-l-offset]
    if offset == 1:
        return pal + s
    elif offset == 2:
        return s + pal
    else:
        pass


def main():
    s1 = 'race'
    assert getPal(s1) == 'ecarace'

    s2 = 'angle'
    assert getPal(s2) == 'anglelgna'

    s3 = 'google'
    assert getPal(s3) == 'elgoogle'

    s4 = 'elgoog'
    assert getPal(s4) == 'elgoogle'


if __name__ == '__main__':
    main()

