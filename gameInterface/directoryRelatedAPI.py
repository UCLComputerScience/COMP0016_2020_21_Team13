import os

def picturesToBeProcessed(dirName):
    currentFolderName = os.path.dirname(os.path.abspath(__file__))
    imageFolderName = os.path.join(currentFolderName, dirName)
    try:
        if os.path.isdir(imageFolderName):
            fileNames = [f.path for f in os.scandir(imageFolderName)
                    if f.is_file() and f.path.endswith(('.png','.jpg','npz'))
                ]
    except Exception as e:
        print(dirName , " does not exits")
    return fileNames

def dirList(directory):
    dir_path = os.path.dirname(os.path.realpath(__file__))
    path = dir_path + directory
    folderName = [f.path for f in os.scandir(path) if f.is_dir]
    return folderName
