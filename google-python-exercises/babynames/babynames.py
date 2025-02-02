#!/usr/bin/python3
# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# Google's Python Class
# http://code.google.com/edu/languages/google-python-class/

import sys
import re

"""Baby Names exercise

Define the extract_names() function below and change main()
to call it.

For writing regex, it's nice to include a copy of the target
text for inspiration.

Here's what the html looks like in the baby.html files:
...
<h3 align="center">Popularity in 1990</h3>
....
<tr align="right"><td>1</td><td>Michael</td><td>Jessica</td>
<tr align="right"><td>2</td><td>Christopher</td><td>Ashley</td>
<tr align="right"><td>3</td><td>Matthew</td><td>Brittany</td>
...

Suggested milestones for incremental development:
 -Extract the year and print it
 -Extract the names and rank numbers and just print them
 -Get the names data into a dict and print it
 -Build the [year, 'name rank', ... ] list and print it
 -Fix main() to use the extract_names list
"""

def extract_names(filename):
  """
  Given a file name for baby.html, returns a list starting with the year string
  followed by the name-rank strings in alphabetical order.
  ['2006', 'Aaliyah 91', Aaron 57', 'Abagail 895', ' ...]
  """
  # +++your code here+++

  # Opening the file

  f = open(filename, encoding='utf-8')

  # Importing re module to execute the findall and search method of the library

  import re

  # Reading the contents of the file into a string varaible file_read_string

  file_read_string = f.read()

  # Finding all the matches for the rank,   boyname and girlname

  matching_line_of_rank_boyname_girlname = re.findall(r'<tr.+><td>(\d+).+>(\w+)<.+>(\w+)', file_read_string)

  # Intiatiling the array for boyname, girlname and year of the file

  boy_name = []
  girl_name = []
  year_of_file=[]

  # Extracting the year from the file

  full_heading_text = re.search(r'(<h3.+>)', file_read_string)
  year_on_heading = re.search(r'\s\d+',full_heading_text.group())

  # Appending the year on the file to the year array

  year_of_file.append(year_on_heading.group().strip())

  # Extracting the boyname with rank and girlname with rank and append it to the boyname and girlname array

  for i in matching_line_of_rank_boyname_girlname:
    boy_name.append(i[1]+" "+ i[0])
    girl_name.append(i[2]+" "+ i[0])
  
  # Combine both the girlname and boyname into a combined array named as 'Total_name'

  total_name = boy_name + girl_name

  # Concat the year array with the sorted Total_name array

  print(year_of_file+sorted(total_name))
  return year_of_file+sorted(total_name)


def main():
  # This command-line parsing code is provided.
  # Make a list of command line arguments, omitting the [0] element
  # which is the script itself.
  args = sys.argv[1:]

  if not args:
    print('usage: [--summaryfile] file [file ...]')
    sys.exit(1)

  # Notice the summary flag and remove it from args if it is present.
  summary = False
  if args[0] == '--summaryfile':
    summary = True
    del args[0]

  # +++your code here+++
  # For each filename, get the names, then either print the text output
  # or write it to a summary file
  for filename in args:
   output_of_the_sorted_names = extract_names(filename)

   if summary:
     with open(filename + '.summary', "w", encoding='utf-8') as f:
      for i in output_of_the_sorted_names:
       f.write(i + '\n')
      f.close()

if __name__ == '__main__':
  main()
