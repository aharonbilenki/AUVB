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
        if os.path.isdir(path + "\\" +DirName+"\\"+fname):  # if fname is a dir, we extract all the files from it
            DirFileList = os.listdir(path + "\\" +DirName+"\\"+fname)
            flist.append([fname, DirFileList])
            temp=DirFileList
    return flist
def ByDir(path):
    count=-1
    flist1=os.listdir(path)
    flist=flist1
    for fname in flist:
        count+=1
        if os.path.isdir(path+"\\"+fname):#if fname is a dir, we extract all the files from it
            DirFileList=os.listdir(path+"\\"+fname)
            flist[count]=[ fname,DirInDir(path,DirFileList,fname)]
    return flist

def creatF(path,names):
    flist=[]
    TempFlist=[]
    for i in names:
        if type(i) is list:
            TempPath=path+"\\"+i[0]
            for fname in i[1]:
                FnamePath=TempPath+"\\"+fname
                TempFlist.append(File.File(FnamePath,os.stat(FnamePath).st_size))
            flist.append(["This files are in "+i[0]+" Dir",TempFlist])
        print("ssss")
        flist.append(File.File(path+"\\"+i,os.stat(path+"\\"+i).st_size))
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
                #print(flistname)
                WrongOption=False
            except Exception as e:
                print(e)
        elif choise=='a':
            AllpC()
            WrongOption=False
        else:print("wrong option chose again")

    for name in flistname:
        counter+=1
        if type(name) is list:
            flist.append("This is "+name[0]+" dir", creatF(path+"\\"+name[0],name[1]))
        flist.append(File.File(path+"\\"+name,os.stat(path+"\\"+name).st_size))

    #for i in flist:
        #print(i.__str__())




main()
