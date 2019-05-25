#!/usr/bin/env python3
"""Problem - Day 11
Implement an autocomplete system. That is, given a query string s and a set of all possible query strings, return all strings in the set that have s as a prefix.
For example, given the query string de and the set of strings [dog, deer, deal], return [deer, deal].
Hint: Try preprocessing the dictionary into a more efficient data structure to speed up queries.
"""
from timeit import timeit
from nltk.corpus import words
from time import time_ns

try:
    WORD_LIST = words.words()
except LookupError:
    import nltk
    nltk.download('words', quiet=True)
    WORD_LIST = words.words()

L1 = ['dog', 'deer', 'deal']

def debug(msg):
    print('DEBUG: {}'.format(msg))

class BruteForceAutoCompleter():
    def __init__(self, words):
        self.words = words

    def complete(self, letters):
        result = [word for word in self.words if word[:len(letters)] == letters]
        return result

class DictKeyAutoCompleter():
    _init_error = 'DictKeyAutoCompleter initialization: Type must be a string or list of strings'
    def __init__(self, words):
        if isinstance(words, list):
            for i in words:
                if not isinstance(i, str):
                    raise TypeError(self._init_error)
            self._words = words
        elif isinstance(words, str):
            self._words = words.split()
        else:
            raise TypeError(self._init_error)
        self._options = {}
        self._add_options()

    def _add_options(self):
        for word in self._words:
            self._add_option(word)

    def _add_option(self, word):
        for i in enumerate(word):
            try:
                self._options[word[:i[0]]].append(word)
            except KeyError:
                self._options[word[:i[0]]] = [word]

    def complete(self, letters):
        try:
            result = self._options[letters]
        except KeyError:
            result = []
        return result

BFACOMP = BruteForceAutoCompleter
A1 = BFACOMP(L1)

DKACOMP = DictKeyAutoCompleter
A2 = DKACOMP(L1)

if __name__ == '__main__':
    r1 = A1.complete('de')
    print('Result of brute force auto-complete: {}'.format(r1))
    it1 = timeit('a1 = BFACOMP(L1)', setup='from __main__ import L1, BFACOMP', number=100000)
    print('Brute force initialiaztion timing for 100000 runs = {}'.format(it1))
    ct1 = timeit("r1 = A1.complete('de')", setup='from __main__ import A1', number=100000)
    print('Brute force match timing for 100000 runs = {}\n'.format(ct1))

    r2 = A2.complete('de')
    print('Result of dictionary key auto-complete from list: {}'.format(r2))
    it2 = timeit('a2 = DKACOMP(L1)', setup='from __main__ import L1, DKACOMP', number=100000)
    print('Dictionary Key initialiaztion from list timing for 100000 runs = {}'.format(it2))
    ct2 = timeit("r2 = A2.complete('de')", setup='from __main__ import A2', number=100000)
    print('Dictionary Key match timing for 100000 runs = {}\n'.format(ct2))

    print('Lets do this with a real list of words!')
    print('Initializing brute force completer with a list of over 200000 words!')
    ta = time_ns()
    bfacomp = BFACOMP(WORD_LIST)
    tb = time_ns()
    print('    ** That took {} seconds! **'.format(((tb - ta) / 1e+9)))
    print('Finding matches for words starting with "deut"')
    ta = time_ns()
    r3 = bfacomp.complete('deut')
    tb = time_ns()
    print('    ** That took {} seconds! **'.format(((tb - ta) / 1e+9)))
    print('Result: {}\n'.format(r3))

    print('Ok, now lets initialize the dictionary key autocompleter with the same list')
    ta = time_ns()
    dkacomp = DKACOMP(WORD_LIST)
    tb = time_ns()
    print('    ** That took {} seconds! **'.format(((tb - ta) / 1e+9)))
    print('Finding matches for words starting with "deut"')
    ta = time_ns()
    r4 = dkacomp.complete('deut')
    tb = time_ns()
    print('    ** That took {} seconds! **'.format(((tb - ta) / 1e+9)))
    print('Result: {}\n'.format(r4))

