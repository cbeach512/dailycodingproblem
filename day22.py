#!/usr/bin/env python3
"""Problem - Day 22
Given a dictionary of words and a string made up of those words (no spaces), return the original sentence in a list. If there is more than one possible reconstruction, return any of them. If there is no possible reconstruction, then return null.
For example, given the set of words 'quick', 'brown', 'the', 'fox', and the string "thequickbrownfox", you should return ['the', 'quick', 'brown', 'fox'].
Given the set of words 'bed', 'bath', 'bedbath', 'and', 'beyond', and the string "bedbathandbeyond", return either ['bed', 'bath', 'and', 'beyond] or ['bedbath', 'and', 'beyond'].
"""
def findSentence(words, sentence, words_lens=None):
    if words_lens is None:
        words_lens = [(word, len(word)) for word in words]
    if sentence == '':
        return ''
    sentence_list = []
    for word in words_lens:
        if word[0] == sentence[:word[1]]:
            sentence_list.append(word[0])
            try:
                sentence_list.extend(findSentence(None, sentence[word[1]:], words_lens))
                return sentence_list
            except Exception:
                pass
    if words is None:
        raise Exception()
    else:
        return None


def main():
    l1 = ['quick', 'brown', 'the', 'fox']
    s1 = 'thequickbrownfox'
    print(findSentence(l1, s1))
    l2 = ['not', 'the', 'right', 'words']
    s2 = 'thiswillnotworkout'
    print(findSentence(l2, s2))
    l3 = [
        'temple', 'but', 'that', 'of', 'which', 'produced', 'arboreally',
        'corner', 'dresser', 'saw', 'as', 'boughs', 'toward', 'turned',
        'rainbow', 'cinema', 'passed', 'human', 'being', 'reflection', 'burst',
        'smile', 'and', 'across', 'white', 'mirrors', 'nature', 'head',
        'quick', 'those', 'involuntarily', 'because', 'from', 'were', 'the',
        'light', 'blindingly', 'unloaded', 'these', 'pharmacy', 'he',
        'parallelogram', 'rose', 'greet', 'with', 'facade', 'vacillation',
        'had', 'clear', 'we', 'or', 'vana', 'flawlessly', 'screen', 'swaying',
        'not', 'by', 'this', 'at', 'sky', 'sliding', 'gliding', 'his', 'who',
        'carrying', 'crossed', 'a', 'ricocheted'
    ]
    s3 = (
        'ashecrossedtowardthepharmacyatthecornerheinvoluntarilyturnedhisheadbe'
        'causeofaburstoflightthathadricochetedfromhistempleandsawwiththatquick'
        'smilewithwhichwegreetarainboworaroseablindinglywhiteparallelogramofsk'
        'ybeingunloadedfromthevanadresserwithmirrorsacrosswhichasacrossacinema'
        'screenpassedaflawlesslyclearreflectionofboughsslidingandswayingnotarb'
        'oreallybutwithahumanvacillationproducedbythenatureofthosewhowerecarry'
        'ingthisskytheseboughsthisglidingfacade'
    )
    print(findSentence(l3, s3))


if __name__ == '__main__':
    main()

