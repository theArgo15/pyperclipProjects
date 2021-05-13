import re
import pyperclip

# data is taken directly from clipboard. Copy an excel column with cells that have information subdivided by semicolon.
data=str(pyperclip.paste())
print(f'scanning {len(data)} objects')
# these methods create a list from data that is subdivided by both new row and by semicolon
cleanData = ';'.join(data.split()).split(';')
cleanData.sort()
# outputs data as a list separated by newlines. This can be pasted into an email or spreadsheet
resultString = '\n'.join(cleanData)
print(resultString)
pyperclip.copy(str(resultString))