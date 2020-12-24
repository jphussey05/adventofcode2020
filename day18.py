# Given postfix expression will "create a tree" but really just evaluate it in flight
def constructTree(postfix):
    stack = []
    for char in postfix :
        if not isOperator(char):
            stack.append(char)
        else:
           
            stack.append(eval(f'{stack.pop()}{char}{stack.pop()}'))
 
    t = stack.pop()
    return t


def isOperator(c):
    if (c in '*+()'):
        return True
    else:
        return False     


def infix2postfix(infix):
    stack, postfix = [], []
    
    for char in infix:
        if not isOperator(char):    # char is an operand
            postfix.append(char)
        else:                       # char is operator
            # all operators are lower precedence from left to right if we ignore parens for now
            # higher precedence "+" gets pushed on top of "*"
            if not stack:   # stack is empty, push
                stack.append(char)
            else:   # stack exists and char is highest precedence + or is left paren
                if char == '+' or char == '(':
                    stack.append(char)
                elif char == ')':  # pop stack until opening paren
                    tmp = stack.pop()
                    while tmp != '(':
                        postfix.append(tmp)
                        tmp = stack.pop()
                elif char == '*':  # lowest precedence operator, stack isn't empty, so check for a +
                    while stack[-1] == '+': 
                        postfix.append(stack.pop())   # loop until we've popped all +
                        if not stack:
                            break
                    stack.append(char)        # now that we have all the higher precedents out, put the * on stack
                else:
                    raise BaseException(f'Not sure what to do with {char} while stack is {stack}')

    while stack:   # pop all the remaining ops off stack 
        postfix.append(stack.pop())
    
    return postfix
    

if __name__ == "__main__":
    with open('day18.txt') as fin:
        contents = [line.strip().replace(' ', '') for line in fin.readlines()]

    total = 0
    for infix in contents:
        
        postfix = ''.join(infix2postfix(infix))
        tree  = constructTree(postfix)
        total += tree

    print(total)