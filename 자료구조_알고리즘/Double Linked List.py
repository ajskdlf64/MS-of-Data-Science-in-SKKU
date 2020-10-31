# 이중연결리스트 구현
class doubleList:
    
    # node 클래스 구현
    class node : 
        def __init__(self, elem, prev, next) : 
            self.elem = elem
            self.prev = prev
            self.next = next
    
    # 초기화
    def __init__(self) : 
        self.head = self.node(None, None, None)
        self.tail = self.node(None, self.head, None)
        self.head.next = self.tail
        self.size = 0

    # 크기
    def size(self): 
        return self.size

    # 비어있는지 체크
    def is_empty(self):
        return self.size == 0

    # 특정 위치의 값 확인
    def search(self, n):
        if self.size < n:
            print('invalid position')
        else:
            p = self.head
            for k in range(n):
                p = p.next
            print(p.elem)

    # 출력
    def printList(self):
        p = self.head.next
        while p != self.tail:
            if p.next != self.tail:
                print(p.elem, end='')
            else:
                print(p.elem)
            p = p.next

    # 원소 추가
    def add(self, n, elem):
        p = self.head
        for _ in range(n):
            p = p.next
        t = p.prev
        n = self.node(elem, t, p)
        p.prev = n
        t.next = n
        self.size += 1
            
    # 원소 삭제
    def delete(self, n):
        x = self.head
        for _ in range(n):
            x = x.next
        f = x.prev
        r = x.next
        f.next = r
        r.prev = f
        self.size -= 1
        return x.elem
        
        
        


# 프로그램 실행
if __name__ == '__main__':
    
    # 인자 받기
    n = int(input())

    # 객체 생성
    myList = doubleList()

    # 받은 인자만큼 반복 실행
    for _ in range(n):
        
        # 각각의 iter에서 실행할 명령
        input_order = input().split()

        # 입력 받는 케이스 지정
        if len(input_order) == 3:
            a, b, c = input_order[0], int(input_order[1]), input_order[2]
        elif len(input_order) == 2:
            a, b = input_order[0], int(input_order[1])
        else:
            a = input_order[0]

        # 받은 명령에 따른 처리
        if a == 'A':
            myList.add(b,c)
        elif a == 'D':
            myList.delete(b)
        elif a == 'G':
            myList.search(b)
        elif a == 'P':
            myList.printList()
