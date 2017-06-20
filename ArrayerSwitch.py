#Script to overwrite PRODUCTION_DATA FOLDER for either Arrayer 1 or Arrayer 2
#Must contain 3 folders: PRODUCTION_DATA, PRODUCTION_ARRAYER1, PRODUCTION_ARRAYER2
#Place script in the same folder as PRODUCTION_DATA
#20/06/17

import os, shutil
folder = '\PRODUCTION_DATA'
root = os.getcwd() + folder
print(root)
#Check to see if directory exists, if so, delete all contents within
if os.path.exists(root):
    shutil.rmtree(root)

print("PRODUCTION_DATA contents deleted")

#Dump either PRODUCTION_DATA folder into PRODUCTION_DATA
num = input("Enter Arrayer Number: ")
shutil.copytree(os.getcwd() +'\PRODUCTION_ARRAYER' +str(num),root)
print('PRODUCTION_DATA set up for ARRAYER' +str(num))

input("Enter any key to exit")