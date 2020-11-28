# DFS
adj_list = [[-1], [2,3,4,6], [1,4,5,7], [1,6], [1,2,7], [2,7], [1,3,7], [2,4,5,6,8], [7]]
visited = [None]*len(adj_list)

def DFS (v) : 
    visited[v] = True
    print(v, end=' ')
    for w in adj_list[v] : 
        if not visited[w] : 
            DFS(w)

print('[DFS]')
num = int(input('입력 : '))
print('출력 : ', end='')
DFS(num)

# BFS 
adj_list = [[-1], [2,3,4,6], [1,4,5,7], [1,6], [1,2,7], [2,7], [1,3,7], [2,4,5,6,8], [7]]
visited = [None]*len(adj_list)

def BFS (i) : 
    queue = []
    visited[i] = True
    queue.append(i)
    while len(queue) != 0 : 
        v = queue.pop(0)
        print(v, end=' ')
        for w in adj_list[v] : 
            if not visited[w] : 
                visited[w] = True
                queue.append(w)

print('\n[BFS]')
num = int(input('입력 : '))
print('출력 : ', end='')
BFS(num)