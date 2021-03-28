import os

def pathBuilder(destination):
    try:
        os.makedirs(destination)
        print(f"[status] created : {destination}")
    except FileExistsError:
        print(f"[status] already exists : {destination}")
    except:
        print("[status] an unknown error occurred in pathBuilder function")