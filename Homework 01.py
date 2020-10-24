# 문제 01
def die3 (x,y,z) : 
    if x + y + z == N : 
        print(x,y,z)
    return None

def die2 (x,y) :
    for z in range(1,7,1) : 
        die3(x,y,z)
    return None

def die1 (x) : 
    for y in range(1,7,1) : 
        die2(x,y)
    return None

def main () :
    global N
    N = int(input())
    for x in range(1,7,1) : 
        die1(x)
    return None



# 문제 02
def question_02 () : 
    N,M = input().split()
    N,M = int(N), int(M)
    if N >= M : 
        big,small = N,M
    else : 
        big,small = M,N
    print(big // small)
    print(big % small)


# 문제 03
def question_03 () :
    N = int(input())   
    print(int((N >= 20) and (N <= 30)))



# 문제 04
def question_04 () : 
    N = input()    
    while True :
        N, value, cnt = str(N), 0, 0  
        while cnt <  len(N) : 
            value += int(N[cnt])
            cnt += 1
        N = str(value)   
        if int(N) < 10 : 
            break
    return int(N)