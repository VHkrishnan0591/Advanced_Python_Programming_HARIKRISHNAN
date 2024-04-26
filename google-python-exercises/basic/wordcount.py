#!/usr/bin/python3
# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# Google's Python Class
# http://code.google.com/edu/languages/google-python-class/

"""Wordcount exercise
Google's Python class

The main() below is already defined and complete. It calls print_words()
and print_top() functions which you write.

1. For the --count flag, implement a print_words(filename) function that counts
how often each word appears in the text and prints:
word1 count1
word2 count2
...

Print the above list in order sorted by word (python will sort punctuation to
come before letters -- that's fine). Store all the words as lowercase,
so 'The' and 'the' count as the same word.

2. For the --topcount flag, implement a print_top(filename) which is similar
to print_words() but which prints just the top 20 most common words sorted
so the most common word is first, then the next most common, and so on.

Use str.split() (no arguments) to split on all whitespace.

Workflow: don't build the whole program at once. Get it to an intermediate
milestone and print your data structure and sys.exit(0).
When that's working, try for the next milestone.

Optional: define a helper function to avoid code duplication inside
print_words() and print_top().

"""

import sys

# +++your code here+++
# Define print_words(filename) and print_top(filename) functions.
# You could write a helper utility function that reads a file
# and builds and returns a word/count dict for it.
# Then print_words() and print_top() can just call the utility function.

def print_words(filename):

  # Opening the file
  f = open(filename, 'rt', encoding='utf-8')
  file_read_string =""

  # Reading the file and storing the content in string

  for line in f:
    file_read_string = file_read_string + line
  
  # Converitng into lowercase and removing punctuation

  file_read_string = file_read_string.lower()
  list_of_common_punctuation = ["'",'"','!','.', ',','`',':',';',')','(','?']
  for i in list_of_common_punctuation:
    file_read_string = file_read_string.replace(i,"")
  
  # Removing the Linespaces

  file_read_string = file_read_string.replace("\n"," ")
  file_read_string = file_read_string.replace("--"," ")

  # Spliting the long text into each words

  list_of_all_words = file_read_string.split(" ")

  # Identifying the unique word

  unique_words_list = list(set(list_of_all_words))

  # Removing the empty strings that have caused due to the occurence of consecutive punctuation
  
  unique_words_list = [word for word in unique_words_list if word]

  # Counting the each unique word
  
  words_count = {}
  for word in unique_words_list:
    words_count[word] = list_of_all_words.count(word)
  print(words_count)

def print_top(filename):

  # Opening the file
  
  f = open(filename, 'rt', encoding='utf-8')
  file_read_string =""

  # Reading the file and storing the content in string

  for line in f:
    file_read_string = file_read_string + line
  
  # Converitng into lowercase and removing punctuation

  file_read_string = file_read_string.lower()
  list_of_common_punctuation = ["'",'"','!','.', ',','`',':',';',')','(','?']
  for i in list_of_common_punctuation:
    file_read_string = file_read_string.replace(i,"")
  
  # Removing the Linespaces

  file_read_string = file_read_string.replace("\n"," ")
  file_read_string = file_read_string.replace("--"," ")

  # Spliting the long text into each words

  list_of_all_words = file_read_string.split(" ")

  # Identifying the unique word

  unique_words_list = list(set(list_of_all_words))

  # Removing the empty strings that have caused due to the occurence of consecutive punctuation
  
  unique_words_list = [word for word in unique_words_list if word]

  # Counting the each unique word

  words_count = {}
  for word in unique_words_list:
    words_count[word] = list_of_all_words.count(word)
  
  # Sorting the dictionary of words with the count based on counts in descending order

  sorted_dict_of_word_count = dict(sorted(words_count.items(), key=lambda item: item[1],reverse= True))
  sorted_word_count_dict_keys_list = list(sorted_dict_of_word_count.keys())

  # Taking the 20 most used words
    
  top_count_of_words = {}
  for key in sorted_word_count_dict_keys_list[:20]:
    top_count_of_words[key] = sorted_dict_of_word_count[key]
  print(top_count_of_words)
###

# This basic command line argument parsing code is provided and
# calls the print_words() and print_top() functions which you must define.
def main():
  if len(sys.argv) != 3:
    print('usage: ./wordcount.py {--count | --topcount} file')
    sys.exit(1)

  option = sys.argv[1]
  filename = sys.argv[2]
  if option == '--count':
    print_words(filename)
  elif option == '--topcount':
    print_top(filename)
  else:
    print('unknown option: ' + option)
    sys.exit(1)

if __name__ == '__main__':
  main()
