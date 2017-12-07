import os

#path_in = r'c:\users\kenwith\git\office-docs-powershell\skype\skype-ps\skype/'
#path_out = r'c:\processed/'
path_in = r'./data/'
path_out = r'./processed/'

# cmdlets_to_ignore are in 2013 but not 2010. We only adding 2010 so ignore these.
# make sure to strip the \n character with rstrip()
cmdlets_to_ignore = [line.rstrip() for line in open("configs/skip_these", "r")]
#cmdlets_to_ignore = open("configs/skip_these", "r").readlines()

#for line in cmdlets_to_ignore:
    #print("skip this line: %s" % (line.rstrip()))

# For each file in the data directory.
for file in os.listdir(path_in):

    f_in = open(os.path.join(path_in, file), 'r', encoding='utf8')
    f_out = open(os.path.join(path_out, file), 'w', encoding='utf8')

    # Set the name of the cmdlet.
    cmdlet_name, file_extension = os.path.splitext(file)
    cmdlet_name_md = cmdlet_name + ".md"

    # if the file is not in the cmdlets_to_ignore them process it.
    if cmdlet_name_md not in cmdlets_to_ignore:
        lines = f_in.readlines()
        for line in lines:
            f_out.write(line.replace("SharePoint Server 2013", "SharePoint Server 2010, SharePoint Server 2013"))
        print("PROCESSED: %s" % cmdlet_name)
    else:
        lines = f_in.readlines()
        for line in lines:
            f_out.write(line)
        print("IGNORED: %s" % cmdlet_name)
    
    f_in.close()
    f_out.close()
