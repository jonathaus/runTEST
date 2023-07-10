# downloaded = False
# import AutoUpdate
# import urllib.request

# AutoUpdate.set_url("https://raw.githubusercontent.com/jonathaus/runTEST/main/version.txt")
# AutoUpdate.set_current_version("2.0")

# print(AutoUpdate.is_up_to_date())  

# if not AutoUpdate.is_up_to_date():
#     urllib.request.urlretrieve("https://github.com/jonathaus/runTEST/archive/refs/heads/main.zip", "testgame.zip")
#     downloaded = True


# from zipfile import ZipFile
# import os

# if downloaded:
#     extracted = False
#     with ZipFile('testgame.zip', 'r') as zip:
#         zip.extractall()
#         extracted = True

#     if extracted:
#         os.system("main.pyw")

import os
# get current path
path = str(os.getcwd())
print(path)

from git import Repo
Repo.clone_from("https://github.com/jonathaus/runTEST.git", path)
