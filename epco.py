import sys

from logger import eventLogger
from classifier import classifier
from path_builder import pathBuilder

SRC = input("path: ")

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

def epco():
    pathBuilder(DST)
    classifier(DOC_EXT_LST, DOC_DST_PATH, SRC)
    classifier(AUD_EXT_LST, AUD_DST_PATH, SRC)
    classifier(VID_EXT_LST, VID_DST_PATH, SRC)
    classifier(IMG_EXT_LST, IMG_DST_PATH, SRC)
    classifier(ARCH_EXT_LST, ARCH_DST_PATH, SRC)
    classifier(OTR_EXT_LST, OTR_DST_PATH, SRC)
