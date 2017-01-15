import shutil
import os

src = 'C:\Users\Owner\Desktop\Folder A'
dest = 'C:\Users\Owner\Desktop\Folder B'

files = os.listdir(src)

for f in files:
    src_file = src + '\\' + f
    dest_file = dest + '\\' + f
    shutil.move(src_file,dest_file)
