class Librarian:
  def __init__(self, projectPath, projectName):
    self.projectPath = projectPath
    self.projectName = projectName

  def createProjectFolders(self):
    #* Google drive mount
    from google.colab import drive
    drive.mount('/content/gdrive')
    #* Folders Creation
    import os
    os.mkdir(self.projectPath + '/' + self.projectName)
    os.mkdir(self.projectPath + '/' + self.projectName + '/1. Raw')
    os.mkdir(self.projectPath + '/' + self.projectName + '/2. Output')

  def getRawFilePaths(self):
    import os
    files = os.listdir(self.projectPath + '/' + self.projectName + '/Raw')
    return files

  def getRawFolderPath(self):
    rawFolderPath = self.projectPath + '/' + self.projectName + '/Raw'
    return rawFolderPath

  def saveOutput(self, fileName):
    import shutil
    outputFolder = self.projectPath + '/' + self.projectName + '/Output'
    print(fileName)
    shutil.copy("/content/" + fileName, outputFolder + "/" + fileName)