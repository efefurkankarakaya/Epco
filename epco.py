import os
import sys
from shutil import copy
import uuid
import pathlib

from logger import eventLogger

SRC = str(sys.argv[1])

MAIN_DIR = "epco_files"
SIMPLIFIED_SRC_PATH = (SRC.replace(":", "__")).replace("/", "__")
DST = MAIN_DIR + "/" + SIMPLIFIED_SRC_PATH

DOC_DST_PATH = DST + "/documents"
AUD_DST_PATH =  DST + "/audios"
VID_DST_PATH = DST + "/videos"
IMG_DST_PATH = DST + "/images"
ARCH_DST_PATH = DST + "/archives"
OTR_DST_PATH = DST + "/others"

DOC_EXT_LST = [".rtf", ".txt", ".pdf", ".docx", ".doc"]
AUD_EXT_LST = [".mp3", ".flac", ".wav"]
VID_EXT_LST = [".mp4", ".webm"]
IMG_EXT_LST = [".jpg", ".jpeg", ".png", ".bmp", ".gif", ".heif", ".heic"]
ARCH_EXT_LST = [".rar", ".zip"]
OTR_EXT_LST = [".py", ".exe"]

def pathCreator():
    try:
        os.makedirs(DST)
        print(f"[status] created : {DST}")
    except FileExistsError:
        print(f"[status] already exists : {DST}")
    except:
        print("[status] an unknown error occurred in pathCreator function")

def classifier(extensionList, destinationPath):
    for path, directory, file in os.walk(SRC):
        for fileName in file:
            filePath = path + "/" + fileName
            for extension in extensionList:
                if (fileName.endswith(extension)):
                    if (not os.path.exists(destinationPath)):
                        try:
                            os.mkdir(destinationPath)
                            print(f"[status] created : {destinationPath}")
                            if (os.path.exists(destinationPath)):
                                details = destinationPath + "/details"
                                os.mkdir(details)
                                print(f"[status] created : {details}")
                        except FileExistsError:
                            print(f"[status] already exists : {destinationPath}")
                        except:
                            print(f"[status] an unknown error occurred in {destinationPath} creation")
                            break
                    newFilePath = destinationPath + "/" + fileName
                    if (not os.path.exists(newFilePath)):
                        copy(filePath, destinationPath)
                        print(f"[status] file fetched : {filePath}")
                        eventLogger(destinationPath, filePath)
                    else:
                        # print(f"[status] could not fetched, already exists : {fileName}")
                        uniquePath = destinationPath + "/" + os.path.splitext(fileName)[0] + "-" + str(uuid.uuid4()) + pathlib.Path(fileName).suffix
                        print(f"{uniquePath=}")
                        copy(filePath, uniquePath)
                        # print(f"[status : unique] file fetched : {filePath}")
                        eventLogger(destinationPath, filePath)

def main():
    pathCreator()
    classifier(DOC_EXT_LST, DOC_DST_PATH)
    classifier(AUD_EXT_LST, AUD_DST_PATH)
    classifier(VID_EXT_LST, VID_DST_PATH)
    classifier(IMG_EXT_LST, IMG_DST_PATH)
    classifier(ARCH_EXT_LST, ARCH_DST_PATH)
    classifier(OTR_EXT_LST, OTR_DST_PATH)

if __name__ == "__main__":
    main()
