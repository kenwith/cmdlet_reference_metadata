import os

path_in = r'c:\users\kenwith\git\office-docs-powershell\sharepoint\sharepoint-ps\sharepoint-online/'
path_out = r'c:\processed/'



for file in os.listdir(path_in):
    f_in = open(os.path.join(path_in, file), 'r', encoding='utf8')
    f_out = open(os.path.join(path_out, file), 'w', encoding='utf8')

    cmdlet_name, file_extension = os.path.splitext(file)


    lines = f_in.readlines()

    lines.insert(3, "title: " + cmdlet_name + "\n")

    for line in lines:
        f_out.write(line) 

    f_in.close()
    f_out.close()

