import os 

# Creating a Folder or Directory
#os.mkdir("c3ops_demo")

os.chdir("/Users/ck/Desktop/Python_Module/")

print(os.getcwd())

listConent = os.listdir('.')

print(listConent)