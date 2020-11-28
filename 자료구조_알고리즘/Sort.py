# Selection Sort
def selection_sort(A, B) : 
    n = len(A)
    for i in range(n-1) : 
        least = i
        for j in range(i+1, n):
            if A[j] < A[least] : 
                least = j
        A[i], A[least] = A[least], A[i]
        B[i], B[least] = B[least], B[i]
        print('Step {}  : {}' .format(i,A))

# Program Run
if __name__ == "__main__" :
    print('\n[Selection Sort]\n')
    records = []
    player = []
    num = int(input('마라토너의 수를 입력하시오 : ')) 
    print('마라토너의 기록을 초단위로 입력 : ')
    for _ in range(num) : 
        value = int(input())
        records.append(value)
    print('마라토너의 선수 번호 입력 : ')
    for _ in range(num) : 
        key = int(input())
        player.append(key)
    print('\n정렬 전 :', records)
    selection_sort(records, player)
    print('정렬 후 :', records, end='\n\n')
    for k in range(3) : 
        HOUR = records[k] // 3600
        MIN = (records[k] - HOUR*3600) // 60
        SEC = records[k] % 60
        print('{}등 : 선수 번호({:>2})  {}시간 {:>2}분 {}초' .format(k+1, player[k], HOUR, MIN, SEC))




# Shell Sort
def sortGapInsertion(A, B, first, last, gap) : 
    for i in range(first+gap, last+1, gap) : 
        key = A[i]
        key_2 = B[i]
        j = i - gap
        while (j >= first) and (key < A[j]) : 
            A[j+gap] = A[j]
            B[j+gap] = B[j]
            j -= gap
        A[j+gap] = key
        B[j+gap] = key_2

def shell_sort(A, B) : 
    n = len(A)
    gap = n//2
    while gap > 0 : 
        if (gap % 2) == 0 : 
            gap += 1
        for i in range(gap) : 
            sortGapInsertion(A, B, i, n-1, gap)
        print('gap = {} : {}' .format(gap,A))
        gap = gap//2
    return None

# Program Run
if __name__ == "__main__" :
    print('\n[Shell Sort]\n')
    records = []
    player = []
    num = int(input('마라토너의 수를 입력하시오 : ')) 
    print('마라토너의 기록을 초단위로 입력 : ')
    for _ in range(num) : 
        value = int(input())
        records.append(value)
    print('마라토너의 선수 번호 입력 : ')
    for _ in range(num) : 
        key = int(input())
        player.append(key)
    print('\n정렬 전 :', records)
    shell_sort(records, player)
    print('정렬 후 :', records, end='\n\n')
    for k in range(3) : 
        HOUR = records[k] // 3600
        MIN = (records[k] - HOUR*3600) // 60
        SEC = records[k] % 60
        print('{}등 : 선수 번호({:>2})  {}시간 {:>2}분 {}초' .format(k+1, player[k], HOUR, MIN, SEC))