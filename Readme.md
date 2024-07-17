# **Google Python Exercises**

## Overview
This repository contains the solutions of the Google Python Developer course exercise problems solved during the summer semester 2024 for the course of Advanced Programming in THD Cham Campus.
The exercises problems are focussed on the foundamental concepts of pythons like List, String, Dictionaries, Files, Regular expression and utilites.

There are four major exericises consisting nine coding exercise files. 
 - Basic Exercise 
   - Focussed on topics like string, list, sorting with the coding exercise files like string1.py, string2.py, list1.py and list2.py
   - Mimic.py and Wordcount.py focusses on topics like Dictionaries and files.
 - Babynames
   - Focussed on topics like Regular expression file operation like read and write operation
 - Logpuzzle
   - Focussed on topics like Regular expression file operation like read and write operation, HTML file creation
 - Copyspecial
   - Focussed on topics like Regular expression file operation like read and write operation and Utilities

---
# Installation Instructions
 - Download the Google Python Exercise Files from <https://developers.google.com/static/edu/python/google-python-exercises.zip>
 - Download the IDE of your choice (eg: VS Code <https://code.visualstudio.com/download>)
 - Download the GitHub Desktop <https://desktop.github.com/>
 - Install VScode and Git Hub Desktop
 - Create a repostiory in the github for the Google Python exercise and add the exercise file to it.
 - Download and Install Python from <https://www.python.org/ftp/python/3.12.4/python-3.12.4-amd64.exe>
 - Download and install git bash from <https://git-scm.com/downloads>
 - Before start solving install the necessary libraies or plugin like python, Git extension from VScode like Start git-bash, Python, Git History, Pylance, Python Debugger.
 ---

 # Plugins and Libraies Used
  - Python Version - 3.12.4
  - VS Code for Windows
  - GitHub for Windows
  - Git for Windows
  - Extension used in VS Code 
     - Start git-bash, Python, Git History, Pylance, Python Debugger.
---
# Coding Practises Followed
- The variables are given meaningful names which truly represent the context of the problem
- Clear and explainable comments are added 
- The variable name follow the **Snake Case** naming convention.
- Following is the below code example for the practises followed
```
python
# Intiatiling the array for boyname, girlname and year of the file

  boy_name = []
  girl_name = []
  year_of_file=[]

  # Extracting the year from the file

  full_heading_text = re.search(r'(<h3.+>)', file_read_string)
  year_on_heading = re.search(r'\s\d+',full_heading_text.group())

  # Appending the year on the file to the year array

  year_of_file.append(year_on_heading.group().strip())
```
---
# Authors
 - [VHkrishnan0591](https://github.com/VHkrishnan0591)