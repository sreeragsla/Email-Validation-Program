import re
s=input()
pattern='[a-zA-Z1-9]\w*[.]?\w+@gmail[.]com'
print(re.findall(pattern,s))

