#!/usr/bin/env python3
"""Problem - Day 25
Implement regular expression matching with the following special characters:
- . (period) which matches any single character
- * (asterisk) which matches zero or more of the preceding element
That is, implement a function that takes in a string and a valid regular expression and returns whether or not the string matches the regular expression.
For example, given the regular expression "ra." and the string "ray", your function should return true. The same regular expression on the string "raymond" should return false.
Given the regular expression ".*at" and the string "chat", your function should return true. The same regular expression on the string "chats" should return false.
"""
def match_it(s, m):
    """Checks if a string matches a formatted string.

    The formatted string can contain 2 special characters:
        . (wildcard): will match any character
        * (optional/repeating): preceeding character occurs 0 or more times

    Parameters:
        s (str): String to be checked
        m (str): Formatted string to check against

    Returns:
        bool: True if s matches m
    """
    try:
        # detect if current character is optional/repeating
        if m[1] == '*':
            asterisk = True
        else:
            asterisk = False
    # occurs if at the end of the formatted string
    except IndexError:
        asterisk = False
    try:
        # does the current character match
        if m[0] in [s[0], '.']:
            # is the character repeating
            if asterisk:
                # branch
                return match_it(s[1:], m[2:]) or match_it(s[1:], m)
            else:
                # next
                return match_it(s[1:], m[1:])
        # continue if character was optional
        elif asterisk:
            return match_it(s, m[2:])
    # occurs if at the end of the strings
    except IndexError:
        # end of both stings, everything matched, return true
        if len(m) == 0 == len(s):
            return True
        # end of sting and last match is optional, return true
        elif asterisk and len(m) == 2 and len(s) == 0:
            return True
    # a character didn't match, return false
    return False


def main():
    s1 = 'ray'
    s2 = 'raymond'
    m1 = 'ra.'
    assert match_it(s1, m1)
    assert not match_it(s2, m1)

    s3 = 'chat'
    s4 = 'chats'
    m2 = '.*at'
    assert match_it(s3, m2)
    assert not match_it(s4, m2)

    s5 = 'same'
    s6 = 'not'
    s7 = 'sam'
    m3 = 'same'
    assert match_it(s5, m3)
    assert not match_it(s6, m3)
    assert not match_it(s7, m3)

    s8 = 'wild'
    m4 = '.il.'
    assert match_it(s8, m4)

    s9 = 'aaa'
    m5 = 'a*'
    assert match_it(s9, m5)

    s10 = 'yes'
    m6 = 'n*yes'
    assert match_it(s10, m6)

    s11 = 'thisshouldpass'
    m7 = '.his*hog*uld.*'
    assert match_it(s11, m7)


if __name__ == '__main__':
    main()

