import os
import sys
from shutil import copy
from datetime import datetime
import uuid
import pathlib

destination = str(sys.argv[1])

mainFolder = "epco_files"
simplifiedFolderName = (destination.replace(":", "__")).replace("/", "__")
theFolder = mainFolder + "/" + simplifiedFolderName

documentFolder = theFolder + "/documents"
audioFolder =  theFolder + "/audios"
videoFolder = theFolder + "/videos"
imageFolder = theFolder + "/images"
archiveFolder = theFolder + "/archives"
otherFolder = theFolder + "/others"

documentExtensions = [".rtf", ".txt", ".pdf", ".docx", ".doc"]
audioExtensions = [".mp3", ".flac", ".wav"]
videoExtensions = [".mp4", ".webm"]
imageExtensions = [".jpg", ".jpeg", ".png", ".bmp", ".gif", ".heif", ".heic"]
archiveExtensions = [".rar", ".zip"]
otherExtensions = [".py", ".exe"]

def FolderCreator():
    try:
        os.makedirs(theFolder)
        print(f"[status] created : {theFolder}")
    except FileExistsError:
        print(f"[status] already exists : {theFolder}")
    except:
        print("[status] an unknown error occurred in FolderCreator function")

def DetailWriter(folder, filePath):
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

def PathRouter(extensionList, folder):
    for path, directory, file in os.walk(destination):
        for fileName in file:
            filePath = path + "/" + fileName
            for extension in extensionList:
                if (fileName.endswith(extension)):
                    if (not os.path.exists(folder)):
                        try:
                            os.mkdir(folder)
                            print(f"[status] created : {folder}")
                            if (os.path.exists(folder)):
                                details = folder + "/details"
                                os.mkdir(details)
                                print(f"[status] created : {details}")
                        except FileExistsError:
                            print(f"[status] already exists : {folder}")
                        except:
                            print(f"[status] an unknown error occurred in {folder} creation")
                            break
                    newFilePath = folder + "/" + fileName
                    if (not os.path.exists(newFilePath)):
                        copy(filePath, folder)
                        print(f"[status] file fetched : {filePath}")
                        DetailWriter(folder, filePath)
                    else:
                        print(f"[status] could not fetched, already exists : {fileName}")
                        # uniquePath = folder + "/" + os.path.splitext(fileName)[0] + "-" + str(uuid.uuid4()) + pathlib.Path(fileName).suffix
                        # print(f"{uniquePath=}")
                        # copy(filePath, uniquePath)
                        # print(f"[status : unique] file fetched : {filePath}")
                        # DetailWriter(folder, filePath)

def main():
    FolderCreator()
    PathRouter(documentExtensions, documentFolder)
    PathRouter(audioExtensions, audioFolder)
    PathRouter(videoExtensions, videoFolder)
    PathRouter(imageExtensions, imageFolder)
    PathRouter(archiveExtensions, archiveFolder)
    PathRouter(otherExtensions, otherFolder)

if __name__ == "__main__":
    main()
