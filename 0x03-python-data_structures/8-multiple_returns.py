#!/usr/bin/python3


def multiple_returns(sentence):
    ln = 0
    fchar = ""
    if len(sentence) > 0 and sentence[0] is not None:
        ln = len(sentence)
        fchar += sentence[0]
    return (ln, fchar)
