# pyperclipProjects

This repo contains various small scripts that implement the pyperclip module.
The pyperclip module can import the contents of your clipboard as a Python string

To use these scripts you will need to pip install pyperclip

aNumbers.py

This script uses a regex to find part numbers that follow the pattern A###B###, but this can be modified to any regex you like.
for example it can be modified so you can copy a whole website page and it will find all of the email addresses or all of the phone numbers.

salesforceBOM.py

This script takes an input from the clipboard that is a column of an excel sheet. 
The excel has data that is split up by row, but also by semicolons. The script outputs all of the data in a single list.
