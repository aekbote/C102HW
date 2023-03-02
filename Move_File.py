import os
import shutil


from_dir = 'C:\\Users\\avani\\Downloads'
to_dir = 'C:\\Users\\avani\\Documents'

list_of_files = os.listdir(from_dir)
print(list_of_files)

for fileName in list_of_files:
    root, extension = os.path.splitext(fileName)

    if extension == '':
        continue
    if extension in [ '.txt', '.doc', '.docx', '.pdf']:
        path1=  from_dir+'/'+fileName
        path2=to_dir+'/'+"Document_Files"
        path3=to_dir+'/'+"Document_Files"+'/'+fileName

        if os.path.exists(path2):
            print("Moving "+ fileName + ".....")

            shutil.move(path1, path3)
        
        else:
            os.makedirs(path2)
            print("Moving " + fileName + ".....")
            shutil.move(path1, path3)