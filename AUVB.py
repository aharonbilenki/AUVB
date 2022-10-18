import File
import os

#creat list of all the files in the pc
def AllpC():
    return 0

#creat list of all the files in a dir.
def DirInDir(path,DirFileList,DirName):
    count=-1
    flist=[]
    temp=DirFileList
    for fname in temp:
        count += 1
        if fname.find('.') == False:  # if fname is a dir, we extract all the files from it
            print(fname)
            DirFileList = os.listdir(path + "\\" +DirName+"\\"+fname)
            flist[count] = [fname, DirFileList]
            temp=DirFileList
    print(flist)
    return flist
def ByDir(path):
    count=-1
    flist=os.listdir(path)
    for fname in flist:
        count+=1
        if fname.find('.')==False:#if fname is a dir, we extract all the files from it
            DirFileList=os.listdir(path+"\\"+fname)
            flist[count]=[ fname,DirInDir(path,DirFileList,fname)]
    return flist

def creatF(path,names):
    flist=[]
    for i in names:
        print(path+"\\"+i)
        print("ssss")
        print(os.stat(path+"\\"+i).st_size)
        flist.append(File(path+"\\"+i,os.stat(path+"\\"+i).st_size))
    return flist

def main():
    flist=[]
    counter=-1
    WrongOption=True

    while WrongOption:
        choise = input("Hi!, we are going to make a list of all the" + '"' + "bad" + '"' + " files. \n"
          " Chose by path or all the pc\n")
        if choise=='p':
            try:
                path=input("Enter the path")
                flistname=ByDir(path)
                print(flistname)
                WrongOption=False
            except Exception as e:
                print(e)
        elif choise=='a':
            AllpC()
            WrongOption=False
        else:print("wrong option chose again")

    for name in flistname:
        counter+=1
        if len(name)>1:
            flist.append("This is "+name[0]+" dir", creatF(path+"\\"+name[0],name[1]))
        flist.append(File(path+"\\"+name,os.stat(path+"\\"+name).st_size))
    for i in flist:
        print(i.__str__())




main()
