# To use label your chapters alphabetically as text files like this:
# Chapter1.0_My-First-Chapter.txt
# Chapter2.0_My-Second-Chapter.txt
# ...
# (Make sure they start with the string 'Chapter')
# Then from the command line:
# python makenovel.py path_to_chapters_dir 'Novel Title'	

# Import the os module, for the os.walk function
import os
import sys
import collections

#organize args
arg_names = ['command', 'directory', 'bookTitle']
args = dict(zip(arg_names, sys.argv))
argList = collections.namedtuple('argList', arg_names)
args = argList(*(args.get(arg, None) for arg in arg_names))

#check if title is None
if args.bookTitle is None:
	args.bookTitle = 'novel.txt'

def chaptersToNovel(rootDir):
	#list of chapters
	chapters = []
	
	#find all files in dir whose names start with 'chapter'
	for dirName, subdirList, fileList in os.walk(rootDir):
	    for fname in fileList:
	        if(fname.find('Chapter')==0):
	        	print('\t%s' % fname)
	        	chapters.append(fname)

	#concatenate them all into 'novel.txt'
	with open(args.bookTitle, 'w') as outfile:
    	    for fname in chapters:
		        with open(fname) as infile:
		            for line in infile:
		                outfile.write(line)

chaptersToNovel(args.directory)
print("Concatenated chapters into novel:" + args.bookTitle)