"""
>>> from pronounceable import PronounceableWord, generate_word, Pronounceablity, Complexity
>>> PronounceableWord().length(8, 15)
'terhtsadathe'
>>> generate_word()
'gloust'
>>> pr = Pronounceablity()
>>> pr.syllable('terhtsadathe')
6
>>> pr.syllable('hello')
2
>>> pr.syllable('gloust')
4
>>> complexity = Complexity()
>>> complexity.complexity('D7!rcc&umnsd')
7
>>> complexity.complexity('a4ILot#h')
7
>>> complexity.complexity('password')
-1
"""
import doctest
doctest.testmod()
