#!/usr/bin/python3
# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# Google's Python Class
# http://code.google.com/edu/languages/google-python-class/

import os
import re
import sys
import urllib
import urllib.request

"""Logpuzzle exercise
Given an apache logfile, find the puzzle urls and download the images.

Here's what a puzzle url looks like:
10.254.254.28 - - [06/Aug/2007:00:13:48 -0700] "GET /~foo/puzzle-bar-aaab.jpg HTTP/1.0" 302 528 "-" "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.8.1.6) Gecko/20070725 Firefox/2.0.0.6"
"""


def read_urls(filename):
  """Returns a list of the puzzle urls from the given log file,
  extracting the hostname from the filename itself.
  Screens out duplicate urls and returns the urls sorted into
  increasing order."""
  # +++your code here+++
  
  # Opening the file

  f = open(filename, encoding='utf-8')

  # Reading the contents of the file into a string varaible file_read_string
  
  file_read_string = f.read()

  # Getting the servername from the filename using split function

  server_name = filename.split('_')[1] # Common convention servername follows after '_' sign in the filename

  # Extracting the image urls from the log file

  matching_line_of_image_url = re.findall(r'GET (\S+puzzle\S+.jpg)', file_read_string)

  # Getting the full URL of all the images
  full_image_url_list = []
  for image_url in matching_line_of_image_url:
    full_image_url_list.append('https://' + server_name + image_url)
  
  # Removing the duplicate usig set data structure

  full_image_url_list = set(full_image_url_list)
    
  # Sorting the URL in alphabetical order

  full_image_url_list = sorted(full_image_url_list,key=lambda full_url_list: full_url_list[-8:-4])

  # print(full_image_url_list)

  return full_image_url_list



def download_images(img_urls, dest_dir):
  """Given the urls already in the correct order, downloads
  each image into the given directory.
  Gives the images local filenames img0, img1, and so on.
  Creates an index.html in the directory
  with an img tag to show each local image file.
  Creates the directory if necessary.
  """
  # +++your code here+++

  # Creating a directory if dest_dir does not exist

  if not os.path.exists(dest_dir):
    os.mkdir(dest_dir)
  each_image_count = 0
  filepath_of_html_file = os.path.join(dest_dir, "index.html")

  # Downloading the images into the given directory

  for image_url in img_urls:
    urllib.request.urlretrieve(image_url, os.path.abspath(os.path.join(dest_dir, 'img'+str(each_image_count)+'.jpg')))
    each_image_count = each_image_count+1
  
  # Opening the html file in write mode in the directory and writing all the html content with the images
  
  with open( filepath_of_html_file, 'w', encoding='utf-8') as f:  
    f.write('<html>' + '\n')
    f.write('<body>' + '\n')
    for iterator in range(each_image_count):
      f.write('<img src="img%d.jpg">'%(iterator))
    f.write('\n' + '</body>' + '\n')
    f.write('</html>' + '\n')


def main():
  args = sys.argv[1:]

  if not args:
    print('usage: [--todir dir] logfile ')
    sys.exit(1)

  todir = ''
  if args[0] == '--todir':
    todir = args[1]
    del args[0:2]

  img_urls = read_urls(args[0])

  if todir:
    download_images(img_urls, todir)
  else:
    print('\n'.join(img_urls))

if __name__ == '__main__':
  main()
