#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

"""
Mimic exercise

Read in the file specified on the command line.
Do a simple split() on whitespace to obtain all the words in the file.
Rather than read the file line by line, it's easier to read it into
one giant string and split it once.

Note: the standard python module 'random' includes a random.choice(list)
method which picks a random element from a non-empty list.

You can try adding in line breaks around 70 columns so the output looks
better.
"""

__author__ = "Erick Sibrian"


import random
import sys


def create_mimic_dict(filename):
    """Returns a dict mapping each word to a list of words which follow it.
    For example:
        Input: "I am a software developer, and I don't care who knows"
        Output:
            {
                "" : ["I"],
                "I" : ["am", "don't"],
                "am": ["a"],
                "a": ["software"],
                "software" : ["developer,"],
                "developer," : ["and"],
                "and" : ["I"],
                "don't" : ["care"],
                "care" : ["who"],
                "who" : ["knows"]
            }
    """
    # open and read the file
    mimic_dict = {}
    previous = ""
    book = open(filename, "r")
    page = book.read()
    book.close()
    words = page.split()
    for word in words:
        if previous not in mimic_dict:
            mimic_dict[previous] = [word]
        else:
            mimic_dict[previous].append(word)
        previous = word
    return mimic_dict
    #############################
    # with open(filename) as book:
    #     page = book.read()
    #     book.close()
    #     nocoma = page.replace(',', '')
    #     word_list = nocoma.split(" ")
    #     for word in word_list:
    #         if previous not in mimic_dict:
    #             mimic_dict[previous] = [word]
    #         else:
    #             mimic_dict[previous].append(word)
    #             previou = word
    #             print(mimic_dict)
    # mimic_dict[word_list[0]] = word_list[1]
    # print(mimic_dict)
    ##################################
    # with open(filename, "r") as book:
    #     for line in book:
    #         lineStr = line.strip()
    #         word_list = lineStr.split(",")
    #         mimic_dict[word_list[0]] = word_list[1]
    #         print(mimic_dict)


print(create_mimic_dict("imdev.txt"))


def print_mimic_random(mimic_dict, num_words):
    """Given a previously created mimic_dict and num_words,
    prints random words from mimic_dict as follows:
        - Use a start_word of '' (empty string)
        - Print the start_word
        - Look up the start_word in your mimic_dict and get its next-list
        - Randomly select a new word from the next-list
        - Repeat this process num_words times
    """
    # +++your code here+++
    start_word = ""
    for i in range(num_words + 1):
        print(start_word)
        if start_word in mimic_dict:
            start_word = random.choice(mimic_dict.get(start_word))
        else:
            start_word = random.choice(mimic_dict.get(""))


print_mimic_random(mimic_dict, num_words)


def main(args):
    # Get input filename from command line args
    filename = args[0]

    # Create and print the jumbled (mimic) version of the input file
    print(f'Using {filename} as input:\n')
    d = create_mimic_dict(filename)
    print_mimic_random(d, 200)


if __name__ == '__main__':
    if len(sys.argv) != 2:
        print('usage: python mimic.py file-to-read')
    else:
        main(sys.argv[1:])
    print('\n\nCompleted.')
