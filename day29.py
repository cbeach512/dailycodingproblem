#!/usr/bin/env python3
"""Problem - Day 29
Run-length encoding is a fast and simple method of encoding strings. The basic idea is to represent repeated successive characters as a single count and character. For example, the string "AAAABBBCCDAA" would be encoded as "4A3B2C1D2A".
Implement run-length encoding and decoding. You can assume the string to be encoded have no digits and consists solely of alphabetic characters. You can assume the string to be decoded is valid.
"""
def encode(s, chain=None, count=0, prev=None):
    if s == '':
        chain.append('{}{}'.format(count, prev))
        return ''.join(chain)
    current = s[0]
    if not prev:
        chain = list()
        prev = current
    if current == prev:
        count += 1
        return encode(s[1:], chain, count, current)
    else:
        chain.append('{}{}'.format(count, prev))
        count = 1
        return encode(s[1:], chain, count, current)


def decode(e, chain=None):
    if e == '':
        return ''.join(chain)
    if not chain:
        chain = list()
    chain.append(e[1] * int(e[0]))
    return decode(e[2:], chain)


def main():
    s1 = 'AAAABBBCCDAA'
    e1 = '4A3B2C1D2A'
    assert encode(s1) == e1
    assert decode(e1) == s1

    s2 = 'KKKKKKYYYYYYYBFFFFFFFFFJJJJJQQQQDDKKKKKKTTTGGGGGGGG'
    e2 = '6K7Y1B9F5J4Q2D6K3T8G'
    assert encode(s2) == e2
    assert decode(e2) == s2


if __name__ == '__main__':
    main()

