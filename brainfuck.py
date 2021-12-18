#!/usr/bin/env python3

from __future__ import print_function

def brainfuck(bf_exp, end, data, idx, size):
    """
    python brainfuck interpreter
    """
    i, ptr = 0, 0
    arr = [0] * size
    while i <= end:
        head = bf_exp[i]
        if head == '>':
            ptr += 1
            if ptr >= len(arr):
                ptr = 0
        elif head == '<':
            ptr -= 1
            if ptr < 0:
                ptr = len(arr) - 1
        elif head == '+':
            arr[ptr] += 1
        elif head == '-':
            arr[ptr] -= 1
        elif head == '.':
            print(chr(arr[ptr]), end="")
        elif head == ',':
            if idx >= 0 and idx < len(data):
                arr[ptr] = ord(data[idx])
                idx += 1
            else:
                arr[ptr] = 0
        elif head =='[':
            if arr[ptr] == 0:
                itert = 1
                while itert > 0:
                    i += 1
                    c = bf_exp[i]
                    if c == '[':
                        itert += 1
                    elif c == ']':
                        itert -= 1
        elif head == ']':
            itert = 1
            while itert > 0:
                i -= 1
                c = bf_exp[i]
                if c == '[':
                    itert -= 1
                elif c == ']':
                    itert += 1
            i -= 1
        i += 1

def main():
    data = "giberish"
    print("******************* add brainfuck buffer size ******************")
    size = int(input())
    if size < 30000:
        size = 30000
    print("******************* add brainfuck expression *******************")
    bf_exp = input()
    len_exp = len(bf_exp)
    if len_exp > 0:
        print("*********************** add input if any ***********************")
        data = input()
        print("***************** add processing index of input ****************")
        idx = input()
        brainfuck(bf_exp, len_exp - 1, data, idx, size)
    print("ADD PROPER EXPRESSION")

if __name__ == "__main__":
    main()
