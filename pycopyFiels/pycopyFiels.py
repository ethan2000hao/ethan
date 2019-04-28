import os
import shutil

srcPath = r"C:\Users\86188\Desktop\test01\ta"
desPath = r"C:\Users\86188\Desktop\test01\te"

for root, dirs, files in os.walk(srcPath):

    for sFile in files:
        if len(sFile) > 2:
            srcname = os.path.join(root, sFile)

            desname = os.path.join(desPath, sFile)
            shutil.copy(srcname, desname)
            print("copying: " + desname)