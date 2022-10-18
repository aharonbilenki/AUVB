#Code starts here
class File:
    def __init__(self,path,size):
        self.path= path
        self.size= size
        self.name=path.split('\\')[-1]
        self.type=self.name.split('.')[-1]
        self.data=""

    def FileRead(self):
        with open(self.name,'r') as f:
            self.data=f.read()




