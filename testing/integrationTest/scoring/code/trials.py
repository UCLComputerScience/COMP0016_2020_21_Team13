import os
import sys
dir_path = os.path.dirname(os.path.realpath(__file__))
path = (dir_path + r'/../../../../openposeAPI/')

folderName = [f.path for f in os.scandir(path) if f.is_file]
print(folderName)
