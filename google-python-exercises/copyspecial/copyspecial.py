#!/usr/bin/python3
# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# Google's Python Class
# http://code.google.com/edu/languages/google-python-class/

import sys
import re
import os
import shutil
import subprocess

"""Copy Special exercise
"""

# +++your code here+++
# Write functions and modify main() to call them
def get_special_paths(dir):
  filenames = os.listdir(dir)
  list_of_path_of_special_files =[]  # "special" file is one where the name contains the pattern __w__ somewhere, where the w is one or more word chars
  for filename in filenames:
    print(filename)
    match = match = re.search(r'__(\w+)__', filename) 
    if match:
     print(os.path.abspath(os.path.join(dir, filename)))
     list_of_path_of_special_files.append(os.path.abspath(os.path.join(dir, filename)))
  return list_of_path_of_special_files

def copy_to(paths, dir):
  if os.path.exists(dir):
    shutil.copy(paths, os.path.abspath(os.path.join(dir, os.path.basename(paths))))
  else:
    os.mkdir(dir)
    shutil.copy(paths, os.path.abspath(os.path.join(dir, os.path.basename(paths))))

def zip_to(paths, zippath):
  cmd = 'zip -j  ' + zipath + paths
  print("Command I'm going to do:", cmd)   ## good to debug cmd before actually running it
  (status, output) = subprocess.getstatusoutput(cmd)
  if status:    ## Error case, print the command's output to stderr and exit
    sys.stderr.write(output)
    sys.exit(status)
  print(output)  ## Otherwise do something with the command's output


def main():
  # This basic command line argument parsing code is provided.
  # Add code to call your functions below.

  # Make a list of command line arguments, omitting the [0] element
  # which is the script itself.
  args = sys.argv[1:]
  if not args:
    print('usage: [--todir dir][--tozip zipfile] dir [dir ...]')
    sys.exit(1)

  # todir and tozip are either set from command line
  # or left as the empty string.
  # The args array is left just containing the dirs.
  todir = ''
  if args[0] == '--todir':
    todir = args[1]
    del args[0:2]

  tozip = ''
  if args[0] == '--tozip':
    tozip = args[1]
    del args[0:2]

  if not args: # A zero length array evaluates to "False".
    print('error: must specify one or more dirs')
    sys.exit(1)

  # +++your code here+++
  # Call your functions
  directory_and_its_file_dictionary = {}
  for directory in args:
   list_of_path_of_files = get_special_paths(directory)
   directory_and_its_file_dictionary[directory] = list_of_path_of_files
  if todir != '':
   for filepath_list in directory_and_its_file_dictionary.values():
    for filepath in filepath_list:
     copy_to(filepath, dir)
  if tozip != '':
   for filepath_list in directory_and_its_file_dictionary.values():
    zip_to(filepath_list, tozip)

if __name__ == '__main__':
  main()
