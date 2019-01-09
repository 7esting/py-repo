#!/usr/bin/env python

import sys
import os
import os.path
import fileinput
import re


for file in os.listdir("."):
    info = os.stat(file)
    print("%-20s : size (bytes) %d inode %d" % (file, info.st_size, info.st_ino))


# python -c "import sys;[sys.stdout.write(' '.join(line.split()[2:]) + '\n') for line in sys.stdin]" < file.txt
# sys.stdout.write(' '.join(line.split()[2:]) + '\n')
#
# for line in sys.stdin:
#     print(line)

# for line in fileinput.input():
#     line = re.sub(r'\* \[(.*)\]\(#(.*)\)', r'<h2 id="\2">\1</h2>', line.rstrip())
#     print(line)

# Count total lines in file
def file_lines(p_file) -> "Return the total number of lines in file.":
    """Return the total number of lines in file."""
    with open(p_file,'r') as file:
        line_count = 0
        for line in file:
            line_count += 1
        return line_count

my_file = '../system_admin/passwd.txt'
print(f"\nFile: {my_file} Total Lines: {file_lines(my_file)}\n")

with open('../system_admin/passwd.txt','r+') as passwd_file:
    for line in passwd_file:
        #print(line)
        #print(f"{line.split(':')[0:1]}")
        #usr = line.split(':')[0:1]
        # .replace('jdoe', 'wolverine', 1)
        # line.find('str', [start_indx], [end_indx])
        if line.find('jdoe', 0, 6) != -1:
            print(f"Found 'jdoe' & replaced user name => {line.replace('jdoe','bgates', 2)}")

            # split at ':' and create a list from current line
            line_list = line.split(':')
            print(f"{line_list} => line has {len(line_list)} cols. \
                line_list[0] => User name {line_list[0]}")

            print(f"{line_list[0].capitalize()}")

            updated_line = ''.join(line_list[0]) + ' is missing!'
            ## Padding int value includes string length

            #updated_line = '{:>60}'.format(updated_line)
            updated_line = '{:60}'.format(updated_line)
            updated_line = "".join(updated_line + ':EOL')
            print(f"{type(updated_line)}: String length: {len(updated_line)}")
            print(f"1:{updated_line}")

            #passwd_file.write(line.replace(str(line_list[0:]), updated_line)) # This is appending to line
            passwd_file.write("".replace(line, updated_line))
            #passwd_file.write(updated_line) # appends updated line
            print(line)


passwd_file.close()
