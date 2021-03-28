import os

from datetime import datetime

def eventLogger(folder, filePath):
    with open(f"{folder}/details/details.txt",
              "a+",
              encoding="utf-8") as detail:
        secondsCT = os.stat(os.path.abspath(filePath)).st_ctime
        creationTime = datetime.fromtimestamp(secondsCT)
        secondsLMT = os.stat(os.path.abspath(filePath)).st_mtime
        lastModifiedTime = datetime.fromtimestamp(secondsLMT)
        secondsLAT = os.stat(os.path.abspath(filePath)).st_atime
        lastAccessTime = datetime.fromtimestamp(secondsLAT)
        detail.write("File Name: " + filePath + "\n" + "Creation Time: " +
                     str(creationTime) + "\n" + "Last Modified Time: " +
                     str(lastModifiedTime) + "\n" + "Last Access Time: " +
                     str(lastAccessTime) + "\n\n*\n\n")