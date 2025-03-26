from stack import ArrayStack

def reverse_string() :
    s = ArrayStack(100)

    string = input ("문자열 입력")

    for i in string :
        s.push(i)

    while not s.isEmpty() :
        print(s.pop(),end='')

def checkBrackets(statement):
    s = ArrayStack(100)

    for c in statement :
        if c == '{' or c == '[' or c == '(' :
            s.push(c)

        elif c == '}' or c == ']' or c == ')' :
            if s.isEmpty() :
                return False
            else :
                left = s.pop()
                if(c == "}" and left != "{" ) or (c == "]" and left != "[" ) or (c == ")" and left != "(") :
                    return False
                
    return s.isEmpty()

def evalPostfix(expr) :
    s = ArrayStack(100)

    for token in expr :
        if token in "+-*/" :
            val2 = s.pop()
            val1 = s.pop()
            if(token == '+') : s.push(val1 + val2)
            elif(token =='-') : s.push(val1 - val2)
            elif(token =='*') : s.push(val1 * val2)
            elif(token =='/') : s.push(val1 / val2)

        else :
            s.push (float(token))

    return s.pop