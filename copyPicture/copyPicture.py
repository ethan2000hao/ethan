import os
import shutil
path = 'C:/Users/86188/Desktop/record'
new_path = 'C:/Users/86188/Desktop/ppp'
i = 0
for root, dirs, files in os.walk(path):
    # print(root)

    for sFile in files:

        i = i + 1
        srcname = os.path.join(root, sFile)
        desname = os.path.join(new_path, sFile)
        shutil.copy(srcname, desname)
        print("copying: NO ", i)
print("finished !")