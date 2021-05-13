import re
import pyperclip

# data is taken directly from clipboard. Copy a whole webpage or email and script will parse out regex
data=str(pyperclip.paste())
print(f'scanning {len(data)} objects')
# this regex searchs for part numbers in the form A###B###, but can be modifed to anything that can be parsed with regex
aNumberRegex=re.compile(r'[A]\d{3}[A-Z]\d{3}', re.MULTILINE)
results = aNumberRegex.findall(data)
# get rid of duplicates
results= list(set(results))
results.sort()
resultString = '\n'.join(results)
# outputs data as a list separated by newlines. This can be pasted into an email or spreadsheet
print(resultString)
pyperclip.copy(str(resultString))