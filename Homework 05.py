# 이중연결리스틀르 위한 노드 구현
class DNode : 
    def __init__(self, elem, prev=None, next=None) : 
        self.data = elem
        self.prev = prev
        self.next = next
        
# 이중연결리스트를 활용한 덱 구현
class DoubleLinkedDeque : 
    
    def __init__(self) : 
        self.front = None
        self.rear = None
        self.size = 0
    
    def isEmpty(self) : 
        return self.front == None
    
    def size(self) : 
        return self.size
    
    def addFront(self, item) : 
        node = DNode(item, None, self.front)
        if self.isEmpty() : 
            self.front = self.rear = node
        else : 
            self.front.prev = node
            self.front = node
        self.size += 1
   
    def addRear(self, item) : 
        node = DNode(item, self.rear, None)
        if self.isEmpty() : 
            self.front = self.rear = node
        else : 
            self.rear.next = node
            self.rear = node
        self.size += 1
    
    def deleteFront(self) : 
        if self.isEmpty() : 
            print('underflow')
            self.size = -1
        else : 
            data = self.front.data
            self.front = self.front.next
            if self.front == None : 
                self.rear = None
            else : 
                self.front.prev = None
            self.size -= 1
            return data
        
    def deleteRear(self) : 
        if self.isEmpty() : 
            print('underflow')
            self.size = -1
        else :
            data = self.rear.data
            self.rear = self.rear.prev
            if self.rear == None : 
                self.front = None
            else : 
                self.rear.next = None
            self.size -= 1
            return data
        
    def display(self) : 
        p = self.front
        print(' ', end='')
        for _ in range(self.size) : 
            print(p.data, end=' ')
            p = p.next
        print()


# 프로그램 실행
aaa = int(input())
myDeque = DoubleLinkedDeque()
for _ in range(0,aaa,1) : 
    bbb = input()
    bbb = bbb.split()
    if bbb[0] == 'AF' : 
        myDeque.addFront(bbb[1])
    elif bbb[0] == 'AR' : 
        myDeque.addRear(bbb[1])
    elif bbb[0] == 'DF' : 
        myDeque.deleteFront()
    elif bbb[0] == 'DR' : 
        myDeque.deleteRear()
    elif bbb[0] == 'P' : 
        myDeque.display()
    if myDeque.size < 0 :
        break