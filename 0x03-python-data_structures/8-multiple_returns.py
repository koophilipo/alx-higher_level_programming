#!/usr/bin/python3

def multiple_returns(sentence):
    ln = 0
    fchar = ""
    if sentence[0] != None and len(sentence) > 0:
        ln = len(sentence)
        fchar += sentence[0]
    return (ln, fchar)
