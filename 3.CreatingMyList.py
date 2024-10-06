import ctypes

class Mylist:
    def __init__(self):
        self.size = 1
        self.no = 0
        #Create a C type array with size = self.size
        self.A = self.__create_array(self.size)

    def __create_array(self, capacity):
        # creates a C type array(static,referential) with size capacity
        return (capacity*ctypes.py_object)()

    def __len__(self):
        return self.no

    def append(self,item):
        if self.size == self.no:
        #resize
            self.__resize(self.size*2)
        #append
        self.A[self.no] = item
        self.no += 1

    def __resize(self,new_capacity):
        #create a new array with new capacity
        B = self.__create_array(new_capacity)
        self.size = new_capacity
        #copy the content of A to B
        for i in range(self.no):
            B[i] = self.A[i]
        # reassign A
        self.A = B

    def __str__(self):
        #[1,2,3]
        result = ''
        for i in range(self.no):
            result += str(self.A[i]) + ','
        return '[' +result[:-1]+ ']'

    def __getitem__(self, index):
        if 0 <= index < self.no:
            return self.A[index]
        return 'Index Error'
    def pop(self):
        if self.no == 0:
            return 'Empty List'
        print('Popped item :',self.A[self.no-1])
        self.no -= 1

    def __delitem__(self,index):
        if 0 <= index < self.no:
            for i in range(index,self.no-1):
                self.A[i] = self.A[i+1]
            self.no -= 1
        else:
            return 'IndexError'

    def remove(self,item):
        pos = self.find(item)
        if type(pos) == int:
            self.__delitem__(pos)
        else:
            return pos

    def clear(self):
        self.size = 1
        self.no = 0

    def find(self,item):
        for i in range(self.no):
            if self.A[i] == item:
                return i
        return 'ValueError- item is not in the list'
    
    def insert(self,position, item):  #[1, 2, 3, INSERT, 4, 5]
        if self.size == self.no:
            self.__resize(self.size*2)
        for i in range(self.no,position,-1):
            self.A[i] = self.A[i-1]
        self.A[position] = item
        self.no += 1

l  = Mylist()
# print(len(l))
print(l)
l.append(1)
l.append(2)
l.append(3)
l.append('abc')
# print(l.find(66))
# print(l.find(3))
l.insert(1,'hello')
print(l)
l.__delitem__(3)
del l[1]
print(l)
# print(l[0])
# l.pop()
# l.clear()
print(l.remove('abc'))
print(l)
print(l[1:3])