# my_module.py

def createFolder(folderPath, folderName):
    from google.colab import drive
    import os
    drive.mount('/content/gdrive')
    os.mkdir(folderPath + '/' + rawDataFolderName)
    print("Folder creado correctamente")