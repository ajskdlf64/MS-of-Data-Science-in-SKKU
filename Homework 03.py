# 문제 1번 구현
def stack_push (stack, char) : 
    stack.insert(0, char) 

def stack_pop (stack) : 
    if len(stack) == 0 : 
        print('Stack Empty')
    else : 
        stack.pop(0)

def stack_peek (stack) : 
    if len(stack) == 0 : 
        print('Stack Empty')
    else : 
         print(stack.pop(0))

def stack_duplicate(stack) : 
    last = stack.pop(0)
    stack.insert(0, last)
    stack.insert(0, last)

def stack_uprotae(stack, n) : 
    target = stack.pop(0)
    stack.insert(int(n)-1, target)

def stack_downrotae(stack, n) : 
    target = stack.pop(int(n)-1)
    stack.insert(0, target)
    
def stack_print (stack) : 
    for char in stack : 
        print(char, end='')
    print()

# 문제 1번 명령 처리
def run (cmd) : 
    cmd = cmd.split()
    if len(cmd) == 2 :
        cmd_1 = cmd[0]
        cmd_2 = cmd[1]
    else : 
        cmd_1 = cmd[0]
    if cmd_1 == 'PRINT' : 
        stack_print(stack)
    elif cmd_1 == 'PUSH' :
        stack_push(stack, cmd_2)
    elif cmd_1 == 'POP' : 
        stack_pop(stack)
    elif cmd_1 == 'PEEK' : 
        stack_peek(stack)
    elif cmd_1 == 'DUP' : 
        stack_duplicate(stack)
    elif cmd_1 =='UpR' : 
        stack_uprotae(stack, cmd_2)
    elif cmd_1 =='DownR' : 
        stack_downrotae(stack, cmd_2)

# 문제 1번 실행
print()
stack = []
commands = ['POP', 'PUSH s', 'PUSH t', 'PUSH a', 'PUSH r', 
            'PRINT', 'UpR 3', 'PRINT', 'PEEK']
for cmd in commands : 
    run(cmd)
print()
stack = []
commands = ['PUSH s', 'PUSH r', 'PUSH a', 'PUSH t', 'PUSH s', 
           'PRINT', 'DownR 4', 'PRINT', 'POP', 'POP', 'PRINT']
for cmd in commands : 
    run(cmd)
print()
stack = []
commands = ['PUSH d', 'DUP', 'PUSH a', 'PRINT']
for cmd in commands : 
    run(cmd)

print('\n\n\n\n')

# 문제 2번 구현
def MyFunction_02(fomula):
    fomula_len = 0
    stack = []
    yn = "OK"
    for keyword in fomula:
        if keyword in ['[', ']', '(', ')', '{', '}']:
            fomula_len += 1
        if keyword in ['[', '(', '{']:
            stack.append(keyword)
        elif keyword in [']', ')', '}']:
            if len(stack) == 0:
                yn = 'Wrong'
            else:
                left = stack.pop()
                if (keyword == ']') and (left != '[') or\
                   (keyword == ')') and (left != '(') or\
                   (keyword == '}') and (left != '{'):
                    yn = 'Wrong'
    if len(stack) != 0:
        yn = 'Wrong'
    return yn +  '_' + str(fomula_len)

# 문제 2번 실행
commands = ['(3+40*(2+(30-7)*2133)', 
            '3*{4+(2-792)/1} + [3*{4-2* (100 -7)}]', 
            '301*{4+(2101-7)/1} + 9*{4-2* (10108-7)}}', 
            '(3*{4001+(2-7)/1} + [3*{4-2* (1-7)}])']
for cmd in commands : 
    print(cmd, '  -->  ', MyFunction_02(cmd), end='\n\n')