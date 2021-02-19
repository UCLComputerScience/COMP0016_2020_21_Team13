import os
def picturesToBeProcessed(dirName):
    currentFolderName = os.path.dirname(os.path.abspath(__file__))
    imageFolderName = os.path.join(currentFolderName, dirName)
    try:
        if os.path.isdir(imageFolderName):
            fileNames = [f.path for f in os.scandir(imageFolderName)
                    if f.is_file() and f.path.endswith(('.png','.jpg'))
                ]
    except Exception as e:
        print(dirName , " does not exits")
    if len(fileNames)>2:
        print("too many pictures in a single file")
        return
    return fileNames

def dirList():
    dir_path = os.path.dirname(os.path.realpath(__file__))
    path = dir_path + r'/../testing/integrationTest/scoring/data'
    folderName = [f.path for f in os.scandir(path) if f.is_dir]
    return folderName