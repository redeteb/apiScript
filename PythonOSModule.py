import os

# display the total number of items (both files and directories) present in the specified directory


count = 0
for root_dir, cur_dir, files in os.walk('kura'):
    count += len(files)
print('file count:', count)