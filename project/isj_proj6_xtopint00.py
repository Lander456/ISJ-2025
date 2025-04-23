#!/usr/bin/env python3
import sys
from collections import Counter
import doctest

class ValidationError(Exception):

    pass

def upd_word_counts(sentence, word_counts = None, *, to_upper = False):

    if word_counts is None:

        word_counts = Counter()

    internalCounter = word_counts.copy()

    if to_upper:

        for key in word_counts.keys():

            if not key.isupper():

                raise ValidationError()

        sentence = sentence.upper()

    internalCounter.update(sentence.split())

    return internalCounter

