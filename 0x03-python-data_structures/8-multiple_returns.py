#!/usr/bin/python3

def multiple_returns(sentence):
    if not sentence:
        ch = None
        num = 0
    else:
        ch = sentence[0]
        num = len(sentence)
    return num, ch
