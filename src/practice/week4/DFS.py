from answer.ch04.MazeDFS import isValidPos
from stack import ArrayStack

def DFS() :
    print('DFS :')
    stack = ArrayStack(100)
    stack.push(0,1)

    while not stack.isEmpty() :
        here = stack.pop()
        print(here, end='->')
        (x,y) = here

        if(map[y][x] == 'x') :
            return True 
        
        else :
            map[y][x] = '.'
            if isValidPos(x,y-1) : stack.push((x,y,-1))
            if isValidPos(x,y+1) : stack.push((x,y+1))
            if isValidPos(x-1,y) : stack.push((x-1,y))
            if isValidPos(x+1,y) : stack.push((x+1,y))
        print('현재 스택 :', stack)

        return False