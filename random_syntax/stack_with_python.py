def create_stack():
    stack = []
    return stack

def check_empty(stack):
    return len(stack) == 0

def push(stack, new_item):
    stack.append(new_item)

def pop(stack):
    if check_empty(stack):
        return "empty"
    return stack.pop()

stack = create_stack()
push(stack, 2)
push(stack, 43)
push(stack, 3)
print(pop(stack))