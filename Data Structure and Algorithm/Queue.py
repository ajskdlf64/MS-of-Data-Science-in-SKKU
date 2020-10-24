# 원형 큐
MAX_QSIZE = 10
class myQueue : 

    def __init__(self) :
        self.front = 0
        self.rear = 0
        self.items = [0] * MAX_QSIZE
        
    def isEmpty (self) : 
        return self.front == self.rear

    def isFull (self) : 
        return self.front == (self.rear+1)%MAX_QSIZE
        
    def enqueue (self, item) : 
        if not self.isFull() : 
            self.rear = (self.rear+1)%MAX_QSIZE
            self.items[self.rear] = item
        else :
            print('overflow', end=' ')
            for item in self.items : 
                print(item, end=' ')
                self.items = []

    def dequeue (self) : 
        if not self.isEmpty() :
            self.items[self.front+1] = 0
            self.front = (self.front+1)%MAX_QSIZE
        else :
            print('underflow', end=' ')
            for item in self.items : 
                print(item, end=' ')
                self.items = []
    
    def display(self) : 
        print(' ', end='')
        for item in self.items : 
            print(item, end=' ')
        print()
        
        
# 주어진 comman에 의해 명령 수행
def INSERT (queue, item) : 
    queue.enqueue(item)
    
def DELETE (queue) : 
    queue.dequeue()

def PRINT (queue) : 
    queue.display()
    
    
    
# 명령 프로그램
def myProgram() : 
    
    q = int(input())
    n = int(input())
    
    global MAX_QSIZE
    MAX_QSIZE = q
    my_queue = myQueue()

    for _ in range(n):
        cmd = str(input()).split()
        if len(cmd) == 2 : 
            cmd_1, cmd_2 = cmd[0], cmd[1]
        else :
            cmd_1 = cmd[0]
        if cmd_1 == 'I' : 
            INSERT(my_queue, cmd_2)
        elif cmd_1 == 'D' : 
            DELETE(my_queue)
        elif cmd_1 == 'P' : 
            PRINT(my_queue)
        if len(my_queue.items) == 0 :
            break



# 실행
myProgram()