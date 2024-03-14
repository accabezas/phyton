class Librarian:
  def __init__(self, projectPath, projectName):
    self.projectPath = projectPath
    self.projectName = projectName

  def createProjectFolders(self):
    #* Imports
    from google.colab import drive
    import os
    
    #* Google drive mount
    if not os.path.exists('/content/gdrive'):
      drive.mount('/content/gdrive')
      
    #* Folders Creation
    if not os.path.exists(self.projectPath + '/' + self.projectName):
      os.mkdir(self.projectPath + '/' + self.projectName)
      os.mkdir(self.projectPath + '/' + self.projectName + '/1. Raw')
      os.mkdir(self.projectPath + '/' + self.projectName + '/2. Output')

  def getRawFilesList(self):
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