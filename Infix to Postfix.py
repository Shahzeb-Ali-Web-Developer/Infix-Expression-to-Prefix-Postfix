class Stack:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        else:
            print("Stack is empty. Cannot pop.")
            return None

    def peek(self):
        if not self.is_empty():
            return self.items[-1]
        else:
            print("Stack is empty. Cannot peek.")
            return None

    def size(self):
        return len(self.items)

    def display(self):
        print("Current stack:")
        print(self.items)



def precedence(operator):
    if operator == '+' or operator == '-':
        return 1
    elif operator == '*' or operator == '/':
        return 2
    else:
        return 0

def convertToPostfix(infix_expression):
    postfix = ""
    stack = Stack()

    for char in infix_expression:
        if char.isalnum():
            postfix += char
        elif char == '(':
            stack.push(char)
        elif char == ')':
            while stack.items and stack.items[-1] != '(':
                postfix += stack.pop()
            stack.pop()

        else:
            while stack.items and precedence(stack.items[-1]) >= precedence(char):
                postfix += stack.pop()
            stack.push(char)
        #print(stack)

    while stack.items:
        postfix += stack.pop()


    return postfix


def display_expression(expression):
    print("Exp:", expression)

def input_expression():
    return input("Enter infix exp: ")

if __name__ == '__main__':
    infix_expression = input_expression()
    display_expression(infix_expression)
    postfix_expression = convertToPostfix(infix_expression)
    display_expression(postfix_expression)