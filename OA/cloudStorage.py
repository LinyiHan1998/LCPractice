class CloudStorage:
    def __init__(self) -> None:
        self.storage = {}
        self.arr = []
    def ADD_FILE(self,name,size):
        if name in self.storage:
            return False
        self.storage[name] = size
        self.arr.append(name)
        return True
    def COPY_FILE(self,nameFrom,nameTo):
        if nameFrom not in self.storage or self.isDIR(nameFrom) or nameTo in self.storage:
            return False
        self.storage[nameTo] = self.storage[nameFrom]
        return True
    def GET_FILE_SIZE(self,name):
        if name not in self.storage:
            return
        return self.storage[name]

    def isDIR(self,name):
        #see if a file name if a file or directory
        arr = name.split('/')
        if '.' in arr[-1]:
            #not dir
            return False
            
        else:
            return True
    def FIND_FILE(self,dir,name):
        for a in self.arr:
            if dir not in a:
                continue
            n = len(name)
            tmp = len(a)
            if tmp > n and a[tmp-n:] == name:
                return a
        return


def solution(queries):
    s = CloudStorage()
    for query in queries:
        if query[0] == "ADD_FILE":
            print(s.ADD_FILE(query[1],query[2]))
        elif query[0] == "COPY_FILE":
            print(s.COPY_FILE(query[1],query[2]))
        elif query[0] == "GET_FILE_SIZE":
            print(s.GET_FILE_SIZE(query[1]))
        elif query[0] == "FIND_FILE":
            print(s.FIND_FILE(query[1]))

if __name__ == '__main__':
    queries = [
    ["ADD_FILE","/root/dir/another_dir"]
    ]
