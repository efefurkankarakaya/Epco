import os
import uuid
import pathlib

from shutil import copy
from logger import eventLogger

def classifier(extensionList, destination, source):
    for path, directory, file in os.walk(source):
        for fileName in file:
            filePath = path + "/" + fileName
            for extension in extensionList:
                if (fileName.endswith(extension)):
                    if (not os.path.exists(destination)):
                        try:
                            os.mkdir(destination)
                            print(f"[status] created : {destination}")
                            if (os.path.exists(destination)):
                                details = destination + "/details"
                                os.mkdir(details)
                                print(f"[status] created : {details}")
                        except FileExistsError:
                            print(f"[status] already exists : {destination}")
                        except:
                            print(f"[status] an unknown error occurred in {destination} creation")
                            break
                    newFilePath = destination + "/" + fileName
                    if (not os.path.exists(newFilePath)):
                        copy(filePath, destination)
                        print(f"[status] file fetched : {filePath}")
                        eventLogger(destination, filePath)
                    else:
                        # print(f"[status] could not fetched, already exists : {fileName}")
                        uniquePath = destination + "/" + os.path.splitext(fileName)[0] + "-" + str(uuid.uuid4()) + pathlib.Path(fileName).suffix
                        print(f"{uniquePath=}")
                        copy(filePath, uniquePath)
                        # print(f"[status : unique] file fetched : {filePath}")
                        eventLogger(destination, filePath)