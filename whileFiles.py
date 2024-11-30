# create directory /temp if not exist
# Remove files in /temp by date if exist
# create 5 files
# sleep for 3 seconds

import os
import time

CURRENT_DIRECTORY = os.getcwd()
print(CURRENT_DIRECTORY)

existd = os.path.isdir('temp')

if not existd:
    os.mkdir('temp')
    print('Directory /temp created')

TEMP_PATH = os.path.join(CURRENT_DIRECTORY,'temp')

# Ordenados por Fecha de creacion
while(True):
    files = os.listdir(TEMP_PATH)
    files = sorted(files, key=lambda file: os.path.getctime(os.path.join(TEMP_PATH, file)))

    if len(files) > 0:
        print('------------------------')
        print('------Removing Files------')

    for file in files:
        file_path = os.path.join(TEMP_PATH,file)
        if os.path.isfile(file_path):
            os.remove(file_path)
            print(f"File '{file}' Removed")
            time.sleep(.8)

    if len(files) > 0:
        print('------Files Removed------')
        print('------------------')
        time.sleep(1.5)

    print('------------------------')
    print('------Creating Files------')
    flag = False
    for i in range(1,6):
        if not os.path.exists(os.path.join(TEMP_PATH,f"{i}.txt")): 
            flag = True
            os.mknod(os.path.join(TEMP_PATH,f"{i}.txt"))
            print(f"Created File: --> {i}.txt")
            time.sleep(.8)
    
    if flag:
        print('------Files Created------')
    
    time.sleep(4)