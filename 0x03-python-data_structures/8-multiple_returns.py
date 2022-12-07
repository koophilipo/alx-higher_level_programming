#!/usr/bin/python

def multiple_returns(sentence):
    ln = 0
    fchar = ""
    if sentence[0] != None:
        ln = len(sentence)
        fchar += sentence[0]
    return (ln, fchar)
