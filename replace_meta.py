import os

path_in = r"c:\\users\\kenwith\\git\\azure-docs-pr\\articles\\active-directory\\saas-apps\\"
path_out = r"c:\\users\\kenwith\\git\\azure-docs-pr\\articles\\active-directory\\saas-apps\\"

# For each file in the data directory.
for file in os.listdir(path_in):

    print("processing: " + file)

    if file.endswith(".md"):
        fin = open(os.path.join(path_in, file), 'r', encoding='utf8')
        lines = fin.readlines()
        fin.close()
        fout = open(os.path.join(path_out, file), 'w', encoding='utf8')
        for line in lines:
            if "ms.reviewer:" in line:
                fout.write("ms.reviewer: celested\n")
            else:
                fout.write(line)
        fout.close()
        continue
    else:
        continue
