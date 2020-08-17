import os

f_in = open(r"C:\\Users\\kenwith\\git\\azure-docs-pr\\articles\\active-directory\\saas-apps\\4me-tutorial.md", 'r', encoding='utf8')

lines = f_in.readlines()
#print (lines)
for line in lines:
    print (line)
    
f_in.close()
