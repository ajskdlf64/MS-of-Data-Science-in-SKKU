# 선형조사법
class Linear : 

    def __init__ (self, size) : 
        self.M = size
        self.a = [None] * size
        self.d = [None] * size

    def hash (self, key) : 
        return key % self.M

    def put (self, key, data) : 
        initial_position = self.hash(key)
        i = initial_position
        j = 0
        while True : 
            if self.a[i] == None : 
                self.a[i] = key
                self.d[i] = data
            if self.a[i] == key : 
                self.d[i] = data
                return
            j += 1
            i = (initial_position + j) % self.M
            if i == initial_position : 
                break

    def print_table (self) :
        for i in range(self.M) : 
            print('{:8}' .format(str(i)), end='')
        print()
        for i in range(self.M) : 
            print('{:8}' .format(str(self.a[i])), end='')
        print()

if __name__ == '__main__' : 
    print('\n\n선형조사법')
    t = Linear(11)
    t.put(12, 'A')
    t.put(44, 'B')
    t.put(13, 'C')  
    t.put(88, 'D')
    t.put(23, 'E')
    t.put(94, 'F')
    t.put(11, 'G')
    t.put(39, 'H')
    t.put(20, 'I')
    t.put(16, 'J')
    t.put(5, 'K')
    t.print_table()
    print('\n\n')



# 이차조사법
class Quad : 
    
    def __init__ (self, size) : 
        self.M = size
        self.a = [None] * size
        self.d = [None] * size
        self.N = 0

    def hash (self, key) : 
        return key % self.M
        
    def put (self, key, data) : 
        initial_position = self.hash(key)
        i = initial_position
        j = 0
        while True : 
            if self.a[i] == None : 
                self.a[i] = key
                self.d[i] = data
                self.N += 1 
                return
            if self.a[i] == key : 
                self.d[i] = data
                return
            j += 1 
            i = (initial_position + j*j) % self.M
            if self.N > self.M : 
                break
        
    def print_table (self) :
        for i in range(self.M) : 
            print('{:8}' .format(str(i)), end='')
        print()
        for i in range(self.M) : 
            print('{:8}' .format(str(self.a[i])), end='')
        print()

if __name__ == '__main__' : 
    print('이차조사법')
    t = Quad(11)
    t.put(12, 'A')
    t.put(44, 'B')
    t.put(13, 'C')
    t.put(88, 'D')
    t.put(23, 'E')
    t.put(94, 'F')
    t.put(11, 'G')
    t.put(39, 'H')
    t.put(20, 'I')
    t.put(16, 'J')
    t.put(5, 'K')
    t.print_table()
    print('\n\n')



# 이중해시법
class Double : 
    def __init__ (self,size) : 
        self.M = size
        self.a = [None] * size
        self.d = [None] * size
        self.N = 0

    def hash (self, key) : 
        return key % self.M

    def put (self, key, data) : 
        initial_position = self.hash(key)
        i = initial_position
        d = 7 - (key  % 7)
        j = 0
        while True : 
            if self.a[i] == None : 
                self.a[i] = key
                self.d[i] = data
                self.N += 1 
                return
            if self.a[i] == key : 
                self.d[i] = data
                return
            j += 1 
            i = (initial_position + j*d) % self.M
            if self.N > self.M : 
                break
        
    def print_table (self) :
        for i in range(self.M) : 
            print('{:8}' .format(str(i)), end='')
        print()
        for i in range(self.M) : 
            print('{:8}' .format(str(self.a[i])), end='')
        print()

if __name__ == '__main__' : 
    print('이중해시법')
    t = Double(11)
    t.put(12, 'A')
    t.put(44, 'B')
    t.put(13, 'C')
    t.put(88, 'D')
    t.put(23, 'E')
    t.put(94, 'F')
    t.put(11, 'G')
    t.put(39, 'H')
    t.put(20, 'I')
    t.put(16, 'J')
    t.put(5, 'K')
    t.print_table()
    print('\n\n')



# 체이닝법
class Chaining : 

    class Node : 
        def __init__ (self, key, data, link) : 
            self.key = key
            self.data = data
            self.next = link
    
    def __init__(self, size) : 
        self.M = size
        self.a = [None] * size

    def hash (self, key) : 
        return key % self.M

    def put (self, key, data) : 
        i = self.hash(key)
        p = self.a[i]
        while p != None : 
            if key == p.key : 
                p.data = data
                return
            p = p.next
        self.a[i] = self.Node(key, data, self.a[i])

    def print_table(self) : 
        for i in range(self.M) : 
            print('{:4}' .format(i), end='')
            p = self.a[i]
            while p != None : 
                print(' --> [{}, {}]' .format(p.key, p.data), end='')
                p = p.next
            print()


if __name__ == '__main__' : 
    print('체이닝법')
    t = Chaining(11)
    t.put(12, 'A')
    t.put(44, 'B')
    t.put(13, 'C')
    t.put(88, 'D')
    t.put(23, 'E')
    t.put(94, 'F')
    t.put(11, 'G')
    t.put(39, 'H')
    t.put(20, 'I')
    t.put(16, 'J')
    t.put(5, 'K')
    t.print_table()
    print('\n\n')