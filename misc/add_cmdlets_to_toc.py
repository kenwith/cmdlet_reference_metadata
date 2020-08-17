import os

f_in = open("fast_cmdlets", 'r', encoding='utf8')
f_out = open("fast_cmdlets_processed", 'w', encoding='utf8')

lines = f_in.readlines()

for line in lines:
    cmdlet = line.rstrip()
    cmdlet_with_md = cmdlet + ".md"
    f_out.write(r"### [" + cmdlet + r"](" + cmdlet_with_md + r")" + "\n")
    f_out.write(r"{{Manually Enter " + cmdlet + r" Description Here}}" + "\n\n")
    print("PROCESSED: %s" % cmdlet)

f_in.close()
f_out.close()
