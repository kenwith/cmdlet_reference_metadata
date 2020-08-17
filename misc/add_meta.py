import os

path_in = r'c:\<path_to_git>\git\office-docs-powershell\sharepoint\sharepoint-ps\sharepoint/'
path_out = r'c:\processed/'


for file in os.listdir(path_in):
    #f_in = open('markUp_files/Update-CsUserDatabase.md', 'r', encoding='utf8')
    #f_out = open('processed/Update-CsUserDatabase.md', 'w', encoding='utf8')
    f_in = open(os.path.join(path_in, file), 'r', encoding='utf8')
    f_out = open(os.path.join(path_out, file), 'w', encoding='utf8')

    lines = f_in.readlines()

    lines.insert(1, "external help file: \n")

    for line in lines:
        f_out.write(line) 

    f_in.close()
    f_out.close()

