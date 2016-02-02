This is a simple script to concatenate 
individual book chapters (as text files)
into a single (novel) file.

To use label your chapters alphabetically 
as text files in a single folder like this:

Chapter1.0_My-First-Chapter.txt

Chapter2.0_My-Second-Chapter.txt

Chapter3.0_My-Second-Chapter.txt
...

(Make sure they start with the string 'Chapter')

Then from the command line:

python makenovel.py path_to_chapters_dir 'Novel Title'	

Your chapters will all be happy together in 'Novel Title'