#!/usr/bin/python3
# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# Google's Python Class
# http://code.google.com/edu/languages/google-python-class/

# Additional basic string exercises

# D. verbing
# Given a string, if its length is at least 3,
# add 'ing' to its end.
# Unless it already ends in 'ing', in which case
# add 'ly' instead.
# If the string length is less than 3, leave it unchanged.
# Return the resulting string.
def verbing(s):
  # +++your code here+++

  # Check for string ends with 'ing and replace it with ly

  if s[-3:] == 'ing':
    s = s+'ly'
  elif len(s) > 2:
    s= s+'ing'
  return s


# E. not_bad
# Given a string, find the first appearance of the
# substring 'not' and 'bad'. If the 'bad' follows
# the 'not', replace the whole 'not'...'bad' substring
# with 'good'.
# Return the resulting string.
# So 'This dinner is not that bad!' yields:
# This dinner is good!
def not_bad(s):
  # +++your code here+++

  # Finding the position of substring 'not'

  pos_of_word_not = s.find('not')

  # Finding the position of substring 'bad'
  
  pos_of_word_bad = s.find('bad')

  # Check if substring 'bad' follows 'not'

  if (pos_of_word_not < pos_of_word_bad):

    # Then Replaces the whole substring 'not'...'bad' with substring 'good'
    s = s.replace(s[pos_of_word_not:pos_of_word_bad+3], 'good')
  elif pos_of_word_bad == -1 or pos_of_word_not == -1:
    s = s
  return s


# F. front_back
# Consider dividing a string into two halves.
# If the length is even, the front and back halves are the same length.
# If the length is odd, we'll say that the extra char goes in the front half.
# e.g. 'abcde', the front half is 'abc', the back half 'de'.
# Given 2 strings, a and b, return a string of the form
#  a-front + b-front + a-back + b-back
def front_back(a, b):
  # +++your code here+++
  def split_string(s):

    # Checking for the length of string to be even or odd

    if len(s) %2 ==0:
      # Split the front and back havlves of the string with same length

      mid_index = int(len(s)/2)
      front_part = s[0:mid_index]
      back_part = s[mid_index:]
      return [front_part, back_part]

    else:
      # Split the front and back havlves of the string with extra character goes to first

      mid_index = int((len(s)/2))+1
      front_part = s[0:mid_index]
      back_part = s[mid_index:]
      return [front_part, back_part]
  a_split = split_string(a)
  b_split = split_string(b)

  # Concating the two strings into the form a-front + b-front + a-back + b-back

  return a_split[0]+b_split[0]+a_split[1]+b_split[1]


# Simple provided test() function used in main() to print
# what each function returns vs. what it's supposed to return.
def test(got, expected):
  if got == expected:
    prefix = ' OK '
  else:
    prefix = '  X '
  print('%s got: %s expected: %s' % (prefix, repr(got), repr(expected)))


# main() calls the above functions with interesting inputs,
# using the above test() to check if the result is correct or not.
def main():
  print('verbing')
  test(verbing('hail'), 'hailing')
  test(verbing('swiming'), 'swimingly')
  test(verbing('do'), 'do')

  print()
  print('not_bad')
  test(not_bad('This movie is not so bad'), 'This movie is good')
  test(not_bad('This dinner is not that bad!'), 'This dinner is good!')
  test(not_bad('This tea is not hot'), 'This tea is not hot')
  test(not_bad("It's bad yet not"), "It's bad yet not")

  print()
  print('front_back')
  test(front_back('abcd', 'xy'), 'abxcdy')
  test(front_back('abcde', 'xyz'), 'abcxydez')
  test(front_back('Kitten', 'Donut'), 'KitDontenut')

if __name__ == '__main__':
  main()
