import os

#f = open('markUp_files/Update-CsUserDatabase.md', 'r')

path_in = 'markup_files/'
path_out = 'processed/'

f_out = open('result', 'w', encoding='utf8')

for file in os.listdir(path_in):
    f_in = open(os.path.join(path_in, file), 'r', encoding='utf8')
    #f_out = open(os.path.join(path_out, file), 'w', encoding='utf8')
    f_out.write(file + '\n')
    f_in.readline()
    a_string = f_in.readline()
    if not a_string.startswith("applicable"):
        print('FOUND IT!  ' + file)
    f_in.close()

f_out.close()
#for line in f:
    #print(line, end='')
