#!/usr/bin/python3
# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# Google's Python Class
# http://code.google.com/edu/languages/google-python-class/

"""Mimic pyquick exercise -- optional extra exercise.
Google's Python Class

Read in the file specified on the command line.
Do a simple split() on whitespace to obtain all the words in the file.
Rather than read the file line by line, it's easier to read
it into one giant string and split it once.

Build a "mimic" dict that maps each word that appears in the file
to a list of all the words that immediately follow that word in the file.
The list of words can be be in any order and should include
duplicates. So for example the key "and" might have the list
["then", "best", "then", "after", ...] listing
all the words which came after "and" in the text.
We'll say that the empty string is what comes before
the first word in the file.

With the mimic dict, it's fairly easy to emit random
text that mimics the original. Print a word, then look
up what words might come next and pick one at random as
the next work.
Use the empty string as the first word to prime things.
If we ever get stuck with a word that is not in the dict,
go back to the empty string to keep things moving.

Note: the standard python module 'random' includes a
random.choice(list) method which picks a random element
from a non-empty list.

For fun, feed your program to itself as input.
Could work on getting it to put in linebreaks around 70
columns, so the output looks better.

"""

import random
import sys


def mimic_dict(filename):
  """Returns mimic dict mapping each word to list of words which follow it."""
  # +++your code here+++

  # Opening the file

  f = open(filename, encoding='utf-8')

  # Reading the contents of the file into a string varaible file_read_string
  
  file_read_string = f.read()

  # Removing punctuation

  # list_of_punctuation = ["'",'"','!','.', ',','`',':',';',')','(','?','-']
  # for i in list_of_punctuation:
  #   file_read_string = file_read_string.replace(i,"")
  
  # Spliting the file content word by word

  list_of_words = file_read_string.replace('\n', " ").split(" ")
  list_of_words =[i for i in list_of_words if i != ""]
  
  # Creating a dictionary to map the words with other word which follows the previous

  mimic_dict = {'':[list_of_words[0]]}
  
  # Iterating through the list of words on the file to check for all the words following it and map them in a dictionary

  for i in list_of_words:
    if i != list_of_words[len(list_of_words)-1]:
      following_word  = [list_of_words[index+1] for (index, item) in enumerate(list_of_words) if item == i]
      mimic_dict[i] = following_word

  return mimic_dict


def print_mimic(mimic_dict, word):
  """Given mimic dict and start word, prints 200 random words."""
  # +++your code here+++
  
  # Maping the start word to a loopup variable used for search in dictionary

  lookup_word = word

  # Running the loop 200 times to print 200 words

  for i in range(200):

  # Suppose lookupword is not present in dictionary start with empty string and choose a random mapping word from mimic_dict 
  # Else choose a  random mapping word till reaching 200 words

    if mimic_dict.get(lookup_word) is None:
      lookup_word = ''
      following_word_list = mimic_dict[lookup_word]
      lookup_word = random.choice(following_word_list)
      print(lookup_word, end=" ")
    else:
      following_word_list = mimic_dict[lookup_word]
      lookup_word = random.choice(following_word_list)
      print(lookup_word, end = " ")


# Provided main(), calls mimic_dict() and mimic()
def main():
  if len(sys.argv) != 2:
    print('usage: ./mimic.py file-to-read')
    sys.exit(1)

  dict = mimic_dict(sys.argv[1])
  print_mimic(dict, '')


if __name__ == '__main__':
  main()
