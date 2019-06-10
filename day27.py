#!/usr/bin/env python3
"""Problem - Day 27
Given a string of round, curly, and square open and closing brackets, return whether the brackets are balanced (well-formed).
For example, given the string "([])[]({})", you should return true.
Given the string "([)]" or "((()", you should return false.
"""
OPENERS = ['(', '{', '[']
CLOSERS = [')', '}', ']']
BRACKETS = {o: c for o, c in zip(OPENERS, CLOSERS)}


def isWellFormed(s, passback=False):
    if s == '':
        return True
    try:
        if BRACKETS[s[0]] == s[1]:
            return isWellFormed(s[2:], passback)
    except KeyError:
        pass
    if s[0] in OPENERS and s[1] in OPENERS:
        holder = s[0]
        try:
            holder += isWellFormed(s[1:], True)
        except TypeError:
            return False
        return isWellFormed(holder, passback)
    if s[0] in CLOSERS and passback:
        return s
    return False


def main():
    s1 = '()'
    s2 = '{}'
    s3 = '[]'
    assert isWellFormed(s1)
    assert isWellFormed(s2)
    assert isWellFormed(s3)

    s4 = '(){}[]'
    assert isWellFormed(s4)

    s5 = ')'
    assert not isWellFormed(s5)

    s6 = '([{}])'
    assert isWellFormed(s6)

    s7 = '([)]'
    assert not isWellFormed(s7)

    s8 = '({[[{[()[{}]](({}[]{})({}[]{}))[[][]]}]]((())(()))})'
    assert isWellFormed(s8)

    s9 = '({[[{[()[{}]](({}[]{})({}[]{})))[[][]]}]]((())(()))})'
    assert not isWellFormed(s9)


if __name__ == '__main__':
    main()

