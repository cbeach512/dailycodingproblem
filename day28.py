#!/usr/bin/env python3
"""Problem - Day 28
Write an algorithm to justify text. Given a sequence of words and an integer line length k, return a list of strings which represents each line, fully justified.
More specifically, you should have as many words as possible in each line. There should be at least one space between each word. Pad extra spaces when necessary so that each line has exactly length k. Spaces should be distributed as equally as possible, with the extra spaces, if any, distributed starting from the left.
If you can only fit one word on a line, then you should pad the right-hand side with spaces.
Each word is guaranteed not to be longer than k.
For example, given the list of words ["the", "quick", "brown", "fox", "jumps", "over", "the", "lazy", "dog"] and k = 16, you should return the following:
    ["the  quick brown", # 1 extra space on the left
    "fox  jumps  over", # 2 extra spaces distributed evenly
    "the   lazy   dog"] # 4 extra spaces distributed evenly
"""
def append_line(k, members):
    members_num = len(members)
    if members_num == 1:
        tail_buffer = k - len(members[0])
        return members[0] + ' ' * tail_buffer
    members_len = sum(len(i) for i in members)
    min_buffer = (k - members_len) // (members_num - 1)
    extra_buffer = k - members_len - min_buffer * (members_num - 1)
    line_buffer = ' ' * min_buffer
    line_str = ''
    for member in enumerate(members):
        if member[0] > extra_buffer:
            current_buffer = line_buffer
        else:
            current_buffer = line_buffer + ' '
        if line_str == '':
            line_str = member[1]
        else:
            line_str += current_buffer + member[1]
    return line_str



def tj(l, k):
    lines = []
    current_line_members = []
    current_len = 0
    for word in l:
        if current_len == 0:
            current_len += len(word)
            current_line_members.append(word)
        elif current_len + len(word) + 1 <= k:
            current_len += len(word) + 1
            current_line_members.append(word)
        else:
            lines.append(append_line(k, current_line_members))
            current_len = len(word)
            current_line_members = [word]
    lines.append(append_line(k, current_line_members))
    return lines


def main():
    l1 = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
          'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    k1 = 5
    assert tj(l1, k1) == ['a b c', 'd e f', 'g h i', 'j k l', 'm n o', 'p q r', 's t u', 'v w x', 'y   z']

    l2 = ['the', 'quick', 'brown', 'fox', 'jumps', 'over', 'the', 'lazy', 'dog']
    k2 = 16
    assert tj(l2, k2) == ['the  quick brown', 'fox  jumps  over', 'the   lazy   dog']


    l3 = ['one', 'two', 'three']
    k3 = 7
    assert tj(l3, k3) == ['one two', 'three  ']


if __name__ == '__main__':
    main()

