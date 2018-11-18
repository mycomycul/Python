f = open("testtext.txt","rt")
# print(f.read())
#Line at a time
for x in f:
    print(x)
#SingleLine
print(f.readline())
#read only a set of characters
print(f.read(5))
print(f.read(5))

#Writing Files"
#Append to File
f= open("texttext.txt","a")
f.write("Ad one more line")

f = open("texttext.txt","rt")
print(f.read())

#Overwrite files
f = open("texttext.txt","w")
f.write("Content Deleted")

f = open("texttext.txt","rt")
print(f.read())

#New Files
try:
    #Use "x" flag
    f = open("testtext.txt","x")
    print(f)
except:
    print("File already exists")

#Delete Files
import os  
f.close()         
if os.path.exists("testtext.txt"):
    os.remove("texttext.txt")
    print("File Deleted")
else:
    print("The file does not exist")

#Create and Delete FOlder
print("Enter s folder Name")
path = input()
os.mkdir(path)
print("Press enter to delete your folder")
input()
os.rmdir(path)





